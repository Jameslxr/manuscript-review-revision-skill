#!/usr/bin/env python3
"""Require a current embedded-formatting release report for every delivered DOCX."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


PROFILE_RULES = {
    "manuscript": {
        "normalizer": "apply_manuscript_profile.py",
        "release_status": "FORMAT_RELEASE_PASS",
        "required_gates": {
            "structural",
            "front_matter",
            "semantic_rhythm",
            "content_preservation",
            "journal",
            "render",
        },
    },
    "submission-package": {
        "normalizer": "apply_submission_package_profile.py",
        "release_status": "PACKAGE_FORMAT_RELEASE_PASS",
        "required_gates": {
            "submission_package",
            "content_preservation",
            "journal",
            "render",
        },
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan a delivery root and fail unless every DOCX is bound by SHA-256 "
            "to a passing embedded manuscript or submission-package release report."
        )
    )
    parser.add_argument("delivery_root", type=Path)
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_relative_path(raw: object, *, field: str) -> Path:
    value = str(raw or "").strip()
    if not value:
        raise ValueError(f"{field} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{field} must stay inside the delivery root: {value!r}")
    return path


def scan_docx(delivery_root: Path) -> set[str]:
    return {
        path.relative_to(delivery_root).as_posix()
        for path in delivery_root.rglob("*")
        if path.is_file() and path.suffix.lower() == ".docx"
    }


def validate(delivery_root: Path, receipt: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if receipt.get("schema_version") != "1.0":
        errors.append("receipt schema_version must be '1.0'")

    artifacts = receipt.get("artifacts")
    if not isinstance(artifacts, list):
        artifacts = []
        errors.append("receipt artifacts must be a list")

    actual_docx = scan_docx(delivery_root)
    recorded_paths: set[str] = set()
    verified_paths: list[str] = []

    for index, artifact in enumerate(artifacts, start=1):
        prefix = f"artifacts[{index}]"
        entry_error_start = len(errors)
        if not isinstance(artifact, dict):
            errors.append(f"{prefix} must be an object")
            continue
        try:
            relative_docx = safe_relative_path(
                artifact.get("path"), field=f"{prefix}.path"
            )
        except ValueError as exc:
            errors.append(str(exc))
            continue
        relative_docx_text = relative_docx.as_posix()
        if relative_docx_text in recorded_paths:
            errors.append(f"duplicate DOCX receipt entry: {relative_docx_text}")
            continue
        recorded_paths.add(relative_docx_text)

        if relative_docx.suffix.lower() != ".docx":
            errors.append(f"{prefix}.path is not a DOCX: {relative_docx_text}")
            continue
        docx_path = delivery_root / relative_docx
        if not docx_path.is_file():
            errors.append(f"recorded DOCX does not exist: {relative_docx_text}")
            continue

        recorded_hash = str(artifact.get("sha256") or "").strip().lower()
        current_hash = sha256(docx_path)
        if recorded_hash != current_hash:
            errors.append(
                f"final DOCX hash mismatch for {relative_docx_text}: "
                f"receipt={recorded_hash or 'MISSING'} current={current_hash}"
            )

        profile = str(artifact.get("profile") or "").strip()
        rule = PROFILE_RULES.get(profile)
        if rule is None:
            errors.append(
                f"{prefix}.profile must be one of {sorted(PROFILE_RULES)}"
            )
            continue
        normalizer = str(artifact.get("normalizer") or "").strip()
        if normalizer != rule["normalizer"]:
            errors.append(
                f"{relative_docx_text} must use {rule['normalizer']} for profile {profile}"
            )

        try:
            report_relative = safe_relative_path(
                artifact.get("release_report"), field=f"{prefix}.release_report"
            )
        except ValueError as exc:
            errors.append(str(exc))
            continue
        report_path = delivery_root / report_relative
        if not report_path.is_file():
            errors.append(
                f"release report does not exist for {relative_docx_text}: "
                f"{report_relative.as_posix()}"
            )
            continue
        try:
            report = read_json(report_path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"invalid release report for {relative_docx_text}: {exc}")
            continue

        if report.get("status") != rule["release_status"]:
            errors.append(
                f"{relative_docx_text} release status must be "
                f"{rule['release_status']}, got {report.get('status')!r}"
            )
        gates = report.get("gates")
        if not isinstance(gates, dict):
            errors.append(f"{relative_docx_text} release report lacks a gates object")
            continue
        missing_gates = sorted(rule["required_gates"] - set(gates))
        if missing_gates:
            errors.append(
                f"{relative_docx_text} release report lacks gates: "
                + ", ".join(missing_gates)
            )
        for gate in sorted(rule["required_gates"]):
            value = gates.get(gate)
            allowed = {"PASS", "NOT_APPLICABLE"} if gate == "journal" else {"PASS"}
            if value not in allowed:
                errors.append(
                    f"{relative_docx_text} gate {gate} must be "
                    f"{' or '.join(sorted(allowed))}, got {value!r}"
                )

        if len(errors) == entry_error_start:
            verified_paths.append(relative_docx_text)

    missing_receipts = sorted(actual_docx - recorded_paths)
    stale_receipts = sorted(recorded_paths - actual_docx)
    if missing_receipts:
        errors.append(
            "DOCX files without release receipts: " + ", ".join(missing_receipts)
        )
    if stale_receipts:
        errors.append(
            "receipt entries without delivered DOCX files: "
            + ", ".join(stale_receipts)
        )

    if not actual_docx and not errors:
        status = "GENERATED_DOCX_RELEASE_NOT_APPLICABLE"
    elif errors:
        status = "GENERATED_DOCX_RELEASE_FAIL"
    else:
        status = "GENERATED_DOCX_RELEASE_PASS"
    return {
        "status": status,
        "delivery_root": str(delivery_root),
        "docx_count": len(actual_docx),
        "verified_docx": sorted(verified_paths),
        "errors": errors,
        "boundary": (
            "This gate proves complete DOCX receipt coverage and final-file hash closure "
            "inside the declared delivery root. It does not validate non-DOCX artifacts "
            "or scientific accuracy."
        ),
    }


def main() -> int:
    args = parse_args()
    try:
        delivery_root = args.delivery_root.resolve(strict=True)
        if not delivery_root.is_dir():
            raise ValueError(f"delivery root is not a directory: {delivery_root}")
        result = validate(delivery_root, read_json(args.receipt))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Unable to validate generated DOCX release: {exc}", file=sys.stderr)
        return 2

    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(
            json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Generated DOCX release: {result['status']}")
        print(f"DOCX files: {result['docx_count']}")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        print(f"BOUNDARY: {result['boundary']}")
    return 0 if result["status"] != "GENERATED_DOCX_RELEASE_FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
