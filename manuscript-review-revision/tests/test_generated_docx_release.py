#!/usr/bin/env python3
"""Regression tests for complete embedded-formatting coverage of delivered DOCX."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = SKILL_ROOT / "scripts" / "validate_generated_docx_release.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def release_report(profile: str, *, status: str | None = None) -> dict[str, object]:
    if profile == "manuscript":
        return {
            "status": status or "FORMAT_RELEASE_PASS",
            "gates": {
                "structural": "PASS",
                "front_matter": "PASS",
                "semantic_rhythm": "PASS",
                "content_preservation": "PASS",
                "journal": "PASS",
                "render": "PASS",
            },
        }
    return {
        "status": status or "PACKAGE_FORMAT_RELEASE_PASS",
        "gates": {
            "submission_package": "PASS",
            "content_preservation": "PASS",
            "journal": "NOT_APPLICABLE",
            "render": "PASS",
        },
    }


def add_artifact(root: Path, relative: str, profile: str) -> dict[str, str]:
    docx = root / relative
    docx.parent.mkdir(parents=True, exist_ok=True)
    docx.write_bytes(f"synthetic DOCX fixture: {relative}".encode())
    report = docx.with_suffix(".format-release.json")
    report.write_text(json.dumps(release_report(profile)), encoding="utf-8")
    return {
        "path": relative,
        "sha256": sha256(docx),
        "profile": profile,
        "normalizer": (
            "apply_manuscript_profile.py"
            if profile == "manuscript"
            else "apply_submission_package_profile.py"
        ),
        "release_report": report.relative_to(root).as_posix(),
    }


def run_validator(root: Path, receipt: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(root), str(receipt), "--json"],
        text=True,
        capture_output=True,
        check=False,
    )


class GeneratedDocxReleaseTests(unittest.TestCase):
    def test_every_manuscript_and_package_docx_can_close(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifacts = [
                add_artifact(root, "revision/manuscript_clean.docx", "manuscript"),
                add_artifact(
                    root, "submission/cover_letter.docx", "submission-package"
                ),
            ]
            receipt = root / "07_generated_docx_release_receipt.json"
            receipt.write_text(
                json.dumps({"schema_version": "1.0", "artifacts": artifacts}),
                encoding="utf-8",
            )
            result = run_validator(root, receipt)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["status"], "GENERATED_DOCX_RELEASE_PASS")
            self.assertEqual(payload["docx_count"], 2)

    def test_unreceipted_docx_blocks_delivery(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifacts = [add_artifact(root, "manuscript.docx", "manuscript")]
            (root / "unreceipted_clean_copy.docx").write_bytes(b"unreceipted")
            receipt = root / "receipt.json"
            receipt.write_text(
                json.dumps({"schema_version": "1.0", "artifacts": artifacts}),
                encoding="utf-8",
            )
            result = run_validator(root, receipt)
            self.assertEqual(result.returncode, 1)
            self.assertIn("DOCX files without release receipts", result.stdout)

    def test_post_pass_docx_write_invalidates_hash_closure(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifacts = [add_artifact(root, "manuscript.docx", "manuscript")]
            (root / "manuscript.docx").write_bytes(b"changed after validation")
            receipt = root / "receipt.json"
            receipt.write_text(
                json.dumps({"schema_version": "1.0", "artifacts": artifacts}),
                encoding="utf-8",
            )
            result = run_validator(root, receipt)
            self.assertEqual(result.returncode, 1)
            self.assertIn("final DOCX hash mismatch", result.stdout)

    def test_wrong_embedded_profile_or_nonpassing_release_blocks_delivery(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifact = add_artifact(root, "cover_letter.docx", "submission-package")
            artifact["normalizer"] = "apply_manuscript_profile.py"
            report = root / artifact["release_report"]
            report.write_text(
                json.dumps(
                    release_report(
                        "submission-package",
                        status="PACKAGE_FORMAT_RELEASE_NOT_ASSESSABLE",
                    )
                ),
                encoding="utf-8",
            )
            receipt = root / "receipt.json"
            receipt.write_text(
                json.dumps({"schema_version": "1.0", "artifacts": [artifact]}),
                encoding="utf-8",
            )
            result = run_validator(root, receipt)
            self.assertEqual(result.returncode, 1)
            self.assertIn("apply_submission_package_profile.py", result.stdout)
            self.assertIn("PACKAGE_FORMAT_RELEASE_PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
