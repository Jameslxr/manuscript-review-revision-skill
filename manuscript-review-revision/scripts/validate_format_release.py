#!/usr/bin/env python3
"""Combine independent DOCX formatting gates into a fail-closed release result."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PASS = "PASS"
FAIL = "FAIL"
NOT_ASSESSABLE = "NOT_ASSESSABLE"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Combine structural, front-matter, preservation, journal, and "
            "render gates into FORMAT_RELEASE_PASS only when all apply."
        )
    )
    parser.add_argument("structural_report", type=Path)
    parser.add_argument("front_matter_report", type=Path)
    parser.add_argument(
        "--content-preservation-status",
        choices=(PASS, FAIL, NOT_ASSESSABLE),
        required=True,
    )
    parser.add_argument(
        "--journal-status",
        choices=(PASS, FAIL, "NOT_APPLICABLE", NOT_ASSESSABLE),
        required=True,
    )
    parser.add_argument(
        "--render-status",
        choices=(PASS, FAIL, NOT_ASSESSABLE),
        required=True,
    )
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def normalize_report_status(
    report: dict[str, Any], *, expected_pass: str, gate: str
) -> str:
    status = report.get("status")
    if status == expected_pass:
        return PASS
    if status == FAIL:
        return FAIL
    raise ValueError(f"Unexpected {gate} report status: {status!r}")


def combine(
    structural_report: dict[str, Any],
    front_matter_report: dict[str, Any],
    *,
    content_preservation_status: str,
    journal_status: str,
    render_status: str,
) -> dict[str, Any]:
    gates = {
        "structural": normalize_report_status(
            structural_report,
            expected_pass="MECHANICAL_PASS",
            gate="structural",
        ),
        "front_matter": normalize_report_status(
            front_matter_report,
            expected_pass="FRONT_MATTER_PASS",
            gate="front-matter",
        ),
        "content_preservation": content_preservation_status,
        "journal": journal_status,
        "render": render_status,
    }
    applicable = [
        value for value in gates.values() if value != "NOT_APPLICABLE"
    ]
    if FAIL in applicable:
        status = "FORMAT_RELEASE_FAIL"
    elif NOT_ASSESSABLE in applicable:
        status = "FORMAT_RELEASE_NOT_ASSESSABLE"
    elif all(value == PASS for value in applicable):
        status = "FORMAT_RELEASE_PASS"
    else:  # pragma: no cover - choices and normalization guard this path
        raise ValueError(f"Unsupported release-gate combination: {gates}")
    return {
        "status": status,
        "gates": gates,
        "boundary": (
            "FORMAT_RELEASE_PASS verifies the resolved DOCX formatting contract. "
            "It does not verify scientific claims, citations, or submission acceptance."
        ),
    }


def main() -> int:
    args = parse_args()
    try:
        result = combine(
            read_json(args.structural_report),
            read_json(args.front_matter_report),
            content_preservation_status=args.content_preservation_status,
            journal_status=args.journal_status,
            render_status=args.render_status,
        )
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Unable to validate format release: {exc}", file=sys.stderr)
        return 2

    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(
            json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"DOCX format release: {result['status']}")
        for gate, status in result["gates"].items():
            print(f"{gate}: {status}")
        print(f"BOUNDARY: {result['boundary']}")
    return 0 if result["status"] == "FORMAT_RELEASE_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
