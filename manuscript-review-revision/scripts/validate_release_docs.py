#!/usr/bin/env python3
"""Validate the bilingual GitHub release documentation."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README_EN.md"
USAGE = ROOT / "docs" / "USAGE.md"
SKILL_ENTRY = ROOT / "manuscript-review-revision" / "SKILL.md"
CONCERN_LEDGER_VALIDATOR = (
    ROOT
    / "manuscript-review-revision"
    / "scripts"
    / "validate_concern_ledger.py"
)
MAX_README_LINES = 200
LOCAL_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
VERSION_RE = re.compile(r"version-v(\d+\.\d+\.\d+)")


def markdown_files() -> list[Path]:
    files = [README_ZH, README_EN, ROOT / "ATTRIBUTION.md", SKILL_ENTRY]
    files.extend(sorted((ROOT / "docs").glob("*.md")))
    files.extend(
        sorted((ROOT / "manuscript-review-revision" / "references").glob("*.md"))
    )
    return files


def local_link_errors(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw_target in LOCAL_LINK_RE.findall(text):
        target = raw_target.strip().strip("<>")
        if (
            not target
            or target.startswith(("#", "http://", "https://", "mailto:"))
        ):
            continue
        local_part = target.split("#", 1)[0]
        if not local_part:
            continue
        resolved = (path.parent / local_part).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link {raw_target!r}")
    return errors


def main() -> int:
    errors: list[str] = []

    for path in markdown_files():
        if not path.exists():
            errors.append(f"missing release document: {path.relative_to(ROOT)}")
    if not CONCERN_LEDGER_VALIDATOR.is_file():
        errors.append(
            "missing concern-ledger validator: "
            f"{CONCERN_LEDGER_VALIDATOR.relative_to(ROOT)}"
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    zh = README_ZH.read_text(encoding="utf-8")
    en = README_EN.read_text(encoding="utf-8")
    usage = USAGE.read_text(encoding="utf-8")
    skill_entry = SKILL_ENTRY.read_text(encoding="utf-8")

    if "[English](README_EN.md)" not in zh:
        errors.append("README.md is missing the English language switch.")
    if "[中文说明](README.md)" not in en:
        errors.append("README_EN.md is missing the Chinese language switch.")

    zh_sections = len(re.findall(r"^## ", zh, flags=re.MULTILINE))
    en_sections = len(re.findall(r"^## ", en, flags=re.MULTILINE))
    if zh_sections != en_sections:
        errors.append(
            "README section-count mismatch: "
            f"Chinese={zh_sections}, English={en_sections}."
        )

    zh_mermaid = zh.count("```mermaid")
    en_mermaid = en.count("```mermaid")
    if zh_mermaid != en_mermaid:
        errors.append(
            "README Mermaid-count mismatch: "
            f"Chinese={zh_mermaid}, English={en_mermaid}."
        )

    zh_versions = VERSION_RE.findall(zh)
    en_versions = VERSION_RE.findall(en)
    if len(zh_versions) != 1 or zh_versions != en_versions:
        errors.append(
            "README version mismatch or missing unique version badge: "
            f"Chinese={zh_versions}, English={en_versions}."
        )

    for label, text in (("README.md", zh), ("README_EN.md", en)):
        for required in ("Codex", "Claude Code"):
            if required not in text:
                errors.append(f"{label} is missing host: {required}.")

    for install_path in ("$HOME/.codex/skills", "$HOME/.claude/skills"):
        if install_path not in zh or install_path not in en or install_path not in usage:
            errors.append(
                f"Cross-platform install path is not documented consistently: "
                f"{install_path}."
            )

    if "references/platform-compatibility.md" not in skill_entry:
        errors.append(
            "SKILL.md does not load references/platform-compatibility.md."
        )
    for required_reference in (
        "references/review-panel-receipt-schema.md",
        "references/concern-ledger-and-adjudication.md",
        "references/biomedical-review-gates.md",
    ):
        if required_reference not in skill_entry:
            errors.append(f"SKILL.md does not load {required_reference}.")
    if "scripts/validate_concern_ledger.py" not in skill_entry:
        errors.append("SKILL.md does not invoke scripts/validate_concern_ledger.py.")

    for path, text in ((README_ZH, zh), (README_EN, en)):
        line_count = len(text.splitlines())
        if line_count > MAX_README_LINES:
            errors.append(
                f"{path.name} has {line_count} lines; maximum is "
                f"{MAX_README_LINES}."
            )

    for path in markdown_files():
        errors.extend(
            local_link_errors(path, path.read_text(encoding="utf-8"))
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Release documentation: PASS")
    print(f"README sections: {zh_sections}")
    print(f"Mermaid diagrams per README: {zh_mermaid}")
    print(f"Version: v{zh_versions[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
