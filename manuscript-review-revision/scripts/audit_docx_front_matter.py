#!/usr/bin/env python3
"""Audit a submission-manuscript title block and page-number placement."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    print(
        "python-docx is required. Use the bundled workspace Python runtime.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc

from audit_docx_manuscript_style import (  # noqa: E402
    PAGE_FIELD_RE,
    automatic_spacing_sources,
    effective_spacing,
    effective_line_spacing,
    field_instruction,
    inspect_font,
    iter_style_chain,
    line_spacing_matches,
    normalize_style_token,
    parse_line_spacing_spec,
)


ROLE_PATTERNS = {
    "title": re.compile(r"(?:^|\b)(?:manuscript\s+)?title(?:\b|$)", re.I),
    "authors": re.compile(r"(?:^|\b)(?:manuscript\s+)?authors?(?:\b|$)", re.I),
    "affiliation": re.compile(r"(?:^|\b)affiliations?(?:\b|$)", re.I),
    "correspondence": re.compile(
        r"(?:^|\b)(?:correspondence|corresponding)(?:\b|$)", re.I
    ),
}
ROLE_ORDER = {"title": 0, "authors": 1, "affiliation": 2, "correspondence": 3}
ROLE_SIZE_RANGES = {
    "title": (12.0, 16.0),
}
ALIGNMENT_VALUES = {
    "left": WD_ALIGN_PARAGRAPH.LEFT,
    "center": WD_ALIGN_PARAGRAPH.CENTER,
    "right": WD_ALIGN_PARAGRAPH.RIGHT,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit title, authors, affiliations, correspondence, front-matter "
            "alignment/spacing, layout containers, and PAGE-field placement."
        )
    )
    parser.add_argument("document", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument("--output-json", type=Path)
    parser.add_argument(
        "--mode", choices=("unblinded", "blinded"), default="unblinded"
    )
    parser.add_argument(
        "--front-matter-alignment",
        choices=tuple(ALIGNMENT_VALUES),
        default="left",
    )
    parser.add_argument(
        "--expected-page-number-position",
        choices=("upper-right", "lower-center", "any"),
        default="upper-right",
    )
    parser.add_argument("--allow-missing-correspondence", action="store_true")
    parser.add_argument("--expected-body-font-size", type=float, default=12.0)
    parser.add_argument("--expected-line-spacing", default="double")
    parser.add_argument(
        "--max-blank-paragraphs-before-abstract", type=int, default=1
    )
    for role in ROLE_ORDER:
        parser.add_argument(
            f"--{role}-style",
            action="append",
            default=[],
            help=f"Explicit paragraph style name or ID for {role}.",
        )
        parser.add_argument(
            f"--{role}-paragraph",
            action="append",
            type=int,
            default=[],
            help=(
                f"One-based top-level paragraph number for {role}. "
                "Repeat for multi-paragraph roles."
            ),
        )
    return parser.parse_args()


def paragraph_style_tokens(paragraph: Any) -> set[str]:
    if paragraph.style is None:
        return set()
    return {
        normalize_style_token(paragraph.style.name),
        normalize_style_token(paragraph.style.style_id),
    }


def build_explicit_style_map(args: argparse.Namespace) -> dict[str, set[str]]:
    return {
        role: {normalize_style_token(value) for value in getattr(args, f"{role}_style")}
        for role in ROLE_ORDER
    }


def build_explicit_paragraph_map(args: argparse.Namespace) -> dict[str, set[int]]:
    result = {
        role: set(getattr(args, f"{role}_paragraph")) for role in ROLE_ORDER
    }
    for role, values in result.items():
        if any(value < 1 for value in values):
            raise ValueError(f"{role} paragraph numbers must be positive")
    assignments: dict[int, list[str]] = {}
    for role, values in result.items():
        for value in values:
            assignments.setdefault(value, []).append(role)
    conflicts = {
        number: roles for number, roles in assignments.items() if len(roles) > 1
    }
    if conflicts:
        raise ValueError(f"Paragraph numbers assigned to multiple roles: {conflicts}")
    return result


def classify_role(
    paragraph: Any,
    explicit_styles: dict[str, set[str]],
    *,
    first_nonempty: bool = False,
    paragraph_number: int | None = None,
    explicit_paragraphs: dict[str, set[int]] | None = None,
) -> str | None:
    if paragraph_number is not None and explicit_paragraphs is not None:
        for role, paragraph_numbers in explicit_paragraphs.items():
            if paragraph_number in paragraph_numbers:
                return role
    tokens = paragraph_style_tokens(paragraph)
    for role, explicit in explicit_styles.items():
        if tokens & explicit:
            return role
    for role, pattern in ROLE_PATTERNS.items():
        if any(pattern.search(token) for token in tokens):
            return role
    if re.match(r"^\s*\*?\s*correspond", paragraph.text, re.I):
        return "correspondence"
    if first_nonempty:
        return "title"
    return None


def effective_alignment(paragraph: Any) -> Any:
    if paragraph.alignment is not None:
        return paragraph.alignment
    if paragraph.style is not None:
        for style in iter_style_chain(paragraph.style):
            alignment = style.paragraph_format.alignment
            if alignment is not None:
                return alignment
    return WD_ALIGN_PARAGRAPH.LEFT


def alignment_name(value: Any) -> str:
    for name, member in ALIGNMENT_VALUES.items():
        if value == member:
            return name
    return str(value)


def inherited_font_size_pt(paragraph: Any) -> float | None:
    if paragraph.style is None:
        return None
    for style in iter_style_chain(paragraph.style):
        if style.font.size is not None:
            return float(style.font.size.pt)
    return None


def paragraph_font_sizes_pt(paragraph: Any) -> list[float]:
    fallback = inherited_font_size_pt(paragraph)
    values: list[float] = []
    for run in paragraph.runs:
        if not run.text.strip():
            continue
        if run.font.size is not None:
            values.append(float(run.font.size.pt))
        elif fallback is not None:
            values.append(fallback)
    if not values and fallback is not None:
        values.append(fallback)
    return values


def paragraph_color_issues(paragraph: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if paragraph.style is not None:
        findings.extend(inspect_font(paragraph.style.font))
    for run in paragraph.runs:
        findings.extend(inspect_font(run.font))
    return findings


def paragraph_has_page_field(paragraph: Any) -> bool:
    for node in paragraph._p.xpath(".//w:instrText | .//w:fldSimple"):
        if PAGE_FIELD_RE.search(field_instruction(node)):
            return True
    return False


def page_field_paragraphs(story: Any) -> list[Any]:
    return [p for p in story.paragraphs if paragraph_has_page_field(p)]


def audit_page_number_position(
    document: Any, expected_position: str
) -> tuple[list[dict[str, object]], dict[str, object]]:
    issues: list[dict[str, object]] = []
    if expected_position == "any":
        return issues, {"expected": "any", "checked_story_count": 0}

    even_and_odd = (
        document.settings.element.find(qn("w:evenAndOddHeaders")) is not None
    )
    checked = 0
    for section_index, section in enumerate(document.sections, start=1):
        stories = [("default", section.header, section.footer)]
        if section.different_first_page_header_footer:
            stories.append(
                ("first", section.first_page_header, section.first_page_footer)
            )
        if even_and_odd:
            stories.append(("even", section.even_page_header, section.even_page_footer))

        for story_name, header, footer in stories:
            checked += 1
            if expected_position == "upper-right":
                target, other = header, footer
                expected_alignment = WD_ALIGN_PARAGRAPH.RIGHT
            else:
                target, other = footer, header
                expected_alignment = WD_ALIGN_PARAGRAPH.CENTER

            fields = page_field_paragraphs(target)
            if not fields:
                issues.append(
                    {
                        "section": section_index,
                        "story": story_name,
                        "code": "PAGE_NUMBER_POSITION",
                        "detail": f"Expected {expected_position} PAGE field.",
                    }
                )
            for paragraph in fields:
                if effective_alignment(paragraph) != expected_alignment:
                    issues.append(
                        {
                            "section": section_index,
                            "story": story_name,
                            "code": "PAGE_NUMBER_ALIGNMENT",
                            "detail": {
                                "expected": expected_position,
                                "actual_alignment": alignment_name(
                                    effective_alignment(paragraph)
                                ),
                            },
                        }
                    )
            if page_field_paragraphs(other):
                issues.append(
                    {
                        "section": section_index,
                        "story": story_name,
                        "code": "DUPLICATE_OR_MISPLACED_PAGE_NUMBER",
                        "detail": f"PAGE field also exists outside {expected_position}.",
                    }
                )
    return issues, {"expected": expected_position, "checked_story_count": checked}


def audit(
    path: Path,
    *,
    mode: str = "unblinded",
    front_matter_alignment: str = "left",
    expected_page_number_position: str = "upper-right",
    allow_missing_correspondence: bool = False,
    max_blank_paragraphs_before_abstract: int = 1,
    expected_body_font_size: float = 12.0,
    expected_line_spacing: object = "double",
    explicit_styles: dict[str, set[str]] | None = None,
    explicit_paragraphs: dict[str, set[int]] | None = None,
) -> dict[str, object]:
    if max_blank_paragraphs_before_abstract < 0:
        raise ValueError("max blank paragraphs must be non-negative")
    if expected_body_font_size <= 0:
        raise ValueError("expected body font size must be positive")
    line_spacing_spec = parse_line_spacing_spec(expected_line_spacing)
    document = Document(str(path))
    explicit_styles = explicit_styles or {role: set() for role in ROLE_ORDER}
    explicit_paragraphs = explicit_paragraphs or {
        role: set() for role in ROLE_ORDER
    }
    issues: list[dict[str, object]] = []
    records: list[dict[str, object]] = []

    body = document.element.body
    children = list(body)
    abstract_child_index: int | None = None
    first_nonempty_seen = False
    blank_indices: list[int] = []
    blank_paragraphs: dict[int, Any] = {}
    paragraph_number = 0

    for child_index, child in enumerate(children):
        if child.tag == qn("w:sectPr"):
            continue
        if child.tag == qn("w:tbl"):
            if child.xpath(".//w:t[text()[normalize-space(.)]]"):
                issues.append(
                    {
                        "code": "FRONT_MATTER_TABLE_LAYOUT",
                        "detail": "A table appears before the Abstract heading.",
                    }
                )
            continue
        if child.tag != qn("w:p"):
            continue

        paragraph_number += 1
        paragraph = Paragraph(child, document._body)
        text = paragraph.text.strip()
        if re.fullmatch(r"abstract", text, re.I):
            abstract_child_index = child_index
            break
        if child.xpath(".//w:txbxContent"):
            issues.append(
                {
                    "code": "FRONT_MATTER_TEXTBOX_LAYOUT",
                    "detail": "A text box appears before the Abstract heading.",
                }
            )
        if not text:
            blank_indices.append(child_index)
            blank_paragraphs[child_index] = paragraph
            continue

        role = classify_role(
            paragraph,
            explicit_styles,
            first_nonempty=not first_nonempty_seen,
            paragraph_number=paragraph_number,
            explicit_paragraphs=explicit_paragraphs,
        )
        first_nonempty_seen = True
        if role is None:
            issues.append(
                {
                    "paragraph": child_index + 1,
                    "code": "UNCLASSIFIED_FRONT_MATTER_PARAGRAPH",
                    "detail": text[:120],
                }
            )
            continue

        record = {
            "paragraph": paragraph_number,
            "child_index": child_index,
            "role": role,
            "style": paragraph.style.name if paragraph.style is not None else "",
            "text_preview": text[:120],
            "alignment": alignment_name(effective_alignment(paragraph)),
            "font_sizes_pt": paragraph_font_sizes_pt(paragraph),
        }
        records.append(record)

        expected_alignment = ALIGNMENT_VALUES[front_matter_alignment]
        if effective_alignment(paragraph) != expected_alignment:
            issues.append(
                {
                    **record,
                    "code": f"{role.upper()}_ALIGNMENT",
                    "detail": {
                        "expected": front_matter_alignment,
                        "actual": record["alignment"],
                    },
                }
            )

        sizes = record["font_sizes_pt"]
        if not sizes:
            issues.append(
                {
                    **record,
                    "code": f"{role.upper()}_FONT_SIZE_UNRESOLVED",
                    "detail": "No explicit or style-resolved point size.",
                }
            )
        else:
            low, high = ROLE_SIZE_RANGES.get(
                role,
                (expected_body_font_size, expected_body_font_size),
            )
            if min(sizes) < low or max(sizes) > high:
                issues.append(
                    {
                        **record,
                        "code": f"{role.upper()}_FONT_SIZE",
                        "detail": {"allowed_pt": [low, high], "actual_pt": sizes},
                    }
                )

        actual_line_spacing = effective_line_spacing(paragraph)
        if not line_spacing_matches(actual_line_spacing, line_spacing_spec):
            issues.append(
                {
                    **record,
                    "code": f"{role.upper()}_LINE_SPACING",
                    "detail": {
                        "expected": line_spacing_spec,
                        "actual": actual_line_spacing,
                    },
                }
            )

        colors = paragraph_color_issues(paragraph)
        if colors:
            issues.append(
                {
                    **record,
                    "code": f"{role.upper()}_NON_BLACK",
                    "detail": colors,
                }
            )

    if abstract_child_index is None:
        issues.append(
            {
                "code": "ABSTRACT_HEADING_MISSING",
                "detail": "No top-level Abstract heading was located.",
            }
        )

    role_counts = {
        role: sum(record["role"] == role for record in records) for role in ROLE_ORDER
    }
    if role_counts["title"] != 1:
        issues.append(
            {
                "code": "TITLE_COUNT",
                "detail": {"expected": 1, "actual": role_counts["title"]},
            }
        )

    identity_roles = ("authors", "affiliation", "correspondence")
    if mode == "blinded":
        for role in identity_roles:
            if role_counts[role]:
                issues.append(
                    {
                        "code": "ANONYMIZATION_LEAK",
                        "detail": f"Blinded manuscript contains {role}.",
                    }
                )
    else:
        for role in ("authors", "affiliation"):
            if role_counts[role] < 1:
                issues.append(
                    {"code": f"{role.upper()}_MISSING", "detail": "Required role missing."}
                )
        if not allow_missing_correspondence and role_counts["correspondence"] < 1:
            issues.append(
                {
                    "code": "CORRESPONDENCE_MISSING",
                    "detail": "Required role missing.",
                }
            )

    observed_order = [ROLE_ORDER[record["role"]] for record in records]
    if observed_order != sorted(observed_order):
        issues.append(
            {
                "code": "FRONT_MATTER_ORDER",
                "detail": [record["role"] for record in records],
            }
        )

    role_indices = [int(record["child_index"]) for record in records]
    if role_indices:
        first_role, last_role = min(role_indices), max(role_indices)
        internal_blanks = [i for i in blank_indices if first_role < i < last_role]
        if internal_blanks:
            issues.append(
                {
                    "code": "FRONT_MATTER_INTERNAL_BLANKS",
                    "detail": {"count": len(internal_blanks)},
                }
            )
        if abstract_child_index is not None:
            trailing_blanks = [
                i for i in blank_indices if last_role < i < abstract_child_index
            ]
            if len(trailing_blanks) > max_blank_paragraphs_before_abstract:
                issues.append(
                    {
                        "code": "EXCESSIVE_FRONT_MATTER_BLANKS",
                        "detail": {
                            "allowed": max_blank_paragraphs_before_abstract,
                            "actual": len(trailing_blanks),
                        },
                    }
                )

    for blank_index in blank_indices:
        paragraph = blank_paragraphs[blank_index]
        for field, label in (("space_before", "BEFORE"), ("space_after", "AFTER")):
            automatic_sources = automatic_spacing_sources(paragraph, field)
            if automatic_sources:
                issues.append(
                    {
                        "paragraph": blank_index + 1,
                        "code": f"FRONT_MATTER_BLANK_AUTOSPACING_{label}",
                        "detail": automatic_sources,
                    }
                )
            points, source = effective_spacing(paragraph, field)
            if abs(points) > 0.01:
                issues.append(
                    {
                        "paragraph": blank_index + 1,
                        "code": f"FRONT_MATTER_BLANK_SPACE_{label}",
                        "detail": {"points": round(points, 3), "source": source},
                    }
                )
        actual_line_spacing = effective_line_spacing(paragraph)
        if not line_spacing_matches(actual_line_spacing, line_spacing_spec):
            issues.append(
                {
                    "paragraph": blank_index + 1,
                    "code": "FRONT_MATTER_BLANK_LINE_SPACING",
                    "detail": {
                        "expected": line_spacing_spec,
                        "actual": actual_line_spacing,
                    },
                }
            )

    for section_index, section in enumerate(document.sections, start=1):
        vertical_nodes = section._sectPr.xpath("./w:vAlign")
        if vertical_nodes:
            value = str(vertical_nodes[0].get(qn("w:val")) or "top").lower()
            if value not in {"top", ""}:
                issues.append(
                    {
                        "section": section_index,
                        "code": "PAGE_VERTICAL_ALIGNMENT_NOT_TOP",
                        "detail": value,
                    }
                )

    page_issues, page_summary = audit_page_number_position(
        document, expected_page_number_position
    )
    issues.extend(page_issues)

    return {
        "status": "FRONT_MATTER_PASS" if not issues else "FAIL",
        "document": str(path.resolve()),
        "profile": {
            "mode": mode,
            "front_matter_alignment": front_matter_alignment,
            "expected_page_number_position": expected_page_number_position,
            "max_blank_paragraphs_before_abstract": max_blank_paragraphs_before_abstract,
            "expected_body_font_size": expected_body_font_size,
            "expected_line_spacing": line_spacing_spec["label"],
        },
        "role_counts": role_counts,
        "page_number_position": page_summary,
        "issue_count": len(issues),
        "issues": issues,
        "inspected": records,
        "boundary": (
            "Journal-neutral front-matter and page-number placement audit only. "
            "Exact journal rules and rendered page inspection remain separate gates."
        ),
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"DOCX front-matter audit: {report['status']}",
        f"Document: {report['document']}",
        f"Roles: {report['role_counts']}",
        f"Issues: {report['issue_count']}",
    ]
    for issue in report["issues"]:
        location = (
            f"paragraph {issue['paragraph']}"
            if "paragraph" in issue
            else f"section {issue['section']}"
            if "section" in issue
            else "document"
        )
        lines.append(f"ERROR: {location}: {issue['code']} - {issue['detail']}")
    lines.append(f"BOUNDARY: {report['boundary']}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        explicit_styles = build_explicit_style_map(args)
        explicit_paragraphs = build_explicit_paragraph_map(args)
        report = audit(
            args.document,
            mode=args.mode,
            front_matter_alignment=args.front_matter_alignment,
            expected_page_number_position=args.expected_page_number_position,
            allow_missing_correspondence=args.allow_missing_correspondence,
            max_blank_paragraphs_before_abstract=args.max_blank_paragraphs_before_abstract,
            expected_body_font_size=args.expected_body_font_size,
            expected_line_spacing=args.expected_line_spacing,
            explicit_styles=explicit_styles,
            explicit_paragraphs=explicit_paragraphs,
        )
    except (OSError, ValueError) as exc:
        print(f"Unable to audit DOCX front matter: {exc}", file=sys.stderr)
        return 2

    if args.output_json:
        args.output_json.write_text(
            json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "FRONT_MATTER_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
