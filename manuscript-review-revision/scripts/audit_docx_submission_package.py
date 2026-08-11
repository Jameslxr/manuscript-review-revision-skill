#!/usr/bin/env python3
"""Fail-closed audit for cover letters and other submission-package DOCX files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    print(
        "python-docx is required. Use the bundled workspace Python runtime.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc

from audit_docx_front_matter import effective_alignment  # noqa: E402
from audit_docx_manuscript_style import (  # noqa: E402
    audit_document_numbering,
    automatic_spacing_sources,
    effective_line_spacing,
    effective_spacing,
    line_spacing_matches,
    paragraph_is_structurally_empty,
    parse_line_spacing_spec,
)
from docx_submission_package_rules import (  # noqa: E402
    ARTIFACT_TYPES,
    blank_nodes_between,
    iter_body_and_table_paragraphs,
    nonempty_top_level_paragraphs,
    paragraph_is_list,
    resolve_cover_letter_roles,
    top_level_paragraphs,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit whole-document typography, spacing, natural blank paragraphs, "
            "margins, and numbering in a submission-package DOCX."
        )
    )
    parser.add_argument("document", type=Path)
    parser.add_argument("--artifact-type", choices=ARTIFACT_TYPES, required=True)
    parser.add_argument("--expected-line-spacing", default="single")
    parser.add_argument("--expected-font-name", default="Times New Roman")
    parser.add_argument("--expected-font-size", type=float, default=12.0)
    parser.add_argument("--expected-margin-inches", type=float, default=1.0)
    parser.add_argument("--salutation-paragraph", type=int)
    parser.add_argument("--closing-paragraph", type=int)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output-json", type=Path)
    return parser.parse_args()


def paragraph_record(paragraph: Any, index: int, location: str) -> dict[str, object]:
    return {
        "paragraph": index,
        "location": location,
        "style": paragraph.style.name if paragraph.style is not None else "",
        "text_preview": paragraph.text.strip().replace("\n", " ")[:100],
    }


def run_format_issues(
    paragraph: Any,
    *,
    expected_font_name: str,
    expected_font_size: float,
) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    expected_half_points = int(round(expected_font_size * 2))
    for run_index, run in enumerate(paragraph._p.xpath(".//w:r[.//w:t]"), start=1):
        text = "".join(str(node.text or "") for node in run.xpath(".//w:t"))
        if not text.strip():
            continue
        r_pr = run.find(qn("w:rPr"))
        if r_pr is None:
            issues.append({"code": "RUN_FORMAT_NOT_EXPLICIT", "run": run_index})
            continue
        r_fonts = r_pr.find(qn("w:rFonts"))
        actual_fonts = (
            {}
            if r_fonts is None
            else {
                key: r_fonts.get(qn(f"w:{key}"))
                for key in ("ascii", "hAnsi", "eastAsia", "cs")
            }
        )
        if any(value != expected_font_name for value in actual_fonts.values()) or len(actual_fonts) != 4:
            issues.append(
                {
                    "code": "FONT_NAME_MISMATCH",
                    "run": run_index,
                    "expected": expected_font_name,
                    "actual": actual_fonts,
                }
            )
        size = r_pr.find(qn("w:sz"))
        size_cs = r_pr.find(qn("w:szCs"))
        actual_sizes = [
            None if node is None else node.get(qn("w:val"))
            for node in (size, size_cs)
        ]
        if any(str(value) != str(expected_half_points) for value in actual_sizes):
            issues.append(
                {
                    "code": "FONT_SIZE_MISMATCH",
                    "run": run_index,
                    "expected_half_points": expected_half_points,
                    "actual": actual_sizes,
                }
            )
        color = r_pr.find(qn("w:color"))
        color_value = None if color is None else color.get(qn("w:val"))
        if str(color_value or "").upper() not in {"000000", "AUTO"}:
            issues.append(
                {
                    "code": "FONT_COLOR_NOT_BLACK",
                    "run": run_index,
                    "actual": color_value,
                }
            )
    return issues


def boundary_issue(
    document: Any, left: Any, right: Any, desired: int, label: str
) -> dict[str, object] | None:
    blanks = blank_nodes_between(document, left._p, right._p)
    if blanks is None:
        return None
    if len(blanks) == desired:
        return None
    return {
        "code": "PACKAGE_BLANK_BOUNDARY_MISMATCH",
        "boundary": label,
        "left": left.text.strip()[:80],
        "right": right.text.strip()[:80],
        "expected": desired,
        "actual": len(blanks),
    }


def cover_boundary_issues(document: Any, roles: dict[str, Any]) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    paragraphs = [p for p in roles["paragraphs"] if p.text.strip()]
    salutation = roles["salutation"]
    closing = roles["closing"]
    salutation_index = paragraphs.index(salutation)
    closing_index = paragraphs.index(closing)
    for index, (left, right) in enumerate(zip(paragraphs, paragraphs[1:])):
        current = index + 1
        existing = blank_nodes_between(document, left._p, right._p)
        if existing is None:
            continue
        if current <= salutation_index:
            desired = 1 if right is salutation else min(1, len(existing))
            label = "preamble"
        elif index < closing_index:
            desired = 1
            label = "salutation-or-body"
        elif left is closing:
            desired = 1
            label = "closing-to-signature"
        else:
            desired = 0
            label = "compact-signature"
        issue = boundary_issue(document, left, right, desired, label)
        if issue:
            issues.append(issue)
    return issues


def generic_boundary_issues(document: Any) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    paragraphs = nonempty_top_level_paragraphs(document)
    for left, right in zip(paragraphs, paragraphs[1:]):
        desired = 0 if paragraph_is_list(left) and paragraph_is_list(right) else 1
        issue = boundary_issue(document, left, right, desired, "generic-block")
        if issue:
            issues.append(issue)
    return issues


def audit(
    path: Path,
    *,
    artifact_type: str,
    expected_line_spacing: str,
    expected_font_name: str,
    expected_font_size: float,
    expected_margin_inches: float,
    salutation_paragraph: int | None,
    closing_paragraph: int | None,
) -> dict[str, object]:
    if expected_font_size <= 0 or expected_margin_inches <= 0:
        raise ValueError("Expected font size and margin must be positive.")
    document = Document(str(path))
    spacing = parse_line_spacing_spec(expected_line_spacing)
    issues: list[dict[str, object]] = []
    inspected: list[dict[str, object]] = []

    top_nodes = {id(p._p) for p in top_level_paragraphs(document)}
    for index, paragraph in enumerate(iter_body_and_table_paragraphs(document), start=1):
        location = "top-level" if id(paragraph._p) in top_nodes else "table-cell"
        record = paragraph_record(paragraph, index, location)
        inspected.append(record)
        actual_line = effective_line_spacing(paragraph)
        if not line_spacing_matches(actual_line, spacing):
            issues.append(
                {
                    **record,
                    "code": "PACKAGE_LINE_SPACING_MISMATCH",
                    "expected": spacing,
                    "actual": actual_line,
                }
            )
        for field, label in (("space_before", "BEFORE"), ("space_after", "AFTER")):
            automatic = automatic_spacing_sources(paragraph, field)
            if automatic:
                issues.append(
                    {**record, "code": f"PACKAGE_AUTOSPACING_{label}", "actual": automatic}
                )
            points, source = effective_spacing(paragraph, field)
            if abs(points) > 0.01:
                issues.append(
                    {
                        **record,
                        "code": f"PACKAGE_SPACE_{label}",
                        "actual_points": round(points, 3),
                        "source": source,
                    }
                )
        if location == "top-level" and effective_alignment(paragraph) != WD_ALIGN_PARAGRAPH.LEFT:
            issues.append({**record, "code": "PACKAGE_ALIGNMENT_NOT_LEFT"})
        for issue in run_format_issues(
            paragraph,
            expected_font_name=expected_font_name,
            expected_font_size=expected_font_size,
        ):
            issues.append({**record, **issue})

    top_level = top_level_paragraphs(document)
    if top_level and paragraph_is_structurally_empty(top_level[0]):
        issues.append({"code": "LEADING_EMPTY_PARAGRAPH"})
    if top_level and paragraph_is_structurally_empty(top_level[-1]):
        issues.append({"code": "TRAILING_EMPTY_PARAGRAPH"})

    if artifact_type == "cover-letter":
        try:
            roles = resolve_cover_letter_roles(
                document,
                salutation_paragraph=salutation_paragraph,
                closing_paragraph=closing_paragraph,
            )
        except ValueError as exc:
            roles = None
            issues.append({"code": "COVER_LETTER_ROLE_RESOLUTION_FAILED", "detail": str(exc)})
        if roles is not None:
            issues.extend(cover_boundary_issues(document, roles))
    else:
        roles = None
        issues.extend(generic_boundary_issues(document))

    for section_index, section in enumerate(document.sections, start=1):
        for side in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
            value = getattr(section, side)
            actual = None if value is None else float(value.inches)
            if actual is None or abs(actual - expected_margin_inches) > 0.01:
                issues.append(
                    {
                        "section": section_index,
                        "code": "PACKAGE_MARGIN_MISMATCH",
                        "side": side,
                        "expected_inches": expected_margin_inches,
                        "actual_inches": actual,
                    }
                )
    numbering_issues, numbering = audit_document_numbering(document)
    issues.extend(numbering_issues)
    return {
        "status": "SUBMISSION_PACKAGE_PASS" if not issues else "FAIL",
        "document": str(path.resolve()),
        "artifact_type": artifact_type,
        "expected_line_spacing": spacing["label"],
        "expected_font_name": expected_font_name,
        "expected_font_size_pt": expected_font_size,
        "expected_margin_inches": expected_margin_inches,
        "issue_count": len(issues),
        "issues": issues,
        "inspected_paragraph_count": len(inspected),
        "numbering": numbering,
        "roles": None
        if roles is None
        else {
            "salutation_paragraph": roles["salutation_paragraph"],
            "closing_paragraph": roles["closing_paragraph"],
            "body_paragraph_count": len(roles["body"]),
            "signature_paragraph_count": len(roles["signature"]),
        },
        "boundary": (
            "Checks editable submission-package typography and semantic rhythm. "
            "Text preservation, current journal rules, and rendered-page review "
            "remain independent release gates."
        ),
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"DOCX submission-package audit: {report['status']}",
        f"Document: {report['document']}",
        f"Artifact type: {report['artifact_type']}",
        f"Issues: {report['issue_count']}",
    ]
    for issue in report["issues"]:
        lines.append(f"ERROR: {issue.get('code')} - {issue}")
    lines.append(f"BOUNDARY: {report['boundary']}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        report = audit(
            args.document,
            artifact_type=args.artifact_type,
            expected_line_spacing=args.expected_line_spacing,
            expected_font_name=args.expected_font_name,
            expected_font_size=args.expected_font_size,
            expected_margin_inches=args.expected_margin_inches,
            salutation_paragraph=args.salutation_paragraph,
            closing_paragraph=args.closing_paragraph,
        )
    except (OSError, ValueError) as exc:
        print(f"Unable to audit submission package: {exc}", file=sys.stderr)
        return 2
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(
            json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "SUBMISSION_PACKAGE_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
