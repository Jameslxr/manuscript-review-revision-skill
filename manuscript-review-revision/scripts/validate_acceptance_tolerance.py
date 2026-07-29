#!/usr/bin/env python3
"""Validate the accepted-paper calibration card used before full review."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


TOP_LEVEL_FIELDS = {
    "target_journal",
    "article_type",
    "accessed_at",
    "status",
    "comparators",
    "substitution_reason",
    "synthesis",
}
COMPARATOR_FIELDS = {
    "id",
    "citation",
    "url",
    "publication_date",
    "journal",
    "article_type",
    "match_level",
    "design",
    "unit_of_inference",
    "scale",
    "validation",
    "limitations",
    "claim_ceiling",
    "data_code_access",
    "comparability_notes",
}
MATCH_LEVELS = {
    "EXACT_JOURNAL_AND_TYPE",
    "EXACT_JOURNAL_ADJACENT_TYPE",
    "ADJACENT_JOURNAL_AND_TYPE",
}
SYNTHESIS_FIELDS = {
    "mandatory_official_requirements",
    "validity_floor",
    "competitiveness_expectations",
    "accepted_with_limitations",
    "optional_strengthening",
    "calibration_boundary",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate an accepted-paper tolerance calibration JSON."
    )
    parser.add_argument("card", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_date(value: object) -> bool:
    if not nonempty_string(value):
        return False
    try:
        date.fromisoformat(str(value))
    except ValueError:
        return False
    return True


def valid_url(value: object) -> bool:
    if not nonempty_string(value):
        return False
    parsed = urlparse(str(value))
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(card: object) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(card, dict):
        return {
            "status": "FAIL",
            "comparator_count": 0,
            "exact_match_count": 0,
            "errors": ["Card root must be a JSON object."],
            "warnings": [],
        }

    missing = sorted(TOP_LEVEL_FIELDS - set(card))
    if missing:
        errors.append(f"Missing top-level fields: {missing}")

    for field in ("target_journal", "article_type"):
        if not nonempty_string(card.get(field)):
            errors.append(f"{field} must be a non-empty string.")
    if not valid_date(card.get("accessed_at")):
        errors.append("accessed_at must be an ISO date (YYYY-MM-DD).")

    declared_status = str(card.get("status", "")).strip().upper()
    if declared_status not in {"PASS", "NOT_ASSESSABLE"}:
        errors.append("status must be PASS or NOT_ASSESSABLE.")

    comparators = card.get("comparators")
    if not isinstance(comparators, list):
        errors.append("comparators must be a list.")
        comparators = []

    exact_matches = 0
    seen_ids: set[str] = set()
    for index, comparator in enumerate(comparators, start=1):
        prefix = f"comparator {index}"
        if not isinstance(comparator, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        missing_comparator = sorted(COMPARATOR_FIELDS - set(comparator))
        if missing_comparator:
            errors.append(f"{prefix} missing fields: {missing_comparator}")
        comparator_id = str(comparator.get("id", "")).strip()
        if not comparator_id:
            errors.append(f"{prefix}: id must be non-empty.")
        elif comparator_id in seen_ids:
            errors.append(f"{prefix}: duplicate id {comparator_id!r}.")
        seen_ids.add(comparator_id)

        for field in (
            "citation",
            "journal",
            "article_type",
            "design",
            "unit_of_inference",
            "scale",
            "validation",
            "claim_ceiling",
            "data_code_access",
            "comparability_notes",
        ):
            if not nonempty_string(comparator.get(field)):
                errors.append(f"{prefix}: {field} must be non-empty.")
        if not valid_url(comparator.get("url")):
            errors.append(f"{prefix}: url must be an HTTP(S) URL.")
        if not valid_date(comparator.get("publication_date")):
            errors.append(f"{prefix}: publication_date must be an ISO date.")

        match_level = str(comparator.get("match_level", "")).strip().upper()
        if match_level not in MATCH_LEVELS:
            errors.append(
                f"{prefix}: match_level must be one of {sorted(MATCH_LEVELS)}."
            )
        elif match_level == "EXACT_JOURNAL_AND_TYPE":
            exact_matches += 1

        limitations = comparator.get("limitations")
        if not isinstance(limitations, list) or not all(
            nonempty_string(item) for item in limitations
        ):
            errors.append(
                f"{prefix}: limitations must be a list of non-empty strings."
            )

    synthesis = card.get("synthesis")
    if not isinstance(synthesis, dict):
        errors.append("synthesis must be an object.")
    else:
        missing_synthesis = sorted(SYNTHESIS_FIELDS - set(synthesis))
        if missing_synthesis:
            errors.append(f"synthesis missing fields: {missing_synthesis}")
        for field in SYNTHESIS_FIELDS:
            value = synthesis.get(field)
            if field == "calibration_boundary":
                if not nonempty_string(value):
                    errors.append("synthesis.calibration_boundary must be non-empty.")
            elif not isinstance(value, list) or not all(
                nonempty_string(item) for item in value
            ):
                errors.append(
                    f"synthesis.{field} must be a list of non-empty strings."
                )

    if declared_status == "PASS" and len(comparators) < 5:
        errors.append("PASS requires at least five accepted-paper comparators.")
    if declared_status == "PASS" and exact_matches < 5:
        if not nonempty_string(card.get("substitution_reason")):
            errors.append(
                "Fewer than five exact journal/article-type matches requires a "
                "non-empty substitution_reason."
            )
        else:
            warnings.append(
                f"Only {exact_matches} exact journal/article-type comparators; "
                "substitution is disclosed."
            )
    if declared_status == "NOT_ASSESSABLE" and not nonempty_string(
        card.get("substitution_reason")
    ):
        errors.append("NOT_ASSESSABLE requires a reason in substitution_reason.")

    return {
        "status": "PASS" if not errors else "FAIL",
        "declared_status": declared_status,
        "comparator_count": len(comparators),
        "exact_match_count": exact_matches,
        "errors": errors,
        "warnings": warnings,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Acceptance-tolerance validation: {report['status']}",
        f"Declared status: {report.get('declared_status', 'UNKNOWN')}",
        f"Comparators: {report.get('comparator_count', 0)}",
        f"Exact journal/type matches: {report.get('exact_match_count', 0)}",
    ]
    lines.extend(f"WARNING: {item}" for item in report.get("warnings", []))
    lines.extend(f"ERROR: {item}" for item in report.get("errors", []))
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        card = json.loads(args.card.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read card: {exc}", file=sys.stderr)
        return 2
    report = validate(card)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
