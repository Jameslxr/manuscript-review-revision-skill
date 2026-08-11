#!/usr/bin/env python3
"""Shared semantic-role rules for manuscript DOCX normalization and audit."""

from __future__ import annotations

import re
from copy import deepcopy
from typing import Any

try:
    from docx.text.run import Run
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    raise SystemExit(
        "python-docx is required. Use the bundled workspace Python runtime."
    ) from exc


BODY_FONT_SIZE_PT = 12.0
HEADING_STYLE_RE = re.compile(r"^(?:heading\s*[1-9]|manuscript heading)$", re.I)
KEYWORD_LABEL_RE = re.compile(r"^(\s*(?:keywords?|key\s+words)\s*:)", re.I)
CREDIT_LABEL = (
    r"cr[eé]dit(?:\s+(?:author(?:ship)?(?:\s+contribution)?\s+statement|"
    r"contributor\s+roles?))?"
)
DECLARATION_LABEL = (
    rf"(?:author\s+contributions?|{CREDIT_LABEL}|"
    r"funding|conflicts?\s+of\s+interest|competing\s+interests?|"
    r"data\s+availability(?:\s+statement)?|acknowledg(?:e)?ments?|"
    r"institutional\s+review\s+board\s+statement|informed\s+consent\s+statement|"
    r"ethics\s+(?:approval|statement)|consent\s+for\s+publication)"
)
DECLARATION_HEADING_RE = re.compile(rf"^\s*{DECLARATION_LABEL}\s*:?[\s.]*$", re.I)
DECLARATION_INLINE_RE = re.compile(rf"^(\s*{DECLARATION_LABEL}\s*:)", re.I)
CREDIT_HEADING_RE = re.compile(rf"^\s*{CREDIT_LABEL}\s*:?[\s.]*$", re.I)
CREDIT_INLINE_RE = re.compile(rf"^(\s*{CREDIT_LABEL}\s*:)", re.I)

CREDIT_ROLE_PATTERNS = {
    label: re.compile(pattern, re.I)
    for label, pattern in {
        "Conceptualization": r"\bConceptualization\b",
        "Data curation": r"\bData\s+curation\b",
        "Formal analysis": r"\bFormal\s+analysis\b",
        "Funding acquisition": r"\bFunding\s+acquisition\b",
        "Investigation": r"\bInvestigation\b",
        "Methodology": r"\bMethodology\b",
        "Project administration": r"\bProject\s+administration\b",
        "Resources": r"\bResources\b",
        "Software": r"\bSoftware\b",
        "Supervision": r"\bSupervision\b",
        "Validation": r"\bValidation\b",
        "Visualization": r"\bVisualization\b",
        "Writing – original draft": r"\bWriting\s*[-–—]\s*original\s+draft\b",
        "Writing – review & editing": (
            r"\bWriting\s*[-–—]\s*review\s*(?:&|and)\s*editing\b"
        ),
    }.items()
}


def credit_role_labels(text: str) -> set[str]:
    """Return official CRediT role labels recognized in supplied statement text."""
    return {
        label for label, pattern in CREDIT_ROLE_PATTERNS.items() if pattern.search(text)
    }


def bold_leading_label(paragraph: Any, pattern: re.Pattern[str]) -> bool:
    """Bold only a recognized leading label while preserving remaining text."""
    match = pattern.match(paragraph.text)
    if match is None:
        return False
    label_end = match.end(1)
    consumed = 0
    for run in list(paragraph.runs):
        text = run.text
        run_start = consumed
        run_end = consumed + len(text)
        consumed = run_end
        if run_start >= label_end:
            run.font.bold = False
            continue
        if run_end <= label_end:
            run.font.bold = True
            continue
        split_at = label_end - run_start
        label_text = text[:split_at]
        remainder = text[split_at:]
        run.text = label_text
        run.font.bold = True
        if remainder:
            remainder_xml = deepcopy(run._r)
            run._r.addnext(remainder_xml)
            remainder_run = Run(remainder_xml, paragraph)
            remainder_run.text = remainder
            remainder_run.font.bold = False
        break
    return True
