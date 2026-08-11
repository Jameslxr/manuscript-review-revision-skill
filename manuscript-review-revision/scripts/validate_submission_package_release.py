#!/usr/bin/env python3
"""Combine independent submission-package formatting gates."""

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
            "Return PACKAGE_FORMAT_RELEASE_PASS only when package audit, content "
            "preservation, journal, and rendered-page gates all pass."
        )
    )
    parser.add_argument("package_report", type=Path)
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


def combine(
    package_report: dict[str, Any],
    *,
    content_preservation_status: str,
    journal_status: str,
    render_status: str,
) -> dict[str, Any]:
    package_status = package_report.get("status")
    if package_status == "SUBMISSION_PACKAGE_PASS":
        normalized_package = PASS
    elif package_status == FAIL:
        normalized_package = FAIL
    else:
        raise ValueError(f"Unexpected package report status: {package_status!r}")
    gates = {
        "submission_package": normalized_package,
        "content_preservation": content_preservation_status,
        "journal": journal_status,
        "render": render_status,
    }
    applicable = [value for value in gates.values() if value != "NOT_APPLICABLE"]
    if FAIL in applicable:
        status = "PACKAGE_FORMAT_RELEASE_FAIL"
    elif NOT_ASSESSABLE in applicable:
        status = "PACKAGE_FORMAT_RELEASE_NOT_ASSESSABLE"
    elif all(value == PASS for value in applicable):
        status = "PACKAGE_FORMAT_RELEASE_PASS"
    else:  # pragma: no cover - guarded by choices
        raise ValueError(f"Unsupported release combination: {gates}")
    return {
        "status": status,
        "gates": gates,
        "boundary": (
            "PACKAGE_FORMAT_RELEASE_PASS verifies the resolved editable-package "
            "formatting contract, not scientific accuracy or editorial acceptance."
        ),
    }


def main() -> int:
    args = parse_args()
    try:
        result = combine(
            read_json(args.package_report),
            content_preservation_status=args.content_preservation_status,
            journal_status=args.journal_status,
            render_status=args.render_status,
        )
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Unable to validate package format release: {exc}", file=sys.stderr)
        return 2
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(
            json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Submission-package format release: {result['status']}")
        for gate, status in result["gates"].items():
            print(f"{gate}: {status}")
        print(f"BOUNDARY: {result['boundary']}")
    return 0 if result["status"] == "PACKAGE_FORMAT_RELEASE_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
