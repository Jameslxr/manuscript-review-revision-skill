#!/usr/bin/env python3
"""Flag report-like colored title/heading styling in a submission-manuscript DOCX."""

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
except ImportError as exc:  # pragma: no cover - environment-dependent error path
    print(
        "python-docx is required. Use the bundled workspace Python runtime.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


HEADING_STYLE_RE = re.compile(r"^(title|subtitle|heading\s*[1-9])$", re.IGNORECASE)
SAFE_THEME_TOKENS = {"DARK", "TEXT_1", "TEXT_2", "NONE"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit explicit or theme-colored title/headings, paragraph borders, "
            "and shading in a DOCX submission manuscript."
        )
    )
    parser.add_argument("document", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument(
        "--output-json", type=Path, help="Also write the report to this JSON file."
    )
    return parser.parse_args()


def theme_is_safe(theme: object) -> bool:
    if theme is None:
        return True
    name = getattr(theme, "name", str(theme)).upper()
    return any(token in name for token in SAFE_THEME_TOKENS)


def inspect_font(font: Any) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    color = getattr(font, "color", None)
    if color is None:
        return findings

    rgb = getattr(color, "rgb", None)
    if rgb is not None and str(rgb).upper() not in {"000000", "AUTO"}:
        findings.append({"kind": "RGB", "value": str(rgb).upper()})

    theme = getattr(color, "theme_color", None)
    if theme is not None and not theme_is_safe(theme):
        findings.append({"kind": "THEME", "value": getattr(theme, "name", str(theme))})
    return findings


def has_border(element: Any) -> bool:
    if element is None:
        return False
    return bool(element.xpath(".//w:pBdr"))


def shading_fill(element: Any) -> str | None:
    if element is None:
        return None
    nodes = element.xpath(".//w:shd")
    for node in nodes:
        fill = node.get(qn("w:fill"))
        if fill and fill.upper() not in {"AUTO", "FFFFFF", "000000"}:
            return fill.upper()
    return None


def paragraph_is_heading(paragraph: Any, first_nonempty_index: int | None, index: int) -> bool:
    style_name = paragraph.style.name if paragraph.style is not None else ""
    if HEADING_STYLE_RE.match(style_name.strip()):
        return True
    return first_nonempty_index == index


def audit(path: Path) -> dict[str, object]:
    document = Document(str(path))
    issues: list[dict[str, object]] = []
    inspected: list[dict[str, object]] = []

    first_nonempty_index: int | None = None
    for index, paragraph in enumerate(document.paragraphs, start=1):
        if paragraph.text.strip():
            first_nonempty_index = index
            break

    for index, paragraph in enumerate(document.paragraphs, start=1):
        if not paragraph.text.strip():
            continue
        if not paragraph_is_heading(paragraph, first_nonempty_index, index):
            continue

        style_name = paragraph.style.name if paragraph.style is not None else ""
        role = (
            "first-paragraph-title-candidate"
            if index == first_nonempty_index and not HEADING_STYLE_RE.match(style_name.strip())
            else style_name
        )
        preview = paragraph.text.strip().replace("\n", " ")[:100]
        record = {
            "paragraph": index,
            "role": role,
            "style": style_name,
            "text_preview": preview,
        }
        inspected.append(record)

        if paragraph.style is not None:
            for color in inspect_font(paragraph.style.font):
                issues.append(
                    {
                        **record,
                        "code": "NON_BLACK_STYLE_COLOR",
                        "detail": color,
                    }
                )

        for run_index, run in enumerate(paragraph.runs, start=1):
            for color in inspect_font(run.font):
                issues.append(
                    {
                        **record,
                        "run": run_index,
                        "code": "NON_BLACK_DIRECT_COLOR",
                        "detail": color,
                    }
                )

        paragraph_ppr = paragraph._p.pPr
        style_ppr = paragraph.style.element.pPr if paragraph.style is not None else None
        if has_border(paragraph_ppr) or has_border(style_ppr):
            issues.append(
                {
                    **record,
                    "code": "DECORATIVE_PARAGRAPH_BORDER",
                    "detail": "Title/heading paragraph has a border or rule.",
                }
            )

        fill = shading_fill(paragraph_ppr) or shading_fill(style_ppr)
        if fill:
            issues.append(
                {
                    **record,
                    "code": "TITLE_OR_HEADING_SHADING",
                    "detail": f"Non-neutral shading fill {fill}.",
                }
            )

    return {
        "status": "FAIL" if issues else "MECHANICAL_PASS",
        "document": str(path.resolve()),
        "paragraph_count": len(document.paragraphs),
        "inspected_title_heading_count": len(inspected),
        "issue_count": len(issues),
        "issues": issues,
        "inspected": inspected,
        "boundary": (
            "Mechanical style screening only. Official-template review and rendered "
            "page-by-page visual QA are still required."
        ),
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"DOCX manuscript style audit: {report['status']}",
        f"Document: {report['document']}",
        f"Inspected title/headings: {report['inspected_title_heading_count']}",
        f"Issues: {report['issue_count']}",
    ]
    for issue in report["issues"]:
        lines.append(
            "ERROR: "
            f"paragraph {issue['paragraph']} ({issue['role']}): "
            f"{issue['code']} - {issue['detail']}"
        )
    lines.append(f"BOUNDARY: {report['boundary']}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        report = audit(args.document)
    except (OSError, ValueError) as exc:
        print(f"Unable to audit DOCX: {exc}", file=sys.stderr)
        return 2

    if args.output_json:
        args.output_json.write_text(
            json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "MECHANICAL_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
