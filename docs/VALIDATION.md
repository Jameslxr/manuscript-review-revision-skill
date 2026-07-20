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

Recalculate the frozen blinded benchmark:

```bash
python3 benchmarks/nature-vs-mrr-v1/score_runs.py \
  benchmarks/nature-vs-mrr-v1/answer-key.tsv \
  benchmarks/nature-vs-mrr-v1/evaluation/run-scores.tsv
python3 benchmarks/nature-vs-mrr-v1/score_runs.py \
  benchmarks/nature-vs-mrr-v1/answer-key.tsv \
  benchmarks/nature-vs-mrr-v1/evaluation/post-v1.4.0/run-score.tsv \
  --expected-runs 1
```

The current suite contains 22 representative tests covering:

1. a complete journal profile passes;
2. a journal profile with an unresolved mandatory rule fails;
3. a five-Agent panel with complete task receipts passes;
4. duplicate host task IDs fail;
5. a report hash that does not match the saved report fails;
6. a recorded `NOT_ASSESSABLE` reviewer does not count as completed;
7. a valid concern ledger with independently supported consensus passes;
8. one reviewer cannot label a finding as consensus;
9. located evidence without a specific pointer fails;
10. high cross-review overlap produces a diagnostic warning rather than invented
   reviewer diversity;
11. a seventh reviewer fails the six-seat maximum;
12. a required core role cannot be mislabeled as optional;
13. reviewer reports above 1,800 word-equivalent units fail;
14. more than eight ledger concerns from one reviewer fail;
15. more than six blocking/major concerns from one reviewer fail;
16. more than two minor/editorial concerns from one reviewer fail;
17. non-blocking out-of-role concerns fail;
18. a bounded verdict with one allowed posture passes;
19. an overlong or multiple-posture verdict fails;
20. direct citation support passes only with full evidence;
21. metadata-only evidence cannot be labeled direct support;
22. blue or otherwise non-black manuscript headings fail the DOCX style audit,
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
- the Skill entrypoint invokes both concern-ledger and bounded-verdict
  validators.

## Manual forward test

Version 1.3.0 was exercised twice against the same synthetic hepatocellular
carcinoma manuscript and frozen Nature Article profile. Current upstream
`nature-reviewer` 1.1.0 was run twice as a comparator. A blinded evaluator
scored all four packages against 18 seeded issues before system identities were
revealed.

One additional fresh-context version 1.4.0 run preserved 18/18 seeded-issue
detection with zero unsupported affirmative concerns. Its six reviewer reports
totaled 8,379 word-equivalent units versus 21,194 and 27,200 in the two
version-1.3.0 runs. This one post-run verifies the new budgets on the fixture;
it is not a replicate-based stability estimate.

This forward test ran in Codex. The repository's Claude Code compatibility is
currently validated at the Agent Skills layout, installation-documentation,
resource-path, and capability-contract levels; it has not yet completed a
Claude Code end-to-end manuscript forward test.

Expected behavior:

- the target journal is fixed before full review;
- five core roles and at most one risk-triggered specialist are selected;
- the panel validator accepts completed execution receipts and report hashes;
- the panel validator enforces axis ownership and per-seat output budgets;
- the concern-ledger validator accepts evidence-anchored consensus and disagreement;
- the synthesis reports major scientific rework when warranted;
- manuscript revision does not begin before explicit author authorization.

The synthetic manuscript, sealed answer key, scoring script, raw review
artifacts, blinded issue map, and benchmark report are distributed under
`benchmarks/nature-vs-mrr-v1/`. The comparison is a bounded forward test, not a
universal ranking of models or review systems.

## Validation boundary

These checks validate the Skill structure and selected fail-closed controls.
They do not prove that every scientific judgment is correct, that every journal
website is reachable, that every compatible host exposes equivalent tools, or
that a submitted manuscript will be accepted. A host without five real
isolated subagent tasks cannot claim completion of the multi-agent review gate.
Task receipts verify recorded host identities and artifact closure; they are
not cryptographic attestation of a host's internal execution.
