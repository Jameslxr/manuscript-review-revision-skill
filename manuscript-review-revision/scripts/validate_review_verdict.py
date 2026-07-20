#!/usr/bin/env python3
"""Validate the bounded author-facing scientific-review verdict."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


POSTURES = {
    "PROCEED_TO_REVISION",
    "MAJOR_SCIENTIFIC_REWORK_REQUIRED",
    "RETARGET_RECOMMENDED",
    "NOT_ASSESSABLE",
}
REPORT_UNIT_RE = re.compile(
    r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*|[\u3400-\u4dbf\u4e00-\u9fff]"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a concise author-facing review verdict."
    )
    parser.add_argument("verdict", type=Path)
    parser.add_argument("--maximum", type=int, default=900)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def validate(path: Path, maximum: int) -> dict[str, object]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return {
            "status": "FAIL",
            "word_equivalent_units": 0,
            "postures": [],
            "errors": [f"Unable to read verdict as UTF-8 text: {exc}"],
        }
    if not text.strip():
        errors.append("Verdict is empty.")
    units = len(REPORT_UNIT_RE.findall(text))
    if units > maximum:
        errors.append(
            f"Verdict contains {units} word-equivalent units; maximum is {maximum}."
        )
    found_postures = sorted(
        posture for posture in POSTURES if re.search(rf"\b{posture}\b", text)
    )
    if len(found_postures) != 1:
        errors.append(
            "Verdict must contain exactly one allowed review posture; found "
            f"{found_postures}."
        )
    return {
        "status": "PASS" if not errors else "FAIL",
        "word_equivalent_units": units,
        "maximum": maximum,
        "postures": found_postures,
        "errors": errors,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"Review verdict validation: {report['status']}",
        f"Word-equivalent units: {report.get('word_equivalent_units', 0)}",
        f"Maximum: {report.get('maximum', 0)}",
        f"Posture: {', '.join(report.get('postures', [])) or 'NONE'}",
    ]
    lines.extend(f"ERROR: {error}" for error in report.get("errors", []))
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    if args.maximum <= 0:
        print("--maximum must be positive.", file=sys.stderr)
        return 2
    report = validate(args.verdict, args.maximum)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
