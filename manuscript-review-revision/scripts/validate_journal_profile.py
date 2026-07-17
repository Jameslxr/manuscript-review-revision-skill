#!/usr/bin/env python3
"""Validate the structural completeness of a live journal-requirements profile."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


PROFILE_STATUSES = {"DRAFT", "PASS", "FAIL", "NOT_ASSESSABLE"}
REQUIREMENT_STATUSES = {
    "MET",
    "NOT_MET",
    "NOT_ASSESSABLE",
    "NOT_APPLICABLE",
    "PENDING",
}
STAGES = {"initial", "revision", "final", "proof", "transfer", "unknown"}
SOURCE_FIELDS = {"title", "url", "accessed_at", "official"}
REQUIREMENT_FIELDS = {
    "id",
    "category",
    "text",
    "source_url",
    "applies_to",
    "mandatory",
    "status",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a manuscript journal-profile JSON file."
    )
    parser.add_argument("profile", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def valid_date(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(profile: object) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(profile, dict):
        return {
            "status": "FAIL",
            "errors": ["Profile root must be a JSON object."],
            "warnings": [],
        }

    for field in (
        "target_journal",
        "article_type",
        "submission_stage",
        "accessed_at",
        "profile_status",
        "official_sources",
        "requirements",
    ):
        if field not in profile:
            errors.append(f"Missing top-level field: {field}")

    for field in ("target_journal", "article_type"):
        if field in profile and (
            not isinstance(profile[field], str) or not profile[field].strip()
        ):
            errors.append(f"{field} must be a non-empty string.")

    stage = str(profile.get("submission_stage", "")).strip().lower()
    if stage not in STAGES:
        errors.append(
            f"submission_stage must be one of {sorted(STAGES)}; got {stage!r}."
        )
    elif stage == "unknown":
        warnings.append("Submission stage is unknown; stage-specific rules remain bounded.")

    if not valid_date(profile.get("accessed_at")):
        errors.append("accessed_at must be an ISO-8601 date or datetime.")

    profile_status = str(profile.get("profile_status", "")).strip().upper()
    if profile_status not in PROFILE_STATUSES:
        errors.append(
            f"profile_status must be one of {sorted(PROFILE_STATUSES)}."
        )

    sources = profile.get("official_sources")
    source_urls: set[str] = set()
    if not isinstance(sources, list) or not sources:
        errors.append("official_sources must be a non-empty list.")
        sources = []

    for index, source in enumerate(sources, start=1):
        prefix = f"official_sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        missing = SOURCE_FIELDS - source.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
        if source.get("official") is not True:
            errors.append(f"{prefix}.official must be true.")
        if not valid_url(source.get("url")):
            errors.append(f"{prefix}.url must be an HTTP(S) URL.")
        else:
            source_urls.add(str(source["url"]).strip())
        if not valid_date(source.get("accessed_at")):
            errors.append(f"{prefix}.accessed_at must be ISO-8601.")
        if not isinstance(source.get("title"), str) or not source.get("title", "").strip():
            errors.append(f"{prefix}.title must be non-empty.")

    requirements = profile.get("requirements")
    if not isinstance(requirements, list) or not requirements:
        errors.append("requirements must be a non-empty list.")
        requirements = []

    ids: set[str] = set()
    mandatory_unresolved: list[str] = []
    for index, requirement in enumerate(requirements, start=1):
        prefix = f"requirements[{index}]"
        if not isinstance(requirement, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        missing = REQUIREMENT_FIELDS - requirement.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
            continue

        req_id = str(requirement["id"]).strip()
        if not req_id:
            errors.append(f"{prefix}.id must be non-empty.")
        elif req_id in ids:
            errors.append(f"Duplicate requirement id: {req_id}")
        ids.add(req_id)

        for field in ("category", "text", "applies_to"):
            value = requirement.get(field)
            if not isinstance(value, (str, list)) or not value:
                errors.append(f"{prefix}.{field} must be non-empty.")

        source_url = str(requirement.get("source_url", "")).strip()
        if not valid_url(source_url):
            errors.append(f"{prefix}.source_url must be an HTTP(S) URL.")
        elif source_url not in source_urls:
            errors.append(
                f"{prefix}.source_url is not listed in official_sources: {source_url}"
            )

        if not isinstance(requirement.get("mandatory"), bool):
            errors.append(f"{prefix}.mandatory must be boolean.")

        status = str(requirement.get("status", "")).strip().upper()
        if status not in REQUIREMENT_STATUSES:
            errors.append(
                f"{prefix}.status must be one of {sorted(REQUIREMENT_STATUSES)}."
            )
        if requirement.get("mandatory") is True and status in {
            "NOT_MET",
            "NOT_ASSESSABLE",
            "PENDING",
        }:
            mandatory_unresolved.append(req_id or prefix)

    if profile_status == "PASS" and mandatory_unresolved:
        errors.append(
            "profile_status is PASS but mandatory requirements are unresolved: "
            + ", ".join(mandatory_unresolved)
        )
    elif mandatory_unresolved:
        warnings.append(
            "Mandatory requirements unresolved: " + ", ".join(mandatory_unresolved)
        )

    return {
        "status": "PASS" if not errors else "FAIL",
        "target_journal": profile.get("target_journal"),
        "source_count": len(sources),
        "requirement_count": len(requirements),
        "mandatory_unresolved": mandatory_unresolved,
        "errors": errors,
        "warnings": warnings,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Journal profile validation: {report['status']}",
        f"Target journal: {report.get('target_journal') or 'UNKNOWN'}",
        f"Official sources: {report.get('source_count', 0)}",
        f"Requirements: {report.get('requirement_count', 0)}",
    ]
    for warning in report.get("warnings", []):
        lines.append(f"WARNING: {warning}")
    for error in report.get("errors", []):
        lines.append(f"ERROR: {error}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        profile = json.loads(args.profile.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read profile: {exc}", file=sys.stderr)
        return 2

    report = validate(profile)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
