#!/usr/bin/env python3
"""Audit manuscript-wide typography and semantic vertical rhythm."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from docx import Document
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    print(
        "python-docx is required. Use the bundled workspace Python runtime.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc

from docx_semantic_rules import (  # noqa: E402
    CREDIT_HEADING_RE,
    CREDIT_INLINE_RE,
    DECLARATION_HEADING_RE,
    DECLARATION_INLINE_RE,
    HEADING_STYLE_RE,
    KEYWORD_LABEL_RE,
    credit_role_labels,
)
from audit_docx_front_matter import paragraph_font_sizes_pt  # noqa: E402
from audit_docx_manuscript_style import (  # noqa: E402
    automatic_spacing_sources,
    effective_line_spacing,
    effective_spacing,
    iter_style_chain,
    line_spacing_matches,
    normalize_style_token,
    paragraph_is_structurally_empty,
    parse_line_spacing_spec,
)


ROLE_STYLE_RE = {
    "title": re.compile(r"(?:^|\b)(?:manuscript\s+)?title(?:\b|$)", re.I),
    "authors": re.compile(r"(?:^|\b)(?:manuscript\s+)?authors?(?:\b|$)", re.I),
    "affiliation": re.compile(r"(?:^|\b)affiliations?(?:\b|$)", re.I),
    "correspondence": re.compile(
        r"(?:^|\b)(?:correspondence|corresponding)(?:\b|$)", re.I
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit global manuscript line spacing, body-size typography, Keywords "
            "label emphasis, and semantic blank-line boundaries."
        )
    )
    parser.add_argument("document", type=Path)
    parser.add_argument("--expected-line-spacing", default="double")
    parser.add_argument("--expected-body-font-size", type=float, default=12.0)
    parser.add_argument("--body-style", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output-json", type=Path)
    return parser.parse_args()


def style_tokens(paragraph: Any) -> set[str]:
    if paragraph.style is None:
        return set()
    return {
        normalize_style_token(paragraph.style.name),
        normalize_style_token(paragraph.style.style_id),
    }


def classify_role(paragraph: Any, body_styles: set[str]) -> str | None:
    text = paragraph.text.strip()
    style_name = paragraph.style.name if paragraph.style is not None else ""
    if not text:
        return "blank"
    for role, pattern in ROLE_STYLE_RE.items():
        if any(pattern.search(token) for token in style_tokens(paragraph)):
            return role
    if KEYWORD_LABEL_RE.match(paragraph.text) or re.search(
        r"keyword", style_name, re.I
    ):
        return "keywords"
    if CREDIT_HEADING_RE.fullmatch(paragraph.text):
        return "credit-heading"
    if re.search(r"credit.*entry", style_name, re.I):
        return "credit-entry"
    if (
        HEADING_STYLE_RE.match(style_name)
        or style_name.lower().startswith("heading")
        or DECLARATION_HEADING_RE.fullmatch(paragraph.text)
    ):
        return "heading"
    if CREDIT_INLINE_RE.match(paragraph.text):
        return "credit-inline"
    if DECLARATION_INLINE_RE.match(paragraph.text):
        return "declaration-inline"
    if style_tokens(paragraph) & body_styles:
        return "body"
    return None


def effective_bold(run: Any, paragraph: Any) -> bool:
    if run.bold is not None:
        return bool(run.bold)
    if paragraph.style is not None:
        for style in iter_style_chain(paragraph.style):
            if style.font.bold is not None:
                return bool(style.font.bold)
    return False


def label_weight_issues(
    paragraph: Any,
    pattern: re.Pattern[str],
    *,
    prefix: str,
) -> list[dict[str, object]]:
    match = pattern.match(paragraph.text)
    if match is None:
        return [{"code": f"{prefix}_LABEL_MISSING"}]
    label_end = match.end(1)
    consumed = 0
    label_not_bold = False
    content_bold = False
    for run in paragraph.runs:
        start = consumed
        end = start + len(run.text)
        consumed = end
        bold = effective_bold(run, paragraph)
        if start < label_end and run.text[: max(0, label_end - start)].strip() and not bold:
            label_not_bold = True
        if end > label_end:
            content_start = max(0, label_end - start)
            if run.text[content_start:].strip() and bold:
                content_bold = True
    issues: list[dict[str, object]] = []
    if label_not_bold:
        issues.append({"code": f"{prefix}_LABEL_NOT_BOLD"})
    if content_bold:
        issues.append({"code": f"{prefix}_CONTENT_BOLD"})
    return issues


def adjacent_blank_count(document: Any, node: Any, direction: int) -> int:
    children = list(document.element.body)
    index = children.index(node) + direction
    count = 0
    while 0 <= index < len(children):
        candidate = children[index]
        if candidate.tag != qn("w:p"):
            break
        paragraph = Paragraph(candidate, document._body)
        if not paragraph_is_structurally_empty(paragraph):
            break
        count += 1
        index += direction
    return count


def previous_nonblank_role(
    document: Any,
    node: Any,
    roles: dict[Any, str | None],
) -> str | None:
    children = list(document.element.body)
    index = children.index(node) - 1
    while index >= 0:
        candidate = children[index]
        if candidate.tag != qn("w:p"):
            return None
        paragraph = Paragraph(candidate, document._body)
        if not paragraph_is_structurally_empty(paragraph):
            return roles.get(candidate)
        index -= 1
    return None


def next_nonblank_role(
    document: Any,
    node: Any,
    roles: dict[Any, str | None],
) -> str | None:
    children = list(document.element.body)
    index = children.index(node) + 1
    while index < len(children):
        candidate = children[index]
        if candidate.tag != qn("w:p"):
            return None
        paragraph = Paragraph(candidate, document._body)
        if not paragraph_is_structurally_empty(paragraph):
            return roles.get(candidate)
        index += 1
    return None


def audit(
    path: Path,
    *,
    expected_line_spacing: object = "double",
    expected_body_font_size: float = 12.0,
    body_style_names: set[str] | None = None,
) -> dict[str, object]:
    if expected_body_font_size <= 0:
        raise ValueError("expected body font size must be positive")
    spacing_spec = parse_line_spacing_spec(expected_line_spacing)
    body_styles = {
        normalize_style_token("Manuscript Body"),
        *(body_style_names or set()),
    }
    document = Document(str(path))
    body = document.element.body
    paragraphs = [
        Paragraph(node, document._body)
        for node in list(body)
        if node.tag == qn("w:p")
    ]
    roles: dict[Any, str | None] = {}
    credit_block_active = False
    for paragraph in paragraphs:
        role = classify_role(paragraph, body_styles)
        if role == "credit-heading":
            credit_block_active = True
        elif role == "blank":
            pass
        elif role == "body" and credit_block_active:
            role = "credit-entry"
        elif role == "credit-entry":
            pass
        elif role == "credit-inline":
            credit_block_active = False
        else:
            credit_block_active = False
        roles[paragraph._p] = role
    issues: list[dict[str, object]] = []
    inspected: list[dict[str, object]] = []

    same_size_roles = {
        "authors",
        "affiliation",
        "correspondence",
        "keywords",
        "heading",
        "body",
        "declaration-inline",
        "credit-heading",
        "credit-inline",
        "credit-entry",
    }
    for index, paragraph in enumerate(paragraphs, start=1):
        role = roles[paragraph._p]
        if role is None:
            continue
        record = {
            "paragraph": index,
            "role": role,
            "style": paragraph.style.name if paragraph.style is not None else "",
            "text_preview": paragraph.text.strip()[:100],
        }
        inspected.append(record)

        actual_spacing = effective_line_spacing(paragraph)
        if not line_spacing_matches(actual_spacing, spacing_spec):
            issues.append(
                {
                    **record,
                    "code": "GLOBAL_LINE_SPACING_MISMATCH",
                    "detail": {"expected": spacing_spec, "actual": actual_spacing},
                }
            )
        for field, label in (("space_before", "BEFORE"), ("space_after", "AFTER")):
            automatic = automatic_spacing_sources(paragraph, field)
            if automatic:
                issues.append(
                    {
                        **record,
                        "code": f"SEMANTIC_AUTOSPACING_{label}",
                        "detail": automatic,
                    }
                )
            points, source = effective_spacing(paragraph, field)
            if abs(points) > 0.01:
                issues.append(
                    {
                        **record,
                        "code": f"SEMANTIC_SPACE_{label}",
                        "detail": {"points": round(points, 3), "source": source},
                    }
                )

        if role in same_size_roles and paragraph.text.strip():
            sizes = paragraph_font_sizes_pt(paragraph)
            if not sizes or any(
                abs(size - expected_body_font_size) > 0.01 for size in sizes
            ):
                issues.append(
                    {
                        **record,
                        "code": "BODY_SIZE_ROLE_MISMATCH",
                        "detail": {
                            "expected_pt": expected_body_font_size,
                            "actual_pt": sizes,
                        },
                    }
                )

        if role == "keywords":
            for issue in label_weight_issues(
                paragraph, KEYWORD_LABEL_RE, prefix="KEYWORDS"
            ):
                issues.append({**record, **issue})
            before = adjacent_blank_count(document, paragraph._p, -1)
            after = adjacent_blank_count(document, paragraph._p, 1)
            if before != 0:
                issues.append(
                    {**record, "code": "KEYWORDS_BLANK_BEFORE", "detail": before}
                )
            if after != 1:
                issues.append(
                    {**record, "code": "KEYWORDS_BLANK_AFTER", "detail": after}
                )

        if role in {"declaration-inline", "credit-inline"}:
            pattern = (
                CREDIT_INLINE_RE
                if role == "credit-inline"
                else DECLARATION_INLINE_RE
            )
            prefix = "CREDIT" if role == "credit-inline" else "DECLARATION"
            for issue in label_weight_issues(
                paragraph, pattern, prefix=prefix
            ):
                issues.append({**record, **issue})
            if role == "credit-inline" and not credit_role_labels(paragraph.text):
                issues.append({**record, "code": "CREDIT_ROLE_VOCABULARY_MISSING"})

        if role in {"heading", "credit-heading"}:
            after = adjacent_blank_count(document, paragraph._p, 1)
            if after != 0:
                issues.append(
                    {**record, "code": "HEADING_BLANK_AFTER", "detail": after}
                )
            if re.fullmatch(r"abstract", paragraph.text.strip(), re.I):
                continue

        if role in {
            "heading",
            "credit-heading",
            "declaration-inline",
            "credit-inline",
        }:
            previous_role = previous_nonblank_role(document, paragraph._p, roles)
            expected_before = (
                0 if previous_role in {"heading", "credit-heading"} else 1
            )
            actual_before = adjacent_blank_count(document, paragraph._p, -1)
            if actual_before != expected_before:
                issues.append(
                    {
                        **record,
                        "code": "SEMANTIC_BLANK_BEFORE",
                        "detail": {
                            "expected": expected_before,
                            "actual": actual_before,
                            "previous_role": previous_role,
                        },
                    }
                )

        if role == "credit-heading":
            if next_nonblank_role(document, paragraph._p, roles) != "credit-entry":
                issues.append({**record, "code": "CREDIT_STATEMENT_MISSING"})

        if role == "credit-entry":
            if not credit_role_labels(paragraph.text):
                issues.append(
                    {**record, "code": "CREDIT_ENTRY_WITHOUT_STANDARD_ROLE"}
                )
            if next_nonblank_role(document, paragraph._p, roles) == "credit-entry":
                between = adjacent_blank_count(document, paragraph._p, 1)
                if between != 0:
                    issues.append(
                        {
                            **record,
                            "code": "CREDIT_ENTRY_BLANK_BETWEEN",
                            "detail": between,
                        }
                    )

    return {
        "status": "SEMANTIC_RHYTHM_PASS" if not issues else "FAIL",
        "document": str(path.resolve()),
        "expected_line_spacing": spacing_spec["label"],
        "expected_body_font_size_pt": expected_body_font_size,
        "issue_count": len(issues),
        "issues": issues,
        "inspected": inspected,
        "boundary": (
            "Checks manuscript typography and semantic vertical rhythm only; "
            "rendered-page and journal-source gates remain independent."
        ),
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"DOCX semantic-rhythm audit: {report['status']}",
        f"Document: {report['document']}",
        f"Issues: {report['issue_count']}",
    ]
    for issue in report["issues"]:
        lines.append(
            f"ERROR: paragraph {issue.get('paragraph', '?')}: "
            f"{issue['code']} - {issue.get('detail', '')}"
        )
    lines.append(f"BOUNDARY: {report['boundary']}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        report = audit(
            args.document,
            expected_line_spacing=args.expected_line_spacing,
            expected_body_font_size=args.expected_body_font_size,
            body_style_names={normalize_style_token(value) for value in args.body_style},
        )
    except (OSError, ValueError) as exc:
        print(f"Unable to audit DOCX semantic rhythm: {exc}", file=sys.stderr)
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
    return 0 if report["status"] == "SEMANTIC_RHYTHM_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
