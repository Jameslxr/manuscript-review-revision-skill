#!/usr/bin/env python3
"""Validate closure from a journal format plan to delivered manuscript files."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


AUDIT_STATUSES = {"PASS", "FAIL", "NOT_ASSESSABLE"}
MANUSCRIPT_FIELDS = {
    "role",
    "path",
    "sha256",
    "mechanical_status",
    "paragraph_separation",
    "line_spacing",
    "line_numbering",
    "page_numbering",
    "page_number_position",
    "front_matter_status",
    "front_matter_alignment",
    "anonymization_mode",
    "content_preservation_status",
    "format_release_status",
    "issue_count",
    "rendered_page_count",
    "inspected_pages",
    "visual_status",
}
CHECK_RESULT_FIELDS = {"check_id", "status", "evidence", "output"}
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a journal format audit against its source plan."
    )
    parser.add_argument("plan", type=Path)
    parser.add_argument("audit", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def resolve_output_path(raw_path: object, audit_path: Path) -> Path | None:
    if not non_empty_string(raw_path):
        return None
    path = Path(str(raw_path)).expanduser()
    if not path.is_absolute():
        path = audit_path.parent / path
    return path.resolve()


def validate(plan: object, audit: object, plan_path: Path, audit_path: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(plan, dict):
        return {
            "status": "FAIL",
            "errors": ["Plan root must be a JSON object."],
            "warnings": [],
        }
    if not isinstance(audit, dict):
        return {
            "status": "FAIL",
            "errors": ["Audit root must be a JSON object."],
            "warnings": [],
        }

    for field in (
        "schema_version",
        "target_journal",
        "article_type",
        "submission_stage",
        "plan_sha256",
        "overall_status",
        "manuscripts",
        "checks",
    ):
        if field not in audit:
            errors.append(f"Missing audit field: {field}")

    if str(audit.get("schema_version", "")).strip() != "1.0":
        errors.append("audit schema_version must be '1.0'.")

    for field in ("target_journal", "article_type", "submission_stage"):
        audit_value = str(audit.get(field, "")).strip()
        plan_value = str(plan.get(field, "")).strip()
        if audit_value != plan_value:
            errors.append(
                f"Audit {field} does not match the format plan: "
                f"{audit_value!r} != {plan_value!r}."
            )

    try:
        actual_plan_sha256 = sha256_file(plan_path)
    except OSError as exc:
        errors.append(f"Unable to hash format plan: {exc}")
        actual_plan_sha256 = ""
    recorded_plan_sha256 = str(audit.get("plan_sha256", "")).strip().lower()
    if not SHA256_RE.fullmatch(recorded_plan_sha256):
        errors.append("plan_sha256 must be a 64-character SHA-256 value.")
    elif recorded_plan_sha256 != actual_plan_sha256:
        errors.append("plan_sha256 does not match the supplied format plan.")

    overall_status = str(audit.get("overall_status", "")).strip().upper()
    if overall_status not in AUDIT_STATUSES:
        errors.append(f"overall_status must be one of {sorted(AUDIT_STATUSES)}.")

    plan_status = str(plan.get("plan_status", "")).strip().upper()
    if plan_status != "PASS":
        errors.append(
            "The supplied format plan must have plan_status PASS before audit closure."
        )

    style = plan.get("style_contract")
    if not isinstance(style, dict):
        errors.append("Format plan style_contract must be an object.")
        style = {}
    expected_paragraph_separation = str(
        style.get("paragraph_separation", "")
    ).strip().lower()
    expected_line_spacing = str(style.get("line_spacing", "")).strip().lower()
    expected_line_numbering = str(style.get("line_numbering", "")).strip().lower()
    expected_page_numbering = str(style.get("page_numbering", "")).strip().lower()
    expected_page_number_position = str(
        style.get("page_number_position", "")
    ).strip().lower()
    expected_front_matter_alignment = str(
        style.get("front_matter_alignment", "")
    ).strip().lower()
    expected_anonymization_mode = str(
        style.get("anonymization_mode", "")
    ).strip().lower()

    manuscripts = audit.get("manuscripts")
    if not isinstance(manuscripts, list) or not manuscripts:
        errors.append("manuscripts must be a non-empty list.")
        manuscripts = []

    roles: set[str] = set()
    clean_count = 0
    for index, manuscript in enumerate(manuscripts, start=1):
        prefix = f"manuscripts[{index}]"
        if not isinstance(manuscript, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        missing = MANUSCRIPT_FIELDS - manuscript.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
            continue

        role = str(manuscript.get("role", "")).strip().lower()
        if role not in {"clean", "tracked"}:
            errors.append(f"{prefix}.role must be clean or tracked.")
        elif role in roles:
            errors.append(f"Duplicate manuscript role: {role}")
        roles.add(role)
        if role == "clean":
            clean_count += 1

        output_path = resolve_output_path(manuscript.get("path"), audit_path)
        if output_path is None:
            errors.append(f"{prefix}.path must be non-empty.")
        elif not output_path.is_file():
            errors.append(f"{prefix}.path does not exist: {output_path}")
        else:
            recorded_sha = str(manuscript.get("sha256", "")).strip().lower()
            if not SHA256_RE.fullmatch(recorded_sha):
                errors.append(f"{prefix}.sha256 must be a 64-character SHA-256 value.")
            elif recorded_sha != sha256_file(output_path):
                errors.append(f"{prefix}.sha256 does not match {output_path}.")

        mechanical_status = str(
            manuscript.get("mechanical_status", "")
        ).strip().upper()
        visual_status = str(manuscript.get("visual_status", "")).strip().upper()
        for field, status in (
            ("mechanical_status", mechanical_status),
            ("visual_status", visual_status),
        ):
            if status not in AUDIT_STATUSES:
                errors.append(f"{prefix}.{field} must be one of {sorted(AUDIT_STATUSES)}.")

        actual_separation = str(
            manuscript.get("paragraph_separation", "")
        ).strip().lower()
        if actual_separation != expected_paragraph_separation:
            errors.append(
                f"{prefix}.paragraph_separation does not match style_contract."
            )
        actual_line_spacing = str(manuscript.get("line_spacing", "")).strip().lower()
        if actual_line_spacing != expected_line_spacing:
            errors.append(f"{prefix}.line_spacing does not match style_contract.")
        actual_line_numbering = str(
            manuscript.get("line_numbering", "")
        ).strip().lower()
        if actual_line_numbering != expected_line_numbering:
            errors.append(f"{prefix}.line_numbering does not match style_contract.")
        actual_page_numbering = str(
            manuscript.get("page_numbering", "")
        ).strip().lower()
        if actual_page_numbering != expected_page_numbering:
            errors.append(f"{prefix}.page_numbering does not match style_contract.")

        for field, expected in (
            ("page_number_position", expected_page_number_position),
            ("front_matter_alignment", expected_front_matter_alignment),
            ("anonymization_mode", expected_anonymization_mode),
        ):
            actual = str(manuscript.get(field, "")).strip().lower()
            if actual != expected:
                errors.append(f"{prefix}.{field} does not match style_contract.")

        front_matter_status = str(
            manuscript.get("front_matter_status", "")
        ).strip().upper()
        preservation_status = str(
            manuscript.get("content_preservation_status", "")
        ).strip().upper()
        format_release_status = str(
            manuscript.get("format_release_status", "")
        ).strip().upper()

        issue_count = manuscript.get("issue_count")
        if not isinstance(issue_count, int) or isinstance(issue_count, bool) or issue_count < 0:
            errors.append(f"{prefix}.issue_count must be a non-negative integer.")

        page_count = manuscript.get("rendered_page_count")
        inspected_pages = manuscript.get("inspected_pages")
        if not isinstance(page_count, int) or isinstance(page_count, bool) or page_count <= 0:
            errors.append(f"{prefix}.rendered_page_count must be a positive integer.")
            page_count = 0
        if not isinstance(inspected_pages, list) or not all(
            isinstance(page, int) and not isinstance(page, bool) and page > 0
            for page in inspected_pages
        ):
            errors.append(f"{prefix}.inspected_pages must be a positive-integer list.")
            inspected_pages = []
        expected_pages = list(range(1, page_count + 1))
        if sorted(set(inspected_pages)) != expected_pages:
            errors.append(
                f"{prefix}.inspected_pages must cover every rendered page exactly once."
            )

        if overall_status == "PASS":
            if mechanical_status != "PASS" or issue_count != 0:
                errors.append(
                    f"overall_status PASS requires {prefix} mechanical PASS with zero issues."
                )
            if visual_status != "PASS":
                errors.append(
                    f"overall_status PASS requires {prefix} visual_status PASS."
                )
            if front_matter_status != "PASS":
                errors.append(
                    f"overall_status PASS requires {prefix} front_matter_status PASS."
                )
            if preservation_status != "PASS":
                errors.append(
                    f"overall_status PASS requires {prefix} content preservation PASS."
                )
            if format_release_status != "FORMAT_RELEASE_PASS":
                errors.append(
                    f"overall_status PASS requires {prefix} FORMAT_RELEASE_PASS."
                )

    if clean_count != 1:
        errors.append("Exactly one clean manuscript entry is required.")

    plan_checks = plan.get("checks")
    if not isinstance(plan_checks, list):
        errors.append("Format plan checks must be a list.")
        plan_checks = []
    plan_check_by_id: dict[str, dict[str, object]] = {}
    for check in plan_checks:
        if isinstance(check, dict) and non_empty_string(check.get("id")):
            plan_check_by_id[str(check["id"]).strip()] = check

    audit_checks = audit.get("checks")
    if not isinstance(audit_checks, list):
        errors.append("Audit checks must be a list.")
        audit_checks = []
    seen_check_ids: set[str] = set()
    audit_status_by_id: dict[str, str] = {}
    for index, result in enumerate(audit_checks, start=1):
        prefix = f"checks[{index}]"
        if not isinstance(result, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        missing = CHECK_RESULT_FIELDS - result.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
            continue
        check_id = str(result.get("check_id", "")).strip()
        if not check_id:
            errors.append(f"{prefix}.check_id must be non-empty.")
        elif check_id in seen_check_ids:
            errors.append(f"Duplicate audit check_id: {check_id}")
        elif check_id not in plan_check_by_id:
            errors.append(f"Unknown audit check_id: {check_id}")
        seen_check_ids.add(check_id)

        status = str(result.get("status", "")).strip().upper()
        if status not in AUDIT_STATUSES:
            errors.append(f"{prefix}.status must be one of {sorted(AUDIT_STATUSES)}.")
        audit_status_by_id[check_id] = status
        for field in ("evidence", "output"):
            if not non_empty_string(result.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string.")

    missing_check_ids = sorted(set(plan_check_by_id) - seen_check_ids)
    if missing_check_ids:
        errors.append(
            "Audit is missing format-plan check IDs: " + ", ".join(missing_check_ids)
        )

    if overall_status == "PASS":
        for check_id, check in plan_check_by_id.items():
            plan_check_status = str(check.get("status", "")).strip().upper()
            mandatory = check.get("mandatory") is True
            audit_check_status = audit_status_by_id.get(check_id)
            if plan_check_status == "NOT_ASSESSABLE":
                errors.append(
                    f"overall_status PASS cannot close NOT_ASSESSABLE plan check {check_id}."
                )
            if mandatory and audit_check_status != "PASS":
                errors.append(
                    f"overall_status PASS requires mandatory check {check_id} to PASS."
                )
            if audit_check_status in {"FAIL", "NOT_ASSESSABLE"}:
                errors.append(
                    f"overall_status PASS conflicts with audit check {check_id}: "
                    f"{audit_check_status}."
                )

    return {
        "status": "PASS" if not errors else "FAIL",
        "target_journal": audit.get("target_journal"),
        "overall_status": overall_status,
        "manuscript_count": len(manuscripts),
        "plan_check_count": len(plan_check_by_id),
        "audit_check_count": len(audit_checks),
        "missing_check_ids": missing_check_ids,
        "errors": errors,
        "warnings": warnings,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Journal format audit validation: {report['status']}",
        f"Target journal: {report.get('target_journal') or 'UNKNOWN'}",
        f"Overall format status: {report.get('overall_status') or 'UNKNOWN'}",
        f"Manuscripts: {report.get('manuscript_count', 0)}",
        f"Plan checks: {report.get('plan_check_count', 0)}",
        f"Audit checks: {report.get('audit_check_count', 0)}",
    ]
    for warning in report.get("warnings", []):
        lines.append(f"WARNING: {warning}")
    for error in report.get("errors", []):
        lines.append(f"ERROR: {error}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
        audit = json.loads(args.audit.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read plan or audit: {exc}", file=sys.stderr)
        return 2

    report = validate(plan, audit, args.plan.resolve(), args.audit.resolve())
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
