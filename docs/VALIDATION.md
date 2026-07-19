# Validation

This document records the reproducible checks for the
`manuscript-review-revision` skill.

## Automated tests

Install the single Python dependency:

```bash
python3 -m pip install -r requirements.txt
```

Run the validator test suite from the repository root:

```bash
python3 -m unittest discover \
  -s manuscript-review-revision/tests \
  -v
```

The current suite contains 12 representative tests covering:

1. a complete journal profile passes;
2. a journal profile with an unresolved mandatory rule fails;
3. a five-Agent panel with complete task receipts passes;
4. duplicate host task IDs fail;
5. a report hash that does not match the saved report fails;
6. a valid concern ledger with independently supported consensus passes;
7. one reviewer cannot label a finding as consensus;
8. located evidence without a specific pointer fails;
9. high cross-review overlap produces a diagnostic warning rather than invented
   reviewer diversity;
10. direct citation support passes only with full evidence;
11. metadata-only evidence cannot be labeled direct support;
12. blue or otherwise non-black manuscript headings fail the DOCX style audit,
   while a plain black manuscript passes.

## Syntax checks

```bash
python3 -m py_compile manuscript-review-revision/scripts/*.py
```

## Release-documentation checks

```bash
python3 manuscript-review-revision/scripts/validate_release_docs.py
```

This check confirms that:

- the Chinese and English README files link to each other;
- both README files have the same number of top-level sections and Mermaid diagrams;
- the displayed version is synchronized;
- every local Markdown link resolves;
- the two release README files remain at or below 200 lines so that detailed
  implementation material stays in `docs/`.
- Codex and Claude Code are both named in the bilingual release pages;
- Codex and Claude Code installation paths remain present in the bilingual
  README files and usage guide;
- the Skill entrypoint loads the platform-compatibility contract.
- the Skill entrypoint loads the receipt schema, concern-ledger contract, and
  biomedical review gates.

## Manual forward test

The initial release was also exercised with a synthetic hepatocellular
carcinoma manuscript targeting a high-tier hepatology journal.

This forward test ran in Codex. The repository's Claude Code compatibility is
currently validated at the Agent Skills layout, installation-documentation,
resource-path, and capability-contract levels; it has not yet completed a
Claude Code end-to-end manuscript forward test.

Expected behavior:

- the target journal is fixed before full review;
- six independent functional reviewer roles are selected for the journal tier;
- the panel validator accepts completed execution receipts and report hashes;
- the concern-ledger validator accepts evidence-anchored consensus and disagreement;
- the synthesis reports major scientific rework when warranted;
- manuscript revision does not begin before explicit author authorization.

The synthetic manuscript and generated reviews are not distributed because
they are workflow test fixtures rather than reusable Skill resources.

## Validation boundary

These checks validate the Skill structure and selected fail-closed controls.
They do not prove that every scientific judgment is correct, that every journal
website is reachable, that every compatible host exposes equivalent tools, or
that a submitted manuscript will be accepted. A host without five real
isolated subagent tasks cannot claim completion of the multi-agent review gate.
Task receipts verify recorded host identities and artifact closure; they are
not cryptographic attestation of a host's internal execution.
