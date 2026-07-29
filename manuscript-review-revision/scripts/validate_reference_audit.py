#!/usr/bin/env python3
"""Validate a claim-to-reference audit ledger and enforce fail-closed support rules."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


REQUIRED_COLUMNS = {
    "sentence_id",
    "atomic_claim",
    "claim_tier",
    "citation_key",
    "identifier",
    "metadata_status",
    "integrity_status",
    "evidence_basis",
    "support_grade",
    "placement_status",
    "format_status",
    "action",
}
CLAIM_TIERS = {"A_MATERIAL", "B_SUPPORTING", "C_CONTEXT"}
METADATA = {"VERIFIED", "UNVERIFIED", "CONFLICT"}
INTEGRITY = {
    "CLEAR",
    "RETRACTED",
    "CORRECTED",
    "EXPRESSION_OF_CONCERN",
    "NOT_CHECKED",
}
EVIDENCE = {
    "RESULTS_SECTION",
    "FULL_TEXT",
    "ABSTRACT",
    "PUBLISHER_PAGE",
    "METADATA_ONLY",
    "UNAVAILABLE",
}
SUPPORT = {
    "DIRECT_SUPPORT",
    "PARTIAL_SUPPORT",
    "BACKGROUND_ONLY",
    "CONTRADICTS_OR_LIMITS",
    "NOT_ASSESSABLE",
}
PLACEMENT = {"PRECISE", "AMBIGUOUS", "MISPLACED", "MISSING"}
FORMAT = {"PASS", "FAIL", "NOT_ASSESSABLE"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a TSV/CSV claim-reference audit ledger."
    )
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def normalized(row: dict[str, str], field: str) -> str:
    return (row.get(field) or "").strip()


def validate_rows(rows: list[dict[str, str]], columns: set[str]) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    missing = REQUIRED_COLUMNS - columns
    if missing:
        errors.append(f"Missing columns: {sorted(missing)}")
        return {
            "status": "FAIL",
            "row_count": len(rows),
            "errors": errors,
            "warnings": warnings,
        }

    seen_rows: set[tuple[str, str, str]] = set()
    blocked_rows: list[int] = []
    advisory_rows: list[int] = []
    tier_counts = {tier: 0 for tier in sorted(CLAIM_TIERS)}

    for index, row in enumerate(rows, start=2):
        sentence_id = normalized(row, "sentence_id")
        claim = normalized(row, "atomic_claim")
        claim_tier = normalized(row, "claim_tier").upper()
        citation_key = normalized(row, "citation_key")
        identifier = normalized(row, "identifier")
        metadata = normalized(row, "metadata_status").upper()
        integrity = normalized(row, "integrity_status").upper()
        evidence = normalized(row, "evidence_basis").upper()
        support = normalized(row, "support_grade").upper()
        placement = normalized(row, "placement_status").upper()
        format_status = normalized(row, "format_status").upper()
        action = normalized(row, "action")

        for field, value in (
            ("sentence_id", sentence_id),
            ("atomic_claim", claim),
            ("citation_key", citation_key),
            ("action", action),
        ):
            if not value:
                errors.append(f"Row {index}: {field} must be non-empty.")

        for field, value, allowed in (
            ("claim_tier", claim_tier, CLAIM_TIERS),
            ("metadata_status", metadata, METADATA),
            ("integrity_status", integrity, INTEGRITY),
            ("evidence_basis", evidence, EVIDENCE),
            ("support_grade", support, SUPPORT),
            ("placement_status", placement, PLACEMENT),
            ("format_status", format_status, FORMAT),
        ):
            if value not in allowed:
                errors.append(
                    f"Row {index}: {field} must be one of {sorted(allowed)}; got {value!r}."
                )

        if claim_tier in CLAIM_TIERS:
            tier_counts[claim_tier] += 1

        row_key = (sentence_id, claim, citation_key)
        if row_key in seen_rows:
            warnings.append(f"Row {index}: duplicate claim-citation relationship.")
        seen_rows.add(row_key)

        if metadata == "VERIFIED" and not identifier:
            errors.append(f"Row {index}: VERIFIED metadata requires an identifier.")

        if support == "DIRECT_SUPPORT":
            if metadata != "VERIFIED":
                errors.append(
                    f"Row {index}: DIRECT_SUPPORT requires VERIFIED metadata."
                )
            if integrity != "CLEAR":
                errors.append(
                    f"Row {index}: DIRECT_SUPPORT requires integrity_status CLEAR."
                )
            if evidence not in {"FULL_TEXT", "RESULTS_SECTION"}:
                errors.append(
                    f"Row {index}: DIRECT_SUPPORT requires FULL_TEXT or RESULTS_SECTION evidence."
                )
            if placement != "PRECISE":
                errors.append(
                    f"Row {index}: DIRECT_SUPPORT requires PRECISE citation placement."
                )

        high_stakes = claim_tier in {"A_MATERIAL", "B_SUPPORTING"}

        # Retractions and expressions of concern cannot support an affirmative
        # claim at any tier. They are allowed only when the manuscript is
        # explicitly using the record to discuss the integrity event or a
        # limitation.
        if (
            integrity in {"RETRACTED", "EXPRESSION_OF_CONCERN"}
            and support != "CONTRADICTS_OR_LIMITS"
        ):
            blocked_rows.append(index)

        # Complete semantic verification is mandatory for material and
        # supporting claims. Generic context rows may be sampled; incomplete
        # checks remain visible as advisories rather than blocking the entire
        # citation gate.
        risk_signals = (
            metadata in {"UNVERIFIED", "CONFLICT"}
            or integrity == "NOT_CHECKED"
            or support == "NOT_ASSESSABLE"
            or placement in {"AMBIGUOUS", "MISPLACED", "MISSING"}
            or format_status == "NOT_ASSESSABLE"
        )
        if risk_signals:
            (blocked_rows if high_stakes else advisory_rows).append(index)

        # A known target-journal formatting error is a concrete correction at
        # every tier, not an uncertainty to be waived by claim materiality.
        if format_status == "FAIL":
            blocked_rows.append(index)

    if not rows:
        errors.append("Ledger contains no claim-reference rows.")

    blocked_rows = sorted(set(blocked_rows))
    advisory_rows = sorted(set(advisory_rows) - set(blocked_rows))
    if blocked_rows:
        warnings.append(
            "Rows blocking a citation-gate PASS: "
            + ", ".join(str(value) for value in blocked_rows)
        )
    if advisory_rows:
        warnings.append(
            "Context rows requiring follow-up but not blocking a citation-gate PASS: "
            + ", ".join(str(value) for value in advisory_rows)
        )

    status = "FAIL" if errors else ("NOT_ASSESSABLE" if blocked_rows else "PASS")
    return {
        "status": status,
        "row_count": len(rows),
        "tier_counts": tier_counts,
        "blocked_rows": blocked_rows,
        "advisory_rows": advisory_rows,
        "errors": errors,
        "warnings": warnings,
    }


def read_ledger(path: Path) -> tuple[list[dict[str, str]], set[str]]:
    sample = path.read_text(encoding="utf-8-sig")
    delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
    reader = csv.DictReader(sample.splitlines(), delimiter=delimiter)
    return list(reader), set(reader.fieldnames or [])


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Reference audit validation: {report['status']}",
        f"Rows: {report.get('row_count', 0)}",
        f"Blocked rows: {report.get('blocked_rows', [])}",
        f"Advisory rows: {report.get('advisory_rows', [])}",
    ]
    for warning in report.get("warnings", []):
        lines.append(f"WARNING: {warning}")
    for error in report.get("errors", []):
        lines.append(f"ERROR: {error}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        rows, columns = read_ledger(args.ledger)
    except OSError as exc:
        print(f"Unable to read ledger: {exc}", file=sys.stderr)
        return 2

    report = validate_rows(rows, columns)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
