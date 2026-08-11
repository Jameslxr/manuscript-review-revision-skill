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

The current suite contains 69 representative tests covering:

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
22. an acceptable inherent limitation can pass without being promoted to a blocker;
23. `BLOCKING` requires the manuscript to remain indefensible after claim narrowing;
24. optional strengthening cannot be labeled `BLOCKING`;
25. a blocking concern requires located manuscript evidence;
26. an incomplete sampled tier-C context citation produces an advisory and can pass;
27. the same unresolved evidence in a tier-A material claim blocks a pass;
28. blue or otherwise non-black manuscript headings fail the DOCX style audit,
    while a plain black manuscript passes;
29. an acceptance-tolerance card with five exact comparators passes;
30. comparator substitution without a disclosed reason fails;
31. non-zero body paragraph spacing and missing literal blank paragraphs fail the DOCX audit;
32. exactly one real empty paragraph with zero spacing passes the DOCX audit;
33. the DOCX audit rejects a journal-template attempt to bypass literal blank paragraphs;
34. implicit or wrong body/separator line spacing fails the DOCX audit;
35. exact and at-least point-based line-spacing tokens pass when encoded explicitly;
36. a complete source-linked journal format plan passes;
37. omission of any required journal-format category fails;
38. a journal-template paragraph override is rejected even when official-template authority is claimed;
39. literal-blank plans with non-zero paragraph spacing fail;
40. a passing format plan cannot conceal an unresolved mandatory journal rule;
41. the formatting gate rejects a structurally valid draft plan;
42. a complete plan-to-manuscript journal format audit passes;
43. omission of any format-plan check from the final audit fails;
44. an overall format pass cannot conceal failed mechanical or visual QA;
45. plan-to-output audit closure rejects a non-passing format plan;
46. an unclassified custom paragraph style blocks DOCX delivery until explicitly excluded;
47. a custom prose style must be explicitly included in the whole-document audit;
48. the DOCX audit rejects attempts to disable the line-spacing gate;
49. hidden Word before/after auto-spacing blocks delivery until disabled;
50. a format plan cannot disable the continuous line/page-number invariant;
51. missing Word-native line numbering or a dynamic page field blocks DOCX delivery;
52. section restarts and paragraph-level line-number suppression block delivery;
53. the bundled numbering enforcer covers multi-section first/default/even page stories;
54. the integrated manuscript profile repairs all-Normal and adversarial title blocks;
55. centered, mixed, oversized, table-based, and over-spaced front matter fails;
56. the journal-neutral profile requires left-aligned title, authors, affiliations, and correspondence;
57. upper-right and sourced lower-center dynamic page-number profiles are distinguished;
58. the profile normalizer is idempotent and preserves non-empty text;
59. front-matter blank-paragraph spacing is rejected and repaired;
60. the combined format-release validator is fail-closed on unassessed rendering;
61. the journal format plan requires explicit front-matter alignment, anonymization, and page-number position;
62. plan-to-output closure rejects mismatched page-number placement;
63. plan-to-output closure requires front-matter audit PASS;
64. plan-to-output closure requires content-preservation PASS;
65. plan-to-output closure requires `FORMAT_RELEASE_PASS`;
66. custom styles must be classified in the embedded formatting lane;
67. hidden automatic paragraph spacing fails in the embedded formatting lane;
68. literal blank paragraphs and continuous numbering pass in the embedded lane;
69. multi-section active page stories pass in the embedded lane.

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
  implementation material stays in `docs/`;
- Codex and Claude Code are both named in the bilingual release pages;
- Codex and Claude Code installation paths remain present in the bilingual
  README files and usage guide;
- the Skill entrypoint loads the platform-compatibility contract;
- the Skill entrypoint loads the receipt schema, concern-ledger contract, and
  biomedical review gates;
- the Skill entrypoint loads the accepted-paper evidence-calibration contract;
- the Skill entrypoint invokes the acceptance-tolerance, concern-ledger, and
  bounded-verdict validators;
- the Skill entrypoint embeds front-matter normalization/audit and the combined
  DOCX format-release validator.

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

Version 1.5.0 adds a separate acceptance-tolerance calibration audit using 24
recent open-access HCC/iCCA papers across four editorial classes and four public
Nature Communications peer-review packages. The frozen corpus, method,
observed boundaries, and limitations are documented in
[`benchmarks/acceptance-tolerance-v1/`](../benchmarks/acceptance-tolerance-v1/README.md).
This audit motivated the four finding classes and risk-tiered reference gate;
it is not a universal estimate of journal acceptance practice.

Version 1.6.0 added 16 formatting-focused tests. Version 1.6.1 adds three
semantic-rhythm regressions, bringing this focused set to 19 tests: the
standalone formatter's 17-test corpus inside the integrated review/revision
Skill plus two plan/audit closure tests. The tests cover adversarial front
matter, body-sized author/affiliation/declaration roles, Keywords label
emphasis, section/subsection/CRediT blank-line boundaries, literal blank
paragraphs, consecutive non-body reference entries, generated-heading audit
coverage, hidden Word auto-spacing, explicit manuscript-wide line spacing,
continuous line/page numbering, content preservation, idempotence, and
fail-closed format-release composition. Passing
these fixtures validates the encoded contracts, not every possible DOCX or
journal template.

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
- the concern ledger separates fatal flaws, correctable issues, acceptable
  limitations, and optional strengthening;
- a blocking finding fails the claim-narrowing and transparent-limitation test;
- tier-A/tier-B citations remain fail-closed while incomplete sampled tier-C
  context checks remain advisory;
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
