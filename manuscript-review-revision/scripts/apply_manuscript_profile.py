#!/usr/bin/env python3
"""Apply a restrained, journal-neutral manuscript DOCX profile."""

from __future__ import annotations

import argparse
import re
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor
    from docx.text.paragraph import Paragraph
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    print(
        "python-docx is required. Use the bundled workspace Python runtime.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc

from audit_docx_front_matter import (  # noqa: E402
    ALIGNMENT_VALUES,
    ROLE_ORDER,
    build_explicit_paragraph_map,
    build_explicit_style_map,
    classify_role,
)
from audit_docx_manuscript_style import (  # noqa: E402
    DEFAULT_BODY_STYLES,
    normalize_style_token,
    paragraph_is_body,
    paragraph_is_structurally_empty,
    parse_line_spacing_spec,
)


PROFILE_STYLES = {
    "title": ("Manuscript Title", 15.0, True, 1.0),
    "authors": ("Manuscript Authors", 12.0, False, 1.0),
    "affiliation": ("Manuscript Affiliation", 10.5, False, 1.0),
    "correspondence": ("Manuscript Correspondence", 10.5, False, 1.0),
    "keywords": ("Manuscript Keywords", 11.0, False, 1.0),
    "heading": ("Manuscript Heading", 12.0, True, 1.0),
    "body": ("Manuscript Body", 12.0, False, 2.0),
}
HEADING_STYLE_RE = re.compile(r"^(?:heading\s*[1-9]|manuscript heading)$", re.I)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize a scientific DOCX to a restrained journal-neutral profile "
            "without changing text content."
        )
    )
    parser.add_argument("document", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--front-matter-alignment",
        choices=tuple(ALIGNMENT_VALUES),
        default="left",
    )
    parser.add_argument("--line-spacing", default="double")
    parser.add_argument(
        "--abstract-start", choices=("integrated", "new-page"), default="integrated"
    )
    parser.add_argument(
        "--body-style",
        action="append",
        default=[],
        help="Existing body-prose style name or ID. Repeat as needed.",
    )
    for role in ROLE_ORDER:
        parser.add_argument(
            f"--{role}-style",
            action="append",
            default=[],
            help=f"Existing paragraph style name or ID for {role}.",
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


def text_node_values(document: Any) -> list[str]:
    return [str(node.text or "") for node in document.element.body.xpath(".//w:t")]


def set_font_name(font: Any, name: str) -> None:
    font.name = name
    r_pr = font._element.get_or_add_rPr()
    r_fonts = r_pr.get_or_add_rFonts()
    for attribute in ("ascii", "hAnsi", "eastAsia", "cs"):
        r_fonts.set(qn(f"w:{attribute}"), name)


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


def ensure_style(
    document: Any,
    name: str,
    *,
    size_pt: float,
    bold: bool,
    line_spacing: dict[str, object],
    alignment: Any,
) -> Any:
    try:
        style = document.styles[name]
    except KeyError:
        style = document.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        style.base_style = None
    set_font_name(style.font, "Times New Roman")
    style.font.size = Pt(size_pt)
    style.font.bold = bold
    style.font.color.rgb = RGBColor(0, 0, 0)
    style.paragraph_format.alignment = alignment
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.space_after = Pt(0)
    set_line_spacing(style.paragraph_format, line_spacing)
    remove_auto_spacing(style.element.get_or_add_pPr())
    return style


def format_paragraph(
    paragraph: Any,
    style: Any,
    *,
    size_pt: float,
    bold: bool,
    alignment: Any,
    line_spacing: dict[str, object],
) -> None:
    paragraph.style = style
    paragraph.alignment = alignment
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(0)
    set_line_spacing(paragraph.paragraph_format, line_spacing)
    remove_auto_spacing(paragraph._p.get_or_add_pPr())
    for run in paragraph.runs:
        set_font_name(run.font, "Times New Roman")
        run.font.size = Pt(size_pt)
        run.font.bold = bold
        run.font.color.rgb = RGBColor(0, 0, 0)


def paragraph_is_abstract(paragraph: Any) -> bool:
    return bool(re.fullmatch(r"abstract", paragraph.text.strip(), re.I))


def flatten_recognized_front_matter_tables(
    document: Any, explicit_styles: dict[str, set[str]]
) -> int:
    body = document.element.body
    flattened = 0
    first_nonempty = True
    for child in list(body):
        if child.tag == qn("w:p"):
            paragraph = Paragraph(child, document._body)
            if paragraph_is_abstract(paragraph):
                break
            if paragraph.text.strip():
                first_nonempty = False
            if child.xpath(".//w:txbxContent"):
                raise ValueError(
                    "Front matter in a text box cannot be safely normalized. "
                    "Convert it to ordinary paragraphs first."
                )
            continue
        if child.tag != qn("w:tbl"):
            continue

        paragraphs = [
            Paragraph(node, document._body)
            for node in child.xpath(".//w:tr/w:tc/w:p")
            if Paragraph(node, document._body).text.strip()
        ]
        if not paragraphs:
            body.remove(child)
            flattened += 1
            continue
        roles: list[str | None] = []
        for index, paragraph in enumerate(paragraphs):
            roles.append(
                classify_role(
                    paragraph,
                    explicit_styles,
                    first_nonempty=first_nonempty and index == 0,
                )
            )
        if any(role is None for role in roles):
            raise ValueError(
                "A table before Abstract contains non-front-matter content; "
                "refusing to flatten it automatically."
            )
        for paragraph in paragraphs:
            body.insert(body.index(child), deepcopy(paragraph._p))
        body.remove(child)
        flattened += 1
        first_nonempty = False
    return flattened


def front_matter_records(
    document: Any,
    explicit_styles: dict[str, set[str]],
    explicit_paragraphs: dict[str, set[int]],
) -> tuple[list[tuple[Any, str]], Any | None]:
    records: list[tuple[Any, str]] = []
    abstract: Any | None = None
    first_nonempty = True
    for paragraph_number, paragraph in enumerate(document.paragraphs, start=1):
        if paragraph_is_abstract(paragraph):
            abstract = paragraph
            break
        if not paragraph.text.strip():
            continue
        role = classify_role(
            paragraph,
            explicit_styles,
            first_nonempty=first_nonempty,
            paragraph_number=paragraph_number,
            explicit_paragraphs=explicit_paragraphs,
        )
        first_nonempty = False
        if role is not None:
            records.append((paragraph, role))
    return records, abstract


def normalize_front_matter_blanks(
    document: Any,
    records: list[tuple[Any, str]],
    abstract: Any | None,
    abstract_start: str,
    separator_style: Any,
    separator_spacing: dict[str, object],
) -> None:
    if not records or abstract is None:
        return
    body = document.element.body
    record_nodes = [paragraph._p for paragraph, _ in records]
    first_index = min(body.index(node) for node in record_nodes)
    last_index = max(body.index(node) for node in record_nodes)
    abstract_index = body.index(abstract._p)

    for child in list(body)[first_index + 1 : last_index]:
        if child.tag == qn("w:p") and not Paragraph(child, document._body).text.strip():
            body.remove(child)

    abstract_index = body.index(abstract._p)
    last_index = max(body.index(node) for node in record_nodes)
    for child in list(body)[last_index + 1 : abstract_index]:
        if child.tag == qn("w:p") and not Paragraph(child, document._body).text.strip():
            body.remove(child)

    if abstract_start == "integrated":
        blank = OxmlElement("w:p")
        body.insert(body.index(abstract._p), blank)
        format_paragraph(
            Paragraph(blank, document._body),
            separator_style,
            size_pt=12.0,
            bold=False,
            alignment=WD_ALIGN_PARAGRAPH.LEFT,
            line_spacing=separator_spacing,
        )
        abstract.paragraph_format.page_break_before = False
    else:
        abstract.paragraph_format.page_break_before = True


def normalize_body_separators(
    document: Any,
    body_paragraphs: list[Any],
    body_style: Any,
    line_spacing: dict[str, object],
) -> None:
    body = document.element.body
    body_nodes = {id(paragraph._p): paragraph._p for paragraph in body_paragraphs}
    children = list(body)
    index = 0
    while index < len(children):
        current = children[index]
        if id(current) not in body_nodes:
            index += 1
            continue
        cursor = index + 1
        blanks: list[Any] = []
        while cursor < len(children):
            candidate = children[cursor]
            if candidate.tag != qn("w:p"):
                break
            paragraph = Paragraph(candidate, document._body)
            if paragraph_is_structurally_empty(paragraph):
                blanks.append(candidate)
                cursor += 1
                continue
            break
        if cursor < len(children) and id(children[cursor]) in body_nodes:
            if not blanks:
                blank = OxmlElement("w:p")
                body.insert(body.index(children[cursor]), blank)
                blanks = [blank]
            for duplicate in blanks[1:]:
                body.remove(duplicate)
            separator = Paragraph(blanks[0], document._body)
            format_paragraph(
                separator,
                body_style,
                size_pt=12.0,
                bold=False,
                alignment=WD_ALIGN_PARAGRAPH.LEFT,
                line_spacing=line_spacing,
            )
        children = list(body)
        index += 1


def apply_profile(
    document_path: Path,
    output_path: Path,
    *,
    front_matter_alignment: str,
    line_spacing_token: str,
    abstract_start: str,
    body_style_tokens: set[str],
    explicit_styles: dict[str, set[str]],
    explicit_paragraphs: dict[str, set[int]],
) -> dict[str, object]:
    if document_path.resolve() == output_path.resolve():
        raise ValueError("--out must differ from the input path; preserve the source DOCX.")
    document = Document(str(document_path))
    original_text_nodes = text_node_values(document)
    flattened_tables = flatten_recognized_front_matter_tables(
        document, explicit_styles
    )

    alignment = ALIGNMENT_VALUES[front_matter_alignment]
    body_spacing = parse_line_spacing_spec(line_spacing_token)
    single_spacing = parse_line_spacing_spec("single")
    styles: dict[str, Any] = {}
    for role, (name, size, bold, _) in PROFILE_STYLES.items():
        spacing = body_spacing if role == "body" else single_spacing
        role_alignment = alignment if role in ROLE_ORDER else WD_ALIGN_PARAGRAPH.LEFT
        styles[role] = ensure_style(
            document,
            name,
            size_pt=size,
            bold=bold,
            line_spacing=spacing,
            alignment=role_alignment,
        )

    records, abstract = front_matter_records(
        document, explicit_styles, explicit_paragraphs
    )
    role_counts = {role: 0 for role in ROLE_ORDER}
    for paragraph, role in records:
        role_counts[role] += 1
        _, size, bold, _ = PROFILE_STYLES[role]
        format_paragraph(
            paragraph,
            styles[role],
            size_pt=size,
            bold=bold,
            alignment=alignment,
            line_spacing=single_spacing,
        )

    if abstract is not None:
        format_paragraph(
            abstract,
            styles["heading"],
            size_pt=12.0,
            bold=True,
            alignment=WD_ALIGN_PARAGRAPH.LEFT,
            line_spacing=single_spacing,
        )

    normalized_body_tokens = set(DEFAULT_BODY_STYLES)
    normalized_body_tokens.update(body_style_tokens)
    normalized_body_tokens.add(normalize_style_token("Manuscript Body"))
    excluded = {
        normalize_style_token(style.name)
        for role, style in styles.items()
        if role != "body"
    }
    body_paragraphs: list[Any] = []
    abstract_seen = False
    for paragraph in document.paragraphs:
        if paragraph_is_abstract(paragraph):
            abstract_seen = True
            continue
        if not abstract_seen:
            continue
        style_name = paragraph.style.name if paragraph.style is not None else ""
        if re.search(r"keyword", style_name, re.I) or re.match(
            r"^\s*keywords?\s*:", paragraph.text, re.I
        ):
            format_paragraph(
                paragraph,
                styles["keywords"],
                size_pt=11.0,
                bold=False,
                alignment=WD_ALIGN_PARAGRAPH.LEFT,
                line_spacing=single_spacing,
            )
            continue
        if HEADING_STYLE_RE.match(style_name) or (
            paragraph.text.strip() and style_name.lower().startswith("heading")
        ):
            format_paragraph(
                paragraph,
                styles["heading"],
                size_pt=12.0,
                bold=True,
                alignment=WD_ALIGN_PARAGRAPH.LEFT,
                line_spacing=single_spacing,
            )
            continue
        if paragraph_is_body(paragraph, normalized_body_tokens, excluded):
            format_paragraph(
                paragraph,
                styles["body"],
                size_pt=12.0,
                bold=False,
                alignment=WD_ALIGN_PARAGRAPH.LEFT,
                line_spacing=body_spacing,
            )
            body_paragraphs.append(paragraph)

    normalize_front_matter_blanks(
        document,
        records,
        abstract,
        abstract_start,
        styles["body"],
        single_spacing,
    )
    normalize_body_separators(
        document, body_paragraphs, styles["body"], body_spacing
    )

    for section in document.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        vertical_nodes = section._sectPr.xpath("./w:vAlign")
        vertical = vertical_nodes[0] if vertical_nodes else OxmlElement("w:vAlign")
        if not vertical_nodes:
            section._sectPr.append(vertical)
        vertical.set(qn("w:val"), "top")

    if text_node_values(document) != original_text_nodes:
        raise ValueError("Text-node preservation check failed; output was not written.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(output_path))
    return {
        "output": str(output_path.resolve()),
        "front_matter_alignment": front_matter_alignment,
        "line_spacing": body_spacing["label"],
        "role_counts": role_counts,
        "flattened_front_matter_tables": flattened_tables,
    }


def main() -> int:
    args = parse_args()
    try:
        explicit_styles = build_explicit_style_map(args)
        explicit_paragraphs = build_explicit_paragraph_map(args)
        body_style_tokens = {
            normalize_style_token(value) for value in args.body_style
        }
        result = apply_profile(
            args.document,
            args.out,
            front_matter_alignment=args.front_matter_alignment,
            line_spacing_token=args.line_spacing,
            abstract_start=args.abstract_start,
            body_style_tokens=body_style_tokens,
            explicit_styles=explicit_styles,
            explicit_paragraphs=explicit_paragraphs,
        )
    except (OSError, ValueError) as exc:
        print(f"Unable to apply manuscript profile: {exc}", file=sys.stderr)
        return 2
    print(f"Manuscript profile applied: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
