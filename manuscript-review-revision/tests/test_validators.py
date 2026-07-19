#!/usr/bin/env python3
"""Representative tests for manuscript-review-revision validators."""

from __future__ import annotations

import csv
import hashlib
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
CORE_ROLES = [
    "journal-priority",
    "domain-science",
    "study-design",
    "statistics-reproducibility",
    "claim-evidence-reference",
]
CONCERN_COLUMNS = [
    "concern_id",
    "issue_key",
    "reviewer_id",
    "role_id",
    "axis",
    "severity",
    "claim_pointer",
    "evidence_pointer",
    "evidence_status",
    "concern",
    "resolution_test",
    "journal_gate",
    "confidence",
    "consensus_status",
    "disposition",
]


def run_script(name: str, *args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *(str(arg) for arg in args)],
        text=True,
        capture_output=True,
        check=False,
    )


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_panel(
    root: Path, *, duplicate_task: bool = False, corrupt_report_hash: bool = False
) -> Path:
    frozen_hashes = {
        "manuscript_sha256": "a" * 64,
        "journal_profile_sha256": "b" * 64,
        "shared_fact_base_sha256": "c" * 64,
    }
    reviewers = []
    for index, role in enumerate(CORE_ROLES, start=1):
        report = root / f"reviewer_{index:02d}.md"
        report.write_text(
            f"# Reviewer {index}\n\nEvidence-based report for {role}.\n",
            encoding="utf-8",
        )
        task_number = 1 if duplicate_task and index == 2 else index
        reviewers.append(
            {
                "agent_id": f"agent-{index}",
                "host_task_id": f"host-task-{task_number}",
                "receipt_source": "HOST_NATIVE",
                "context_mode": "FRESH_NON_FORK",
                "role_id": role,
                "role": role.replace("-", " "),
                "independent": True,
                "saw_other_reviews": False,
                "status": "COMPLETED",
                "started_at": f"2026-07-19T10:0{index}:00-05:00",
                "completed_at": f"2026-07-19T10:1{index}:00-05:00",
                "input_hashes": frozen_hashes,
                "report_path": report.name,
                "report_sha256": (
                    "d" * 64
                    if corrupt_report_hash and index == 1
                    else file_sha256(report)
                ),
            }
        )
    panel = root / "panel.json"
    panel.write_text(
        json.dumps(
            {
                "panel_schema_version": "2.0",
                "skill_version": "1.3.0",
                "host": "Test Host",
                "host_version": "1.0",
                "target_journal": "Example Journal",
                "article_type": "Original Article",
                **frozen_hashes,
                "execution_mode": "independent_agents",
                "root_is_reviewer": False,
                "synthesis_started_before_reviews_completed": False,
                "reviewers": reviewers,
            }
        ),
        encoding="utf-8",
    )
    return panel


def write_concern_ledger(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CONCERN_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def concern_row(
    concern_id: str,
    issue_key: str,
    reviewer_number: int,
    role_id: str,
    *,
    consensus_status: str = "UNIQUE",
    evidence_status: str = "LOCATED",
    evidence_pointer: str = "Results > Validation, paragraph 2",
) -> dict[str, str]:
    return {
        "concern_id": concern_id,
        "issue_key": issue_key,
        "reviewer_id": f"agent-{reviewer_number}",
        "role_id": role_id,
        "axis": "experimental-design",
        "severity": "MAJOR",
        "claim_pointer": "Discussion, paragraph 1: external validity",
        "evidence_pointer": evidence_pointer,
        "evidence_status": evidence_status,
        "concern": "The stated generalization exceeds the tested cohort.",
        "resolution_test": "Narrow the claim or add an independent external cohort.",
        "journal_gate": "evidence threshold",
        "confidence": "0.9",
        "consensus_status": consensus_status,
        "disposition": (
            "NOT_ASSESSABLE" if evidence_status == "NOT_ASSESSABLE" else "OPEN"
        ),
    }


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
            panel = write_panel(root)
            result = run_script("validate_review_panel.py", panel)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Reviewer agents: 5", result.stdout)
            self.assertIn("Validated receipts: 5", result.stdout)

    def test_duplicate_task_id_and_inconsistent_input_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            panel = write_panel(root, duplicate_task=True)
            result = run_script("validate_review_panel.py", panel)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Duplicate host_task_id", result.stdout)

            panel = write_panel(root)
            content = json.loads(panel.read_text(encoding="utf-8"))
            content["reviewers"][0]["input_hashes"]["manuscript_sha256"] = "f" * 64
            panel.write_text(json.dumps(content), encoding="utf-8")
            result = run_script("validate_review_panel.py", panel)
            self.assertEqual(result.returncode, 1)
            self.assertIn("does not match the frozen panel input", result.stdout)

    def test_report_hash_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            panel = write_panel(Path(temp), corrupt_report_hash=True)
            result = run_script("validate_review_panel.py", panel)
            self.assertEqual(result.returncode, 1)
            self.assertIn("report_sha256 does not match", result.stdout)

    def test_concern_ledger_passes_with_valid_consensus(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            panel = write_panel(root)
            ledger = root / "concerns.tsv"
            rows = [
                concern_row(
                    "C001",
                    "external-validation",
                    2,
                    "domain-science",
                    consensus_status="CONSENSUS",
                ),
                concern_row(
                    "C002",
                    "external-validation",
                    3,
                    "study-design",
                    consensus_status="CONSENSUS",
                ),
                concern_row(
                    "C003",
                    "multiplicity",
                    4,
                    "statistics-reproducibility",
                ),
            ]
            write_concern_ledger(ledger, rows)
            result = run_script("validate_concern_ledger.py", ledger, panel)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Concern ledger validation: PASS", result.stdout)
            self.assertIn("Consensus / disagreement / unique: 1 / 0 / 1", result.stdout)

    def test_single_reviewer_cannot_claim_consensus(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            panel = write_panel(root)
            ledger = root / "concerns.tsv"
            write_concern_ledger(
                ledger,
                [
                    concern_row(
                        "C001",
                        "external-validation",
                        3,
                        "study-design",
                        consensus_status="CONSENSUS",
                    )
                ],
            )
            result = run_script("validate_concern_ledger.py", ledger, panel)
            self.assertEqual(result.returncode, 1)
            self.assertIn("fewer than two reviewers", result.stdout)

    def test_located_evidence_requires_pointer(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            panel = write_panel(root)
            ledger = root / "concerns.tsv"
            write_concern_ledger(
                ledger,
                [
                    concern_row(
                        "C001",
                        "external-validation",
                        3,
                        "study-design",
                        evidence_pointer="",
                    )
                ],
            )
            result = run_script("validate_concern_ledger.py", ledger, panel)
            self.assertEqual(result.returncode, 1)
            self.assertIn("requires a specific evidence_pointer", result.stdout)

    def test_high_overlap_warns_without_inventing_diversity(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            panel = write_panel(root)
            ledger = root / "concerns.tsv"
            rows = []
            for issue_number in range(1, 4):
                issue_key = f"shared-{issue_number}"
                rows.extend(
                    [
                        concern_row(
                            f"C{issue_number}A",
                            issue_key,
                            2,
                            "domain-science",
                            consensus_status="CONSENSUS",
                        ),
                        concern_row(
                            f"C{issue_number}B",
                            issue_key,
                            3,
                            "study-design",
                            consensus_status="CONSENSUS",
                        ),
                    ]
                )
            write_concern_ledger(ledger, rows)
            result = run_script("validate_concern_ledger.py", ledger, panel)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("WARNING: Reviewer pair agent-2/agent-3", result.stdout)

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
