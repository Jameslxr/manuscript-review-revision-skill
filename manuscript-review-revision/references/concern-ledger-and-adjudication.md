# Concern ledger and adjudication

Use this protocol after the independent reports are complete and before root
synthesis. It makes the review traceable without pretending that a structural
validator can determine scientific truth.

## One row, one concern

Create `reviews/concern_ledger.tsv`. Each row must identify:

- a unique `concern_id`
- an `issue_key` shared only when reviewers are addressing the same underlying
  issue
- the panel `reviewer_id` and `role_id`
- one review `axis` and one `severity`
- an exact `claim_pointer` into the manuscript
- an `evidence_pointer`, or an explicit reason why a location is unavailable
- the concern in falsifiable language
- a concrete `resolution_test`
- any applicable `journal_gate`
- confidence from 0 to 1
- cross-review status and adjudication disposition

Do not use invented line numbers. Prefer stable section, paragraph, table,
figure, supplement, equation, or quoted-text anchors.

## Internal review axes

These axes are scientific stress tests, not official journal requirements:

1. `journal-fit`
2. `novelty-significance`
3. `mechanism-evidence`
4. `experimental-design`
5. `statistical-rigor`
6. `reproducibility`
7. `clinical-validity`
8. `ethical-governance`
9. `data-resource-quality`
10. `figures-and-tables`
11. `writing-clarity`
12. `claim-moderation`
13. `causal-vs-correlative`
14. `reference-support`

Mark an inapplicable domain gate in the reviewer report as `NOT APPLICABLE`.
Use `NOT ASSESSABLE` only when required material is absent or inaccessible.

## Severity

- `BLOCKING`: prevents a defensible submission to the selected journal.
- `MAJOR`: materially changes interpretation, validity, or positioning.
- `MINOR`: bounded correction that does not change the central conclusion.
- `EDITORIAL`: clarity or presentation only.

Severity follows consequence, not reviewer tone or vote count.

## Cross-review status

- `UNIQUE`: raised by exactly one reviewer.
- `CONSENSUS`: independently raised by at least two reviewers with compatible
  reasoning.
- `DISAGREEMENT`: at least two reviewers reach materially different judgments
  about the same issue.

The root agent assigns these labels only after all reports are frozen. It must
preserve disagreements and explain the adjudication; it must not use majority
vote as a substitute for evidence.

Pairwise issue-key overlap above 35% is a diagnostic warning that roles may be
duplicating one another. It is not an instruction to manufacture artificial
differences. High overlap can be legitimate when a central flaw affects several
review domains.

## Resolution and disposition

Use one disposition:

- `OPEN`
- `ACCEPTED`
- `PARTIAL`
- `DISPUTED`
- `RESOLVED`
- `NOT_ASSESSABLE`

A resolution test must be observable, for example:

- analysis added with named inputs, model, contrast, and expected output
- claim narrowed to the design-supported ceiling
- cohort definition and exclusion flow made reproducible
- figure value reconciled with source data and Results text
- citation replaced by a source that directly supports the atomic claim

Do not mark an issue `RESOLVED` because prose sounds better.

## Required validation

Run:

```bash
python3 "$SKILL_ROOT/scripts/validate_concern_ledger.py" \
  reviews/concern_ledger.tsv 03_review_panel_plan.json
```

The validator checks schema, reviewer/role mapping, evidence anchors, consensus
cardinality, dispositions, and overlap. It does not verify whether the scientific
judgment itself is correct.
