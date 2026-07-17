#!/usr/bin/env python3
"""Representative tests for manuscript-review-revision validators."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from docx import Document
from docx.shared import RGBColor


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = SKILL_ROOT / "scripts"


def run_script(name: str, *args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *(str(arg) for arg in args)],
        text=True,
        capture_output=True,
        check=False,
    )


class ValidatorTests(unittest.TestCase):
    def test_valid_journal_profile_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "profile.json"
            source_url = "https://journal.example.org/authors"
            path.write_text(
                json.dumps(
                    {
                        "target_journal": "Example Journal",
                        "article_type": "Original Article",
                        "submission_stage": "initial",
                        "accessed_at": "2026-07-17",
                        "profile_status": "PASS",
                        "official_sources": [
                            {
                                "title": "Author guide",
                                "url": source_url,
                                "accessed_at": "2026-07-17",
                                "official": True,
                            }
                        ],
                        "requirements": [
                            {
                                "id": "J001",
                                "category": "format",
                                "text": "Use a standard manuscript file.",
                                "source_url": source_url,
                                "applies_to": "initial",
                                "mandatory": True,
                                "status": "MET",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            result = run_script("validate_journal_profile.py", path)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("validation: PASS", result.stdout)

    def test_pass_profile_with_pending_mandatory_rule_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "profile.json"
            source_url = "https://journal.example.org/authors"
            path.write_text(
                json.dumps(
                    {
                        "target_journal": "Example Journal",
                        "article_type": "Review",
                        "submission_stage": "initial",
                        "accessed_at": "2026-07-17",
                        "profile_status": "PASS",
                        "official_sources": [
                            {
                                "title": "Author guide",
                                "url": source_url,
                                "accessed_at": "2026-07-17",
                                "official": True,
                            }
                        ],
                        "requirements": [
                            {
                                "id": "J001",
                                "category": "references",
                                "text": "Reference limit must be confirmed.",
                                "source_url": source_url,
                                "applies_to": "initial",
                                "mandatory": True,
                                "status": "PENDING",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            result = run_script("validate_journal_profile.py", path)
            self.assertEqual(result.returncode, 1)
            self.assertIn("mandatory requirements are unresolved", result.stdout)

    def test_five_agent_panel_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            roles = [
                "journal-priority",
                "domain-science",
                "study-design",
                "statistics-reproducibility",
                "claim-evidence-reference",
            ]
            reviewers = []
            for index, role in enumerate(roles, start=1):
                report = root / f"reviewer_{index:02d}.md"
                report.write_text(f"# Reviewer {index}\n\nEvidence-based report.\n")
                reviewers.append(
                    {
                        "agent_id": f"agent-{index}",
                        "role_id": role,
                        "role": role.replace("-", " "),
                        "independent": True,
                        "saw_other_reviews": False,
                        "status": "COMPLETED",
                        "report_path": report.name,
                    }
                )
            panel = root / "panel.json"
            panel.write_text(
                json.dumps(
                    {
                        "target_journal": "Example Journal",
                        "article_type": "Original Article",
                        "manuscript_sha256": "a" * 64,
                        "journal_profile_sha256": "b" * 64,
                        "execution_mode": "independent_agents",
                        "root_is_reviewer": False,
                        "synthesis_started_before_reviews_completed": False,
                        "reviewers": reviewers,
                    }
                ),
                encoding="utf-8",
            )
            result = run_script("validate_review_panel.py", panel)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Reviewer agents: 5", result.stdout)

    def test_reference_direct_support_passes_only_with_full_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ledger = Path(temp) / "references.tsv"
            columns = [
                "sentence_id",
                "atomic_claim",
                "citation_key",
                "identifier",
                "metadata_status",
                "integrity_status",
                "evidence_basis",
                "support_grade",
                "placement_status",
                "format_status",
                "action",
            ]
            with ledger.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t")
                writer.writeheader()
                writer.writerow(
                    {
                        "sentence_id": "S001",
                        "atomic_claim": "The tested relationship was observed in HCC.",
                        "citation_key": "REF001",
                        "identifier": "doi:10.1000/example",
                        "metadata_status": "VERIFIED",
                        "integrity_status": "CLEAR",
                        "evidence_basis": "RESULTS_SECTION",
                        "support_grade": "DIRECT_SUPPORT",
                        "placement_status": "PRECISE",
                        "format_status": "PASS",
                        "action": "retain",
                    }
                )
            result = run_script("validate_reference_audit.py", ledger)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("validation: PASS", result.stdout)

    def test_metadata_only_direct_support_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ledger = Path(temp) / "references.tsv"
            columns = [
                "sentence_id",
                "atomic_claim",
                "citation_key",
                "identifier",
                "metadata_status",
                "integrity_status",
                "evidence_basis",
                "support_grade",
                "placement_status",
                "format_status",
                "action",
            ]
            with ledger.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t")
                writer.writeheader()
                writer.writerow(
                    {
                        "sentence_id": "S001",
                        "atomic_claim": "A causal mechanism is established.",
                        "citation_key": "REF001",
                        "identifier": "doi:10.1000/example",
                        "metadata_status": "VERIFIED",
                        "integrity_status": "CLEAR",
                        "evidence_basis": "METADATA_ONLY",
                        "support_grade": "DIRECT_SUPPORT",
                        "placement_status": "PRECISE",
                        "format_status": "PASS",
                        "action": "inspect full text",
                    }
                )
            result = run_script("validate_reference_audit.py", ledger)
            self.assertEqual(result.returncode, 1)
            self.assertIn("requires FULL_TEXT or RESULTS_SECTION", result.stdout)

    def test_blue_heading_docx_fails_and_black_heading_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            blue_path = root / "blue.docx"
            blue = Document()
            title = blue.add_paragraph(style="Title")
            title_run = title.add_run("Blue manuscript title")
            title_run.font.color.rgb = RGBColor(0x00, 0x70, 0xC0)
            heading = blue.add_heading("Introduction", level=1)
            heading.runs[0].font.color.rgb = RGBColor(0x00, 0x70, 0xC0)
            blue.add_paragraph("Body text.")
            blue.save(blue_path)

            blue_result = run_script("audit_docx_manuscript_style.py", blue_path)
            self.assertEqual(blue_result.returncode, 1)
            self.assertIn("NON_BLACK", blue_result.stdout)

            black_path = root / "black.docx"
            black = Document()
            black.styles["Heading 1"].font.color.rgb = RGBColor(0, 0, 0)
            black_title = black.add_paragraph()
            black_title_run = black_title.add_run("Black manuscript title")
            black_title_run.bold = True
            black_title_run.font.color.rgb = RGBColor(0, 0, 0)
            black.add_heading("Introduction", level=1)
            black.add_paragraph("Body text.")
            black.save(black_path)

            black_result = run_script("audit_docx_manuscript_style.py", black_path)
            self.assertEqual(
                black_result.returncode, 0, black_result.stdout + black_result.stderr
            )
            self.assertIn("MECHANICAL_PASS", black_result.stdout)


if __name__ == "__main__":
    unittest.main()
