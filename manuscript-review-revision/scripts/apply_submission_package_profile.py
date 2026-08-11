#!/usr/bin/env python3
"""Apply a natural, role-aware profile to submission-package DOCX files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt
    from docx.text.paragraph import Paragraph
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    print(
        "python-docx is required. Use the bundled workspace Python runtime.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc

from audit_docx_manuscript_style import (  # noqa: E402
    iter_style_chain,
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
            "Normalize a cover letter, response letter, or other editable "
            "submission-package DOCX without changing its text."
        )
    )
    parser.add_argument("document", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--artifact-type", choices=ARTIFACT_TYPES, required=True)
    parser.add_argument("--line-spacing", default="single")
    parser.add_argument("--font-name", default="Times New Roman")
    parser.add_argument("--font-size", type=float, default=12.0)
    parser.add_argument("--margin-inches", type=float, default=1.0)
    parser.add_argument("--salutation-paragraph", type=int)
    parser.add_argument("--closing-paragraph", type=int)
    return parser.parse_args()


def text_node_values(document: Any) -> list[str]:
    return [str(node.text or "") for node in document.element.body.xpath(".//w:t")]


def set_line_spacing(paragraph_format: Any, spec: dict[str, object]) -> None:
    kind = str(spec["kind"])
    value = float(spec["value"])
    if kind == "multiple":
        paragraph_format.line_spacing = value
        paragraph_format.line_spacing_rule = None
    elif kind == "exact":
        paragraph_format.line_spacing = Pt(value)
        paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
    elif kind == "at-least":
        paragraph_format.line_spacing = Pt(value)
        paragraph_format.line_spacing_rule = WD_LINE_SPACING.AT_LEAST
    else:  # pragma: no cover - guarded by parse_line_spacing_spec
        raise ValueError(f"Unsupported line-spacing kind: {kind}")


def remove_auto_spacing(paragraph_properties: Any) -> None:
    if paragraph_properties is None:
        return
    for spacing in paragraph_properties.xpath("./w:spacing"):
        spacing.attrib.pop(qn("w:beforeAutospacing"), None)
        spacing.attrib.pop(qn("w:afterAutospacing"), None)


def set_or_add(parent: Any, tag: str, attribute: str, value: str) -> Any:
    node = parent.find(qn(tag))
    if node is None:
        node = OxmlElement(tag)
        parent.append(node)
    node.set(qn(attribute), value)
    return node


def format_run_xml(run: Any, *, font_name: str, font_size: float) -> None:
    r_pr = run.find(qn("w:rPr"))
    if r_pr is None:
        r_pr = OxmlElement("w:rPr")
        run.insert(0, r_pr)
    r_fonts = r_pr.find(qn("w:rFonts"))
    if r_fonts is None:
        r_fonts = OxmlElement("w:rFonts")
        r_pr.insert(0, r_fonts)
    for attribute in ("ascii", "hAnsi", "eastAsia", "cs"):
        r_fonts.set(qn(f"w:{attribute}"), font_name)
    half_points = str(int(round(font_size * 2)))
    set_or_add(r_pr, "w:sz", "w:val", half_points)
    set_or_add(r_pr, "w:szCs", "w:val", half_points)
    color = set_or_add(r_pr, "w:color", "w:val", "000000")
    for attribute in ("themeColor", "themeTint", "themeShade"):
        color.attrib.pop(qn(f"w:{attribute}"), None)


def format_paragraph(
    paragraph: Any,
    *,
    line_spacing: dict[str, object],
    font_name: str,
    font_size: float,
) -> None:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(0)
    set_line_spacing(paragraph.paragraph_format, line_spacing)
    remove_auto_spacing(paragraph._p.get_or_add_pPr())
    if paragraph.style is not None:
        for style in iter_style_chain(paragraph.style):
            remove_auto_spacing(style.element.get_or_add_pPr())
    for run in paragraph._p.xpath(".//w:r[.//w:t]"):
        format_run_xml(run, font_name=font_name, font_size=font_size)


def format_blank(
    document: Any,
    node: Any,
    *,
    line_spacing: dict[str, object],
    font_name: str,
    font_size: float,
) -> None:
    paragraph = Paragraph(node, document._body)
    try:
        paragraph.style = document.styles["Normal"]
    except KeyError:
        pass
    format_paragraph(
        paragraph,
        line_spacing=line_spacing,
        font_name=font_name,
        font_size=font_size,
    )


def set_boundary_blank_count(
    document: Any,
    left: Any,
    right: Any,
    desired: int,
    *,
    line_spacing: dict[str, object],
    font_name: str,
    font_size: float,
) -> None:
    body = document.element.body
    blanks = blank_nodes_between(document, left, right)
    if blanks is None:
        return
    for duplicate in blanks[desired:]:
        body.remove(duplicate)
    blanks = blanks[:desired]
    while len(blanks) < desired:
        blank = OxmlElement("w:p")
        body.insert(body.index(right), blank)
        blanks.append(blank)
    for blank in blanks:
        format_blank(
            document,
            blank,
            line_spacing=line_spacing,
            font_name=font_name,
            font_size=font_size,
        )


def remove_edge_blanks(document: Any) -> None:
    body = document.element.body
    paragraphs = top_level_paragraphs(document)
    while paragraphs and paragraph_is_structurally_empty(paragraphs[0]):
        body.remove(paragraphs[0]._p)
        paragraphs = top_level_paragraphs(document)
    while paragraphs and paragraph_is_structurally_empty(paragraphs[-1]):
        body.remove(paragraphs[-1]._p)
        paragraphs = top_level_paragraphs(document)


def normalize_generic_boundaries(
    document: Any,
    *,
    line_spacing: dict[str, object],
    font_name: str,
    font_size: float,
) -> None:
    paragraphs = nonempty_top_level_paragraphs(document)
    for left, right in zip(paragraphs, paragraphs[1:]):
        desired = 0 if paragraph_is_list(left) and paragraph_is_list(right) else 1
        set_boundary_blank_count(
            document,
            left._p,
            right._p,
            desired,
            line_spacing=line_spacing,
            font_name=font_name,
            font_size=font_size,
        )


def normalize_cover_letter_boundaries(
    document: Any,
    roles: dict[str, Any],
    *,
    line_spacing: dict[str, object],
    font_name: str,
    font_size: float,
) -> None:
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
        elif index < closing_index:
            desired = 1
        elif left is closing:
            desired = 1
        else:
            desired = 0
        set_boundary_blank_count(
            document,
            left._p,
            right._p,
            desired,
            line_spacing=line_spacing,
            font_name=font_name,
            font_size=font_size,
        )


def apply_profile(
    document_path: Path,
    output_path: Path,
    *,
    artifact_type: str,
    line_spacing_token: str,
    font_name: str,
    font_size: float,
    margin_inches: float,
    salutation_paragraph: int | None,
    closing_paragraph: int | None,
) -> dict[str, object]:
    if document_path.resolve() == output_path.resolve():
        raise ValueError("--out must differ from input; preserve the source DOCX.")
    if font_size <= 0 or margin_inches <= 0:
        raise ValueError("Font size and margin must be positive.")
    document = Document(str(document_path))
    original_text = text_node_values(document)
    spacing = parse_line_spacing_spec(line_spacing_token)

    roles: dict[str, Any] | None = None
    if artifact_type == "cover-letter":
        roles = resolve_cover_letter_roles(
            document,
            salutation_paragraph=salutation_paragraph,
            closing_paragraph=closing_paragraph,
        )

    remove_edge_blanks(document)
    if artifact_type == "cover-letter":
        assert roles is not None
        normalize_cover_letter_boundaries(
            document,
            roles,
            line_spacing=spacing,
            font_name=font_name,
            font_size=font_size,
        )
    else:
        normalize_generic_boundaries(
            document,
            line_spacing=spacing,
            font_name=font_name,
            font_size=font_size,
        )

    for paragraph in iter_body_and_table_paragraphs(document):
        format_paragraph(
            paragraph,
            line_spacing=spacing,
            font_name=font_name,
            font_size=font_size,
        )
    for section in document.sections:
        section.top_margin = Inches(margin_inches)
        section.bottom_margin = Inches(margin_inches)
        section.left_margin = Inches(margin_inches)
        section.right_margin = Inches(margin_inches)
        vertical = section._sectPr.find(qn("w:vAlign"))
        if vertical is None:
            vertical = OxmlElement("w:vAlign")
            section._sectPr.append(vertical)
        vertical.set(qn("w:val"), "top")

    if text_node_values(document) != original_text:
        raise ValueError("Text-node preservation check failed; output was not written.")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(output_path))
    return {
        "output": str(output_path.resolve()),
        "artifact_type": artifact_type,
        "line_spacing": spacing["label"],
        "font_name": font_name,
        "font_size_pt": font_size,
        "margin_inches": margin_inches,
        "salutation_paragraph": None if roles is None else roles["salutation_paragraph"],
        "closing_paragraph": None if roles is None else roles["closing_paragraph"],
    }


def main() -> int:
    args = parse_args()
    try:
        result = apply_profile(
            args.document,
            args.out,
            artifact_type=args.artifact_type,
            line_spacing_token=args.line_spacing,
            font_name=args.font_name,
            font_size=args.font_size,
            margin_inches=args.margin_inches,
            salutation_paragraph=args.salutation_paragraph,
            closing_paragraph=args.closing_paragraph,
        )
    except (OSError, ValueError) as exc:
        print(f"Unable to apply submission-package profile: {exc}", file=sys.stderr)
        return 2
    print(f"Submission-package profile applied: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
