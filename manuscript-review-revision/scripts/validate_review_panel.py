#!/usr/bin/env python3
"""Validate that a review panel used at least five independent reviewer agents."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


CORE_ROLES = {
    "journal-priority",
    "domain-science",
    "study-design",
    "statistics-reproducibility",
    "claim-evidence-reference",
}
COMPLETED_STATUSES = {"COMPLETED", "NOT_ASSESSABLE"}
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a multi-agent manuscript review-panel JSON file."
    )
    parser.add_argument("panel", type=Path)
    parser.add_argument("--minimum", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def validate(panel: object, panel_path: Path, minimum: int) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(panel, dict):
        return {
            "status": "FAIL",
            "errors": ["Panel root must be a JSON object."],
            "warnings": [],
        }

    for field in (
        "target_journal",
        "article_type",
        "manuscript_sha256",
        "journal_profile_sha256",
        "execution_mode",
        "root_is_reviewer",
        "reviewers",
    ):
        if field not in panel:
            errors.append(f"Missing top-level field: {field}")

    for field in ("manuscript_sha256", "journal_profile_sha256"):
        value = str(panel.get(field, ""))
        if not SHA256_RE.fullmatch(value):
            errors.append(f"{field} must be a 64-character SHA-256 hex digest.")

    if panel.get("execution_mode") != "independent_agents":
        errors.append("execution_mode must be 'independent_agents'.")
    if panel.get("root_is_reviewer") is not False:
        errors.append("root_is_reviewer must be false; synthesis does not count as review.")
    if panel.get("synthesis_started_before_reviews_completed") is True:
        errors.append("Synthesis started before independent reviews completed.")

    reviewers = panel.get("reviewers")
    if not isinstance(reviewers, list):
        errors.append("reviewers must be a list.")
        reviewers = []

    agent_ids: set[str] = set()
    role_ids: set[str] = set()
    completed = 0
    base_dir = panel_path.parent

    for index, reviewer in enumerate(reviewers, start=1):
        prefix = f"reviewers[{index}]"
        if not isinstance(reviewer, dict):
            errors.append(f"{prefix} must be an object.")
            continue

        for field in (
            "agent_id",
            "role_id",
            "role",
            "independent",
            "saw_other_reviews",
            "status",
            "report_path",
        ):
            if field not in reviewer:
                errors.append(f"{prefix} missing field: {field}")

        agent_id = str(reviewer.get("agent_id", "")).strip()
        role_id = str(reviewer.get("role_id", "")).strip()
        if not agent_id:
            errors.append(f"{prefix}.agent_id must be non-empty.")
        elif agent_id in agent_ids:
            errors.append(f"Duplicate agent_id: {agent_id}")
        agent_ids.add(agent_id)

        if not role_id:
            errors.append(f"{prefix}.role_id must be non-empty.")
        elif role_id in role_ids:
            errors.append(f"Duplicate role_id: {role_id}")
        role_ids.add(role_id)

        if reviewer.get("independent") is not True:
            errors.append(f"{prefix}.independent must be true.")
        if reviewer.get("saw_other_reviews") is not False:
            errors.append(f"{prefix}.saw_other_reviews must be false.")

        status = str(reviewer.get("status", "")).strip().upper()
        if status in COMPLETED_STATUSES:
            completed += 1
        else:
            errors.append(
                f"{prefix}.status must be COMPLETED or NOT_ASSESSABLE; got {status!r}."
            )

        report_value = reviewer.get("report_path")
        if not isinstance(report_value, str) or not report_value.strip():
            errors.append(f"{prefix}.report_path must be non-empty.")
        else:
            report_path = Path(report_value)
            if not report_path.is_absolute():
                report_path = base_dir / report_path
            if not report_path.is_file() or report_path.stat().st_size == 0:
                errors.append(f"{prefix}.report_path is missing or empty: {report_path}")

    if completed < minimum:
        errors.append(
            f"Only {completed} completed independent reviewer agents; minimum is {minimum}."
        )

    missing_roles = CORE_ROLES - role_ids
    if missing_roles:
        errors.append(f"Missing required role_id values: {sorted(missing_roles)}")

    if len(reviewers) > minimum:
        warnings.append(f"Panel includes {len(reviewers)} reviewers; minimum is {minimum}.")

    return {
        "status": "PASS" if not errors else "FAIL",
        "target_journal": panel.get("target_journal"),
        "reviewer_count": len(reviewers),
        "completed_reviewer_count": completed,
        "roles": sorted(role_ids),
        "errors": errors,
        "warnings": warnings,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Review panel validation: {report['status']}",
        f"Target journal: {report.get('target_journal') or 'UNKNOWN'}",
        f"Reviewer agents: {report.get('reviewer_count', 0)}",
        f"Completed: {report.get('completed_reviewer_count', 0)}",
        f"Roles: {', '.join(report.get('roles', []))}",
    ]
    for warning in report.get("warnings", []):
        lines.append(f"WARNING: {warning}")
    for error in report.get("errors", []):
        lines.append(f"ERROR: {error}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        panel = json.loads(args.panel.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read panel: {exc}", file=sys.stderr)
        return 2

    report = validate(panel, args.panel.resolve(), args.minimum)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
