#!/usr/bin/env python3
"""Validate an executable, source-linked target-journal formatting plan."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


PLAN_STATUSES = {"DRAFT", "PASS", "FAIL", "NOT_ASSESSABLE"}
CHECK_STATUSES = {"RESOLVED", "NOT_ASSESSABLE", "NOT_APPLICABLE"}
STAGES = {"initial", "revision", "final", "proof", "transfer", "unknown"}
SOURCE_FIELDS = {"title", "url", "accessed_at", "official"}
CHECK_FIELDS = {
    "id",
    "category",
    "requirement",
    "implementation",
    "verification",
    "deliverable",
    "basis",
    "source_url",
    "mandatory",
    "status",
}
STYLE_FIELDS = {
    "paragraph_separation",
    "paragraph_separation_basis",
    "line_spacing",
    "line_spacing_basis",
    "line_numbering",
    "line_numbering_basis",
    "page_numbering",
    "page_numbering_basis",
    "page_number_position",
    "page_number_position_basis",
    "front_matter_alignment",
    "front_matter_alignment_basis",
    "anonymization_mode",
    "body_font_family",
    "body_font_size_pt",
    "font_basis",
    "text_color_hex",
    "space_before_pt",
    "space_after_pt",
    "body_styles",
    "page_size",
    "margins",
    "columns",
    "source_urls",
}
BASIS_VALUES = {
    "EDITOR_INSTRUCTION",
    "OFFICIAL_TEMPLATE",
    "OFFICIAL_GUIDE",
    "CONSERVATIVE_FALLBACK",
    "USER_GLOBAL_INVARIANT",
    "NOT_APPLICABLE",
}
OFFICIAL_BASIS_VALUES = {
    "EDITOR_INSTRUCTION",
    "OFFICIAL_TEMPLATE",
    "OFFICIAL_GUIDE",
}
REQUIRED_CHECK_CATEGORIES = {
    "article-type",
    "file-format",
    "title-page",
    "anonymization",
    "abstract",
    "main-text",
    "section-order",
    "references",
    "figures",
    "tables",
    "supplements",
    "line-numbering",
    "page-numbering",
    "statistics",
    "reporting-guidelines",
    "ethics-registration",
    "data-code",
    "declarations",
    "cover-letter",
    "submission-files",
}
LINE_SPACING_RE = re.compile(
    r"^(?:single|1\.15|1\.5|double|[0-9]+(?:\.[0-9]+)?|"
    r"exact:[0-9]+(?:\.[0-9]+)?pt|at-least:[0-9]+(?:\.[0-9]+)?pt)$",
    flags=re.IGNORECASE,
)
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
HEX_COLOR_RE = re.compile(r"^[0-9a-fA-F]{6}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a target-journal formatting-plan JSON file."
    )
    parser.add_argument("plan", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument(
        "--require-pass",
        action="store_true",
        help="Fail unless plan_status is PASS and all required rules are resolved.",
    )
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


def normalized_token(value: object) -> str:
    return str(value).strip().lower().replace("_", "-").replace(" ", "-")


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(plan: object, require_pass: bool = False) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(plan, dict):
        return {
            "status": "FAIL",
            "errors": ["Plan root must be a JSON object."],
            "warnings": [],
        }

    for field in (
        "schema_version",
        "target_journal",
        "article_type",
        "submission_stage",
        "accessed_at",
        "plan_status",
        "journal_profile_sha256",
        "official_sources",
        "style_contract",
        "checks",
    ):
        if field not in plan:
            errors.append(f"Missing top-level field: {field}")

    if str(plan.get("schema_version", "")).strip() != "1.0":
        errors.append("schema_version must be '1.0'.")

    for field in ("target_journal", "article_type"):
        if not non_empty_string(plan.get(field)):
            errors.append(f"{field} must be a non-empty string.")

    stage = normalized_token(plan.get("submission_stage", ""))
    if stage not in STAGES:
        errors.append(f"submission_stage must be one of {sorted(STAGES)}.")
    elif stage == "unknown":
        warnings.append("Submission stage is unknown; stage-specific formatting is bounded.")

    if not valid_date(plan.get("accessed_at")):
        errors.append("accessed_at must be an ISO-8601 date or datetime.")

    plan_status = str(plan.get("plan_status", "")).strip().upper()
    if plan_status not in PLAN_STATUSES:
        errors.append(f"plan_status must be one of {sorted(PLAN_STATUSES)}.")
    elif require_pass and plan_status != "PASS":
        errors.append("--require-pass requires plan_status PASS.")

    if not SHA256_RE.fullmatch(str(plan.get("journal_profile_sha256", "")).strip()):
        errors.append("journal_profile_sha256 must be a 64-character SHA-256 value.")

    sources = plan.get("official_sources")
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
        url = str(source.get("url", "")).strip()
        if not valid_url(url):
            errors.append(f"{prefix}.url must be an HTTP(S) URL.")
        else:
            source_urls.add(url)
        if not valid_date(source.get("accessed_at")):
            errors.append(f"{prefix}.accessed_at must be ISO-8601.")
        if not non_empty_string(source.get("title")):
            errors.append(f"{prefix}.title must be non-empty.")

    style = plan.get("style_contract")
    if not isinstance(style, dict):
        errors.append("style_contract must be an object.")
        style = {}
    missing_style = STYLE_FIELDS - style.keys()
    if missing_style:
        errors.append(f"style_contract missing fields: {sorted(missing_style)}")

    paragraph_separation = normalized_token(style.get("paragraph_separation", ""))
    if paragraph_separation != "literal-blank":
        errors.append(
            "style_contract.paragraph_separation must be literal-blank; every "
            "modified DOCX uses the global empty-paragraph invariant."
        )

    style_basis_fields = (
        "paragraph_separation_basis",
        "line_spacing_basis",
        "line_numbering_basis",
        "page_numbering_basis",
        "page_number_position_basis",
        "front_matter_alignment_basis",
        "font_basis",
    )
    style_basis_values: dict[str, str] = {}
    for field in style_basis_fields:
        basis = str(style.get(field, "")).strip().upper()
        style_basis_values[field] = basis
        if basis not in BASIS_VALUES - {"NOT_APPLICABLE"}:
            errors.append(f"style_contract.{field} has invalid basis {basis!r}.")

    style_source_urls = style.get("source_urls")
    if not isinstance(style_source_urls, list):
        errors.append("style_contract.source_urls must be a list.")
        style_source_urls = []
    for source_url in style_source_urls:
        if not valid_url(source_url):
            errors.append(f"Invalid style_contract source URL: {source_url!r}")
        elif str(source_url).strip() not in source_urls:
            errors.append(
                "style_contract source URL is not listed in official_sources: "
                f"{source_url}"
            )

    if any(value in OFFICIAL_BASIS_VALUES for value in style_basis_values.values()):
        if not style_source_urls:
            errors.append(
                "Official style-contract decisions require at least one source_urls entry."
            )

    if style_basis_values.get("paragraph_separation_basis") != "USER_GLOBAL_INVARIANT":
        errors.append(
            "style_contract.paragraph_separation_basis must be "
            "USER_GLOBAL_INVARIANT."
        )

    for field in ("line_numbering_basis", "page_numbering_basis"):
        if style_basis_values.get(field) != "USER_GLOBAL_INVARIANT":
            errors.append(
                f"style_contract.{field} must be USER_GLOBAL_INVARIANT."
            )

    for field in ("line_numbering", "page_numbering"):
        if normalized_token(style.get(field, "")) != "continuous":
            errors.append(
                f"style_contract.{field} must be continuous for every modified DOCX."
            )

    if normalized_token(style.get("page_number_position", "")) not in {
        "upper-right",
        "lower-center",
    }:
        errors.append(
            "style_contract.page_number_position must be upper-right or lower-center."
        )

    if normalized_token(style.get("front_matter_alignment", "")) not in {
        "left",
        "center",
        "right",
    }:
        errors.append(
            "style_contract.front_matter_alignment must be left, center, or right."
        )

    if normalized_token(style.get("anonymization_mode", "")) not in {
        "blinded",
        "unblinded",
    }:
        errors.append(
            "style_contract.anonymization_mode must be blinded or unblinded."
        )

    line_spacing = str(style.get("line_spacing", "")).strip()
    if not LINE_SPACING_RE.fullmatch(line_spacing):
        errors.append(
            "style_contract.line_spacing must be an explicit multiple or point rule."
        )

    if not non_empty_string(style.get("body_font_family")):
        errors.append("style_contract.body_font_family must be non-empty.")
    body_font_size = style.get("body_font_size_pt")
    if not isinstance(body_font_size, (int, float)) or body_font_size <= 0:
        errors.append("style_contract.body_font_size_pt must be a positive number.")
    if not HEX_COLOR_RE.fullmatch(str(style.get("text_color_hex", "")).strip()):
        errors.append("style_contract.text_color_hex must contain six hexadecimal digits.")

    for field in ("space_before_pt", "space_after_pt"):
        value = style.get(field)
        if not isinstance(value, (int, float)) or value < 0:
            errors.append(f"style_contract.{field} must be a non-negative number.")
        elif abs(float(value)) > 0.01:
            errors.append(
                f"literal-blank mode requires style_contract.{field}=0."
            )

    body_styles = style.get("body_styles")
    if not isinstance(body_styles, list) or not body_styles or not all(
        non_empty_string(value) for value in body_styles
    ):
        errors.append("style_contract.body_styles must be a non-empty string list.")
    for field in ("page_size", "margins"):
        if not non_empty_string(style.get(field)):
            errors.append(f"style_contract.{field} must be a resolved non-empty string.")
    columns = style.get("columns")
    if not isinstance(columns, int) or isinstance(columns, bool) or columns not in {1, 2}:
        errors.append("style_contract.columns must be integer 1 or 2.")

    checks = plan.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append("checks must be a non-empty list.")
        checks = []

    check_ids: set[str] = set()
    covered_categories: set[str] = set()
    unresolved_mandatory: list[str] = []
    unresolved_categories: set[str] = set()
    checks_by_category: dict[str, list[dict[str, object]]] = {}

    for index, check in enumerate(checks, start=1):
        prefix = f"checks[{index}]"
        if not isinstance(check, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        missing = CHECK_FIELDS - check.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")
            continue

        check_id = str(check.get("id", "")).strip()
        if not check_id:
            errors.append(f"{prefix}.id must be non-empty.")
        elif check_id in check_ids:
            errors.append(f"Duplicate check id: {check_id}")
        check_ids.add(check_id)

        category = normalized_token(check.get("category", ""))
        if not category:
            errors.append(f"{prefix}.category must be non-empty.")
        else:
            covered_categories.add(category)
            checks_by_category.setdefault(category, []).append(check)

        for field in ("requirement", "implementation", "verification", "deliverable"):
            if not non_empty_string(check.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string.")

        basis = str(check.get("basis", "")).strip().upper()
        if basis not in BASIS_VALUES:
            errors.append(f"{prefix}.basis must be one of {sorted(BASIS_VALUES)}.")

        source_url_value = check.get("source_url")
        source_url = str(source_url_value or "").strip()
        if basis in OFFICIAL_BASIS_VALUES:
            if not valid_url(source_url):
                errors.append(f"{prefix}.source_url is required for official rules.")
            elif source_url not in source_urls:
                errors.append(
                    f"{prefix}.source_url is not listed in official_sources: {source_url}"
                )
        elif source_url:
            if not valid_url(source_url):
                errors.append(f"{prefix}.source_url must be an HTTP(S) URL or null.")
            elif source_url not in source_urls:
                errors.append(
                    f"{prefix}.source_url is not listed in official_sources: {source_url}"
                )

        mandatory = check.get("mandatory")
        if not isinstance(mandatory, bool):
            errors.append(f"{prefix}.mandatory must be boolean.")

        status = str(check.get("status", "")).strip().upper()
        if status not in CHECK_STATUSES:
            errors.append(f"{prefix}.status must be one of {sorted(CHECK_STATUSES)}.")
        if basis == "NOT_APPLICABLE" and status != "NOT_APPLICABLE":
            errors.append(f"{prefix} uses NOT_APPLICABLE basis but status is {status!r}.")
        if status == "NOT_APPLICABLE" and basis != "NOT_APPLICABLE":
            errors.append(f"{prefix} has NOT_APPLICABLE status without matching basis.")
        if mandatory is True and status != "RESOLVED":
            unresolved_mandatory.append(check_id or prefix)
        if category in REQUIRED_CHECK_CATEGORIES and status == "NOT_ASSESSABLE":
            unresolved_categories.add(category)

    missing_categories = sorted(REQUIRED_CHECK_CATEGORIES - covered_categories)
    if missing_categories:
        errors.append(
            "Missing required journal-format check categories: "
            + ", ".join(missing_categories)
        )

    for category in ("line-numbering", "page-numbering"):
        invariant_checks = checks_by_category.get(category, [])
        if not invariant_checks:
            continue
        if not any(
            str(check.get("basis", "")).strip().upper()
            == "USER_GLOBAL_INVARIANT"
            and check.get("mandatory") is True
            and str(check.get("status", "")).strip().upper() == "RESOLVED"
            for check in invariant_checks
        ):
            errors.append(
                f"{category} requires a mandatory RESOLVED "
                "USER_GLOBAL_INVARIANT check."
            )

    if plan_status == "PASS" and unresolved_mandatory:
        errors.append(
            "plan_status is PASS but mandatory checks are unresolved: "
            + ", ".join(unresolved_mandatory)
        )
    elif unresolved_mandatory:
        warnings.append(
            "Mandatory checks unresolved: " + ", ".join(unresolved_mandatory)
        )

    if plan_status == "PASS" and unresolved_categories:
        errors.append(
            "plan_status is PASS but required categories are NOT_ASSESSABLE: "
            + ", ".join(sorted(unresolved_categories))
        )

    return {
        "status": "PASS" if not errors else "FAIL",
        "target_journal": plan.get("target_journal"),
        "plan_status": plan_status,
        "official_source_count": len(sources),
        "check_count": len(checks),
        "covered_required_category_count": len(
            REQUIRED_CHECK_CATEGORIES & covered_categories
        ),
        "required_category_count": len(REQUIRED_CHECK_CATEGORIES),
        "missing_categories": missing_categories,
        "unresolved_mandatory": unresolved_mandatory,
        "errors": errors,
        "warnings": warnings,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Journal format plan validation: {report['status']}",
        f"Target journal: {report.get('target_journal') or 'UNKNOWN'}",
        f"Plan status: {report.get('plan_status') or 'UNKNOWN'}",
        f"Official sources: {report.get('official_source_count', 0)}",
        f"Checks: {report.get('check_count', 0)}",
        "Required categories covered: "
        f"{report.get('covered_required_category_count', 0)}/"
        f"{report.get('required_category_count', 0)}",
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
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read format plan: {exc}", file=sys.stderr)
        return 2

    report = validate(plan, require_pass=args.require_pass)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
