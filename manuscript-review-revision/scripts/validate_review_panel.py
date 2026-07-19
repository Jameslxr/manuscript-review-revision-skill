#!/usr/bin/env python3
"""Validate reviewer-agent receipts and review artifact closure."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path


CORE_ROLES = {
    "journal-priority",
    "domain-science",
    "study-design",
    "statistics-reproducibility",
    "claim-evidence-reference",
}
COMPLETED_STATUSES = {"COMPLETED", "NOT_ASSESSABLE"}
RECEIPT_SOURCES = {"HOST_NATIVE", "HOST_LOG"}
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a multi-agent manuscript review-panel JSON file."
    )
    parser.add_argument("panel", type=Path)
    parser.add_argument("--minimum", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = value.strip().replace("Z", "+00:00")
    try:
        timestamp = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if timestamp.tzinfo is None:
        return None
    return timestamp


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
        "panel_schema_version",
        "skill_version",
        "host",
        "host_version",
        "target_journal",
        "article_type",
        "manuscript_sha256",
        "journal_profile_sha256",
        "shared_fact_base_sha256",
        "execution_mode",
        "root_is_reviewer",
        "synthesis_started_before_reviews_completed",
        "reviewers",
    ):
        if field not in panel:
            errors.append(f"Missing top-level field: {field}")

    if panel.get("panel_schema_version") != "2.0":
        errors.append("panel_schema_version must be '2.0'.")
    if not SEMVER_RE.fullmatch(str(panel.get("skill_version", ""))):
        errors.append("skill_version must be a semantic version such as '1.3.0'.")
    for field in ("host", "host_version", "target_journal", "article_type"):
        if not isinstance(panel.get(field), str) or not str(panel.get(field)).strip():
            errors.append(f"{field} must be a non-empty string.")

    input_hashes = (
        "manuscript_sha256",
        "journal_profile_sha256",
        "shared_fact_base_sha256",
    )
    for field in input_hashes:
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
    task_ids: set[str] = set()
    role_ids: set[str] = set()
    completed = 0
    validated_receipts = 0
    base_dir = panel_path.parent

    for index, reviewer in enumerate(reviewers, start=1):
        prefix = f"reviewers[{index}]"
        if not isinstance(reviewer, dict):
            errors.append(f"{prefix} must be an object.")
            continue

        for field in (
            "agent_id",
            "host_task_id",
            "receipt_source",
            "context_mode",
            "role_id",
            "role",
            "independent",
            "saw_other_reviews",
            "status",
            "started_at",
            "completed_at",
            "input_hashes",
            "report_path",
            "report_sha256",
        ):
            if field not in reviewer:
                errors.append(f"{prefix} missing field: {field}")

        agent_id = str(reviewer.get("agent_id", "")).strip()
        task_id = str(reviewer.get("host_task_id", "")).strip()
        role_id = str(reviewer.get("role_id", "")).strip()
        role = str(reviewer.get("role", "")).strip()
        if not agent_id:
            errors.append(f"{prefix}.agent_id must be non-empty.")
        elif agent_id in agent_ids:
            errors.append(f"Duplicate agent_id: {agent_id}")
        agent_ids.add(agent_id)

        if not task_id:
            errors.append(f"{prefix}.host_task_id must be non-empty.")
        elif task_id in task_ids:
            errors.append(f"Duplicate host_task_id: {task_id}")
        task_ids.add(task_id)

        if not role_id:
            errors.append(f"{prefix}.role_id must be non-empty.")
        elif role_id in role_ids:
            errors.append(f"Duplicate role_id: {role_id}")
        role_ids.add(role_id)
        if not role:
            errors.append(f"{prefix}.role must be non-empty.")

        if reviewer.get("independent") is not True:
            errors.append(f"{prefix}.independent must be true.")
        if reviewer.get("saw_other_reviews") is not False:
            errors.append(f"{prefix}.saw_other_reviews must be false.")
        if reviewer.get("context_mode") != "FRESH_NON_FORK":
            errors.append(f"{prefix}.context_mode must be 'FRESH_NON_FORK'.")
        receipt_source = str(reviewer.get("receipt_source", "")).strip().upper()
        if receipt_source not in RECEIPT_SOURCES:
            errors.append(
                f"{prefix}.receipt_source must be one of {sorted(RECEIPT_SOURCES)}."
            )

        status = str(reviewer.get("status", "")).strip().upper()
        if status in COMPLETED_STATUSES:
            completed += 1
        else:
            errors.append(
                f"{prefix}.status must be COMPLETED or NOT_ASSESSABLE; got {status!r}."
            )

        started_at = parse_timestamp(reviewer.get("started_at"))
        completed_at = parse_timestamp(reviewer.get("completed_at"))
        if started_at is None:
            errors.append(f"{prefix}.started_at must be an ISO-8601 timestamp with timezone.")
        if completed_at is None:
            errors.append(
                f"{prefix}.completed_at must be an ISO-8601 timestamp with timezone."
            )
        if started_at is not None and completed_at is not None:
            if completed_at < started_at:
                errors.append(f"{prefix}.completed_at precedes started_at.")

        reviewer_inputs = reviewer.get("input_hashes")
        inputs_valid = isinstance(reviewer_inputs, dict)
        if not inputs_valid:
            errors.append(f"{prefix}.input_hashes must be an object.")
        else:
            for field in input_hashes:
                expected = str(panel.get(field, "")).lower()
                actual = str(reviewer_inputs.get(field, "")).lower()
                if actual != expected:
                    inputs_valid = False
                    errors.append(
                        f"{prefix}.input_hashes.{field} does not match the frozen panel input."
                    )

        report_value = reviewer.get("report_path")
        report_valid = False
        if not isinstance(report_value, str) or not report_value.strip():
            errors.append(f"{prefix}.report_path must be non-empty.")
        else:
            report_path = Path(report_value)
            if not report_path.is_absolute():
                report_path = base_dir / report_path
            if not report_path.is_file() or report_path.stat().st_size == 0:
                errors.append(f"{prefix}.report_path is missing or empty: {report_path}")
            else:
                reported_hash = str(reviewer.get("report_sha256", "")).lower()
                if not SHA256_RE.fullmatch(reported_hash):
                    errors.append(
                        f"{prefix}.report_sha256 must be a 64-character SHA-256 hex digest."
                    )
                else:
                    actual_hash = sha256_file(report_path)
                    if actual_hash != reported_hash:
                        errors.append(
                            f"{prefix}.report_sha256 does not match {report_path}."
                        )
                    else:
                        report_valid = True

        if (
            task_id
            and receipt_source in RECEIPT_SOURCES
            and reviewer.get("context_mode") == "FRESH_NON_FORK"
            and started_at is not None
            and completed_at is not None
            and completed_at >= started_at
            and inputs_valid
            and report_valid
        ):
            validated_receipts += 1

    if completed < minimum:
        errors.append(
            f"Only {completed} completed independent reviewer agents; minimum is {minimum}."
        )
    if validated_receipts < minimum:
        errors.append(
            f"Only {validated_receipts} reviewer receipts closed against frozen inputs and "
            f"report hashes; minimum is {minimum}."
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
        "validated_receipt_count": validated_receipts,
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
        f"Validated receipts: {report.get('validated_receipt_count', 0)}",
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
