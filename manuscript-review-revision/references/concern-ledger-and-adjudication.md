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
- `role_scope`: `PRIMARY` for an owned axis or `BLOCKING_CROSSOVER` for a
  blocking out-of-role finding
- an exact `claim_pointer` into the manuscript
- an `evidence_pointer`, or an explicit reason why a location is unavailable
- the concern in falsifiable language
- one `finding_class`
- whether the paper remains defensible after claim narrowing and transparent
  limitation disclosure
- one primary `resolution_mode`
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

The panel plan assigns each axis to one primary role. A `PRIMARY` ledger row
must use that owner. A reviewer may cross the boundary only when the issue is
`BLOCKING`; record that row as `BLOCKING_CROSSOVER`. Do not use crossover rows
to duplicate major, minor, or editorial findings owned by another role.

## Severity

- `BLOCKING`: prevents a defensible submission to the selected journal.
- `MAJOR`: materially changes interpretation, validity, or positioning.
- `MINOR`: bounded correction that does not change the central conclusion.
- `EDITORIAL`: clarity or presentation only.

Severity follows consequence, not reviewer tone or vote count.

Apply the blocking test from
[evidence-calibration.md](evidence-calibration.md). `BLOCKING` is valid only
when the manuscript remains `NOT_DEFENSIBLE` after accurate claim narrowing and
transparent limitation disclosure, and the defect is anchored to located
manuscript evidence. If the paper remains defensible, use a lower severity even
when a larger cohort or additional experiment would be valuable. If evidence
cannot be located, use `NOT_ASSESSABLE`, not a speculative blocker.

## Finding class and resolution mode

Use exactly one finding class:

- `FATAL_VALIDITY_FLAW`
- `CORRECTABLE_BEFORE_SUBMISSION`
- `ACCEPTABLE_INHERENT_LIMITATION`
- `OPTIONAL_STRENGTHENING`

Record `defensibility_after_claim_narrowing` as:

- `REMAINS_DEFENSIBLE`
- `NOT_DEFENSIBLE`
- `NOT_ASSESSABLE`

Use one primary resolution mode:

- `NEW_ANALYSIS_OR_EXPERIMENT`
- `CLAIM_NARROWING`
- `LIMITATION_DISCLOSURE`
- `JUSTIFIED_NON_ACTION`
- `RETARGET`
- `EDITORIAL_CORRECTION`
- `NO_DEFENSIBLE_REMEDY`

`NO_DEFENSIBLE_REMEDY` is reserved for `FATAL_VALIDITY_FLAW`.
`OPTIONAL_STRENGTHENING` and `ACCEPTABLE_INHERENT_LIMITATION` can never be
`BLOCKING`.

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

The validator also enforces a maximum of eight concerns per reviewer. This is
a prioritization limit, not permission to omit a blocking issue: replace a
lower-severity entry when a blocking concern is found.

## Resolution and disposition

Use one disposition:

- `OPEN`
- `ACCEPTED`
- `PARTIAL`
- `DISPUTED`
- `RESOLVED`
- `ACCEPTABLE_LIMITATION`
- `NOT_ASSESSABLE`

A resolution test must be observable, for example:

- analysis added with named inputs, model, contrast, and expected output
- claim narrowed to the design-supported ceiling
- cohort definition and exclusion flow made reproducible
- figure value reconciled with source data and Results text
- citation replaced by a source that directly supports the atomic claim
- limitation disclosed and the associated claim narrowed without implying that
  a new experiment was completed
- justified non-action tied to feasibility, scope, or ethical/data-access limits

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
