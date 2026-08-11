#!/usr/bin/env python3
"""Shared rules for deterministic submission-package DOCX formatting."""

from __future__ import annotations

import re
from typing import Any, Iterable

try:
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    raise SystemExit(
        "python-docx is required. Use the bundled workspace Python runtime."
    ) from exc

from audit_docx_manuscript_style import paragraph_is_structurally_empty


ARTIFACT_TYPES = ("cover-letter", "response-letter", "generic")
SALUTATION_RE = re.compile(
    r"^\s*(?:dear\b|to\s+the\s+(?:editor|editors|editorial\s+office)\b)",
    re.IGNORECASE,
)
CLOSING_RE = re.compile(
    r"^\s*(?:sincerely|yours\s+sincerely|yours\s+faithfully|respectfully|"
    r"best\s+regards|kind\s+regards|with\s+kind\s+regards)\b",
    re.IGNORECASE,
)


def top_level_paragraphs(document: Any) -> list[Paragraph]:
    return [
        Paragraph(node, document._body)
        for node in document.element.body.iterchildren()
        if node.tag == qn("w:p")
    ]


def nonempty_top_level_paragraphs(document: Any) -> list[Paragraph]:
    return [p for p in top_level_paragraphs(document) if p.text.strip()]


def paragraph_is_list(paragraph: Any) -> bool:
    p_pr = paragraph._p.pPr
    if p_pr is not None and p_pr.find(qn("w:numPr")) is not None:
        return True
    style_name = paragraph.style.name if paragraph.style is not None else ""
    return bool(re.search(r"(?:^|\b)list(?:\b|$)", style_name, re.IGNORECASE))


def _explicit_paragraph(
    paragraphs: list[Paragraph], paragraph_number: int | None, role: str
) -> Paragraph | None:
    if paragraph_number is None:
        return None
    if paragraph_number < 1 or paragraph_number > len(paragraphs):
        raise ValueError(
            f"--{role}-paragraph {paragraph_number} is outside the top-level "
            f"paragraph range 1..{len(paragraphs)}."
        )
    paragraph = paragraphs[paragraph_number - 1]
    if not paragraph.text.strip():
        raise ValueError(f"--{role}-paragraph must identify a non-empty paragraph.")
    return paragraph


def resolve_cover_letter_roles(
    document: Any,
    *,
    salutation_paragraph: int | None = None,
    closing_paragraph: int | None = None,
) -> dict[str, Any]:
    """Resolve cover-letter salutation, body, closing, and signature roles."""
    paragraphs = top_level_paragraphs(document)
    explicit_salutation = _explicit_paragraph(
        paragraphs, salutation_paragraph, "salutation"
    )
    explicit_closing = _explicit_paragraph(paragraphs, closing_paragraph, "closing")

    if explicit_salutation is None:
        candidates = [p for p in paragraphs if SALUTATION_RE.match(p.text)]
        if len(candidates) != 1:
            raise ValueError(
                "Cover-letter salutation is missing or ambiguous. Pass exactly one "
                "--salutation-paragraph after inventory."
            )
        salutation = candidates[0]
    else:
        salutation = explicit_salutation

    salutation_index = paragraphs.index(salutation)
    if explicit_closing is None:
        candidates = [
            p
            for p in paragraphs[salutation_index + 1 :]
            if CLOSING_RE.match(p.text)
        ]
        if len(candidates) != 1:
            raise ValueError(
                "Cover-letter closing is missing or ambiguous. Pass exactly one "
                "--closing-paragraph after inventory."
            )
        closing = candidates[0]
    else:
        closing = explicit_closing

    closing_index = paragraphs.index(closing)
    if closing_index <= salutation_index:
        raise ValueError("The cover-letter closing must follow the salutation.")
    body = [
        p
        for p in paragraphs[salutation_index + 1 : closing_index]
        if p.text.strip()
    ]
    if not body:
        raise ValueError("The cover letter has no non-empty body paragraph.")
    preamble = [p for p in paragraphs[:salutation_index] if p.text.strip()]
    signature = [p for p in paragraphs[closing_index + 1 :] if p.text.strip()]
    return {
        "paragraphs": paragraphs,
        "preamble": preamble,
        "salutation": salutation,
        "body": body,
        "closing": closing,
        "signature": signature,
        "salutation_paragraph": salutation_index + 1,
        "closing_paragraph": closing_index + 1,
    }


def blank_nodes_between(document: Any, left: Any, right: Any) -> list[Any] | None:
    """Return empty paragraph nodes between two blocks, or None for other content."""
    children = list(document.element.body)
    left_index = children.index(left)
    right_index = children.index(right)
    if right_index <= left_index:
        raise ValueError("Boundary nodes are not in document order.")
    blanks: list[Any] = []
    for node in children[left_index + 1 : right_index]:
        if node.tag != qn("w:p"):
            return None
        paragraph = Paragraph(node, document._body)
        if not paragraph_is_structurally_empty(paragraph):
            return None
        blanks.append(node)
    return blanks


def iter_table_paragraphs(document: Any) -> Iterable[Paragraph]:
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                yield from cell.paragraphs


def iter_body_and_table_paragraphs(document: Any) -> Iterable[Paragraph]:
    yield from top_level_paragraphs(document)
    yield from iter_table_paragraphs(document)
