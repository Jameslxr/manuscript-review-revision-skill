#!/usr/bin/env python3
"""Validate reviewer concerns, evidence anchors, and cross-review status."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


REQUIRED_COLUMNS = {
    "concern_id",
    "issue_key",
    "reviewer_id",
    "role_id",
    "axis",
    "severity",
    "claim_pointer",
    "evidence_pointer",
    "evidence_status",
    "concern",
    "resolution_test",
    "journal_gate",
    "confidence",
    "consensus_status",
    "disposition",
}
AXES = {
    "journal-fit",
    "novelty-significance",
    "mechanism-evidence",
    "experimental-design",
    "statistical-rigor",
    "reproducibility",
    "clinical-validity",
    "ethical-governance",
    "data-resource-quality",
    "figures-and-tables",
    "writing-clarity",
    "claim-moderation",
    "causal-vs-correlative",
    "reference-support",
}
SEVERITIES = {"BLOCKING", "MAJOR", "MINOR", "EDITORIAL"}
EVIDENCE_STATUSES = {"LOCATED", "LOCATION_NOT_PROVIDED", "NOT_ASSESSABLE"}
CONSENSUS_STATUSES = {"UNIQUE", "CONSENSUS", "DISAGREEMENT"}
DISPOSITIONS = {
    "OPEN",
    "ACCEPTED",
    "PARTIAL",
    "DISPUTED",
    "RESOLVED",
    "NOT_ASSESSABLE",
}
EMPTY_MARKERS = {"", "N/A", "NA", "NONE", "UNKNOWN", "NOT_PROVIDED"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a concern-ledger TSV against a review-panel JSON."
    )
    parser.add_argument("ledger", type=Path)
    parser.add_argument("panel", type=Path)
    parser.add_argument(
        "--max-overlap",
        type=float,
        default=0.35,
        help="Warn when pairwise issue-key overlap exceeds this fraction.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def load_panel(path: Path) -> tuple[dict[str, object], list[str]]:
    errors: list[str] = []
    try:
        panel = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {}, [f"Unable to read panel: {exc}"]
    if not isinstance(panel, dict):
        return {}, ["Panel root must be a JSON object."]
    reviewers = panel.get("reviewers")
    if not isinstance(reviewers, list):
        errors.append("Panel reviewers must be a list.")
    return panel, errors


def load_ledger(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            columns = set(reader.fieldnames or [])
            missing = sorted(REQUIRED_COLUMNS - columns)
            if missing:
                errors.append(f"Missing ledger columns: {missing}")
            rows = [
                {str(key): str(value or "").strip() for key, value in row.items()}
                for row in reader
            ]
    except OSError as exc:
        return [], [f"Unable to read ledger: {exc}"]
    if not rows:
        errors.append("Concern ledger has no rows.")
    return rows, errors


def validate(
    rows: list[dict[str, str]], panel: dict[str, object], max_overlap: float
) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    reviewers = panel.get("reviewers")
    reviewer_roles: dict[str, str] = {}
    if isinstance(reviewers, list):
        for reviewer in reviewers:
            if isinstance(reviewer, dict):
                reviewer_id = str(reviewer.get("agent_id", "")).strip()
                role_id = str(reviewer.get("role_id", "")).strip()
                if reviewer_id:
                    reviewer_roles[reviewer_id] = role_id

    concern_ids: set[str] = set()
    issue_reviewers: dict[str, set[str]] = defaultdict(set)
    issue_statuses: dict[str, set[str]] = defaultdict(set)
    reviewer_issues: dict[str, set[str]] = defaultdict(set)

    for row_number, row in enumerate(rows, start=2):
        prefix = f"row {row_number}"
        concern_id = row.get("concern_id", "")
        issue_key = row.get("issue_key", "")
        reviewer_id = row.get("reviewer_id", "")
        role_id = row.get("role_id", "")

        if not concern_id:
            errors.append(f"{prefix}: concern_id is required.")
        elif concern_id in concern_ids:
            errors.append(f"{prefix}: duplicate concern_id {concern_id!r}.")
        concern_ids.add(concern_id)

        if not issue_key:
            errors.append(f"{prefix}: issue_key is required.")
        if reviewer_id not in reviewer_roles:
            errors.append(f"{prefix}: reviewer_id {reviewer_id!r} is not in the panel.")
        elif reviewer_roles[reviewer_id] != role_id:
            errors.append(
                f"{prefix}: role_id {role_id!r} does not match panel role "
                f"{reviewer_roles[reviewer_id]!r}."
            )

        axis = row.get("axis", "")
        if axis not in AXES:
            errors.append(f"{prefix}: invalid axis {axis!r}.")
        severity = row.get("severity", "").upper()
        if severity not in SEVERITIES:
            errors.append(f"{prefix}: invalid severity {severity!r}.")
        evidence_status = row.get("evidence_status", "").upper()
        if evidence_status not in EVIDENCE_STATUSES:
            errors.append(f"{prefix}: invalid evidence_status {evidence_status!r}.")
        consensus_status = row.get("consensus_status", "").upper()
        if consensus_status not in CONSENSUS_STATUSES:
            errors.append(f"{prefix}: invalid consensus_status {consensus_status!r}.")
        disposition = row.get("disposition", "").upper()
        if disposition not in DISPOSITIONS:
            errors.append(f"{prefix}: invalid disposition {disposition!r}.")

        for field in ("claim_pointer", "concern", "resolution_test"):
            if row.get(field, "").upper() in EMPTY_MARKERS:
                errors.append(f"{prefix}: {field} must be specific and non-empty.")
        if evidence_status == "LOCATED":
            if row.get("evidence_pointer", "").upper() in EMPTY_MARKERS:
                errors.append(
                    f"{prefix}: LOCATED evidence requires a specific evidence_pointer."
                )
        if evidence_status == "NOT_ASSESSABLE" and disposition != "NOT_ASSESSABLE":
            errors.append(
                f"{prefix}: NOT_ASSESSABLE evidence requires NOT_ASSESSABLE disposition."
            )

        try:
            confidence = float(row.get("confidence", ""))
        except ValueError:
            errors.append(f"{prefix}: confidence must be numeric from 0 to 1.")
        else:
            if not 0 <= confidence <= 1:
                errors.append(f"{prefix}: confidence must be from 0 to 1.")

        if issue_key and reviewer_id:
            issue_reviewers[issue_key].add(reviewer_id)
            issue_statuses[issue_key].add(consensus_status)
            reviewer_issues[reviewer_id].add(issue_key)

    for issue_key, reviewer_ids in issue_reviewers.items():
        statuses = issue_statuses[issue_key]
        if len(statuses) > 1:
            errors.append(
                f"Issue {issue_key!r} has inconsistent consensus_status values: "
                f"{sorted(statuses)}."
            )
            continue
        status = next(iter(statuses), "")
        if status in {"CONSENSUS", "DISAGREEMENT"} and len(reviewer_ids) < 2:
            errors.append(
                f"Issue {issue_key!r} is {status} but has fewer than two reviewers."
            )
        if status == "UNIQUE" and len(reviewer_ids) != 1:
            errors.append(
                f"Issue {issue_key!r} is UNIQUE but appears under multiple reviewers."
            )

    pair_overlaps: list[dict[str, object]] = []
    max_observed = 0.0
    for left, right in combinations(sorted(reviewer_issues), 2):
        left_issues = reviewer_issues[left]
        right_issues = reviewer_issues[right]
        denominator = min(len(left_issues), len(right_issues))
        overlap = len(left_issues & right_issues) / denominator if denominator else 0.0
        max_observed = max(max_observed, overlap)
        pair_overlaps.append(
            {"reviewers": [left, right], "overlap": round(overlap, 4)}
        )
        if overlap > max_overlap:
            warnings.append(
                f"Reviewer pair {left}/{right} issue-key overlap is {overlap:.0%}; "
                f"target is at most {max_overlap:.0%}. Inspect role duplication, but do "
                "not invent artificial differences."
            )

    status_counts = Counter(
        next(iter(statuses), "UNKNOWN") for statuses in issue_statuses.values()
    )
    return {
        "status": "PASS" if not errors else "FAIL",
        "concern_count": len(rows),
        "issue_count": len(issue_reviewers),
        "consensus_issue_count": status_counts["CONSENSUS"],
        "disagreement_issue_count": status_counts["DISAGREEMENT"],
        "unique_issue_count": status_counts["UNIQUE"],
        "maximum_pair_overlap": round(max_observed, 4),
        "pair_overlaps": pair_overlaps,
        "errors": errors,
        "warnings": warnings,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Concern ledger validation: {report['status']}",
        f"Concerns: {report.get('concern_count', 0)}",
        f"Issues: {report.get('issue_count', 0)}",
        f"Consensus / disagreement / unique: "
        f"{report.get('consensus_issue_count', 0)} / "
        f"{report.get('disagreement_issue_count', 0)} / "
        f"{report.get('unique_issue_count', 0)}",
        f"Maximum pair overlap: {float(report.get('maximum_pair_overlap', 0)):.0%}",
    ]
    for warning in report.get("warnings", []):
        lines.append(f"WARNING: {warning}")
    for error in report.get("errors", []):
        lines.append(f"ERROR: {error}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    if not 0 <= args.max_overlap <= 1:
        print("--max-overlap must be from 0 to 1.", file=sys.stderr)
        return 2

    panel, panel_errors = load_panel(args.panel)
    rows, ledger_errors = load_ledger(args.ledger)
    report = validate(rows, panel, args.max_overlap)
    report["errors"] = panel_errors + ledger_errors + list(report["errors"])
    if report["errors"]:
        report["status"] = "FAIL"

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
