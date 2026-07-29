# Evidence calibration and acceptance tolerance

Use this protocol after the exact journal, article type, and submission stage
are fixed. Its purpose is to calibrate review severity to demonstrated journal
practice without treating published papers as scientifically flawless.

## Evidence hierarchy

Use three distinct evidence layers:

1. official journal requirements and editor instructions: mandatory when they
   apply;
2. scientific validity and integrity: never relaxed by precedent;
3. recent accepted same-type papers: evidence about editorial tolerance,
   positioning, and feasible evidence depth, not a waiver of validity.

Official requirements outrank comparators. A published paper with a weakness
does not authorize repeating that weakness, but it can show that an honestly
bounded limitation is not automatically fatal.

## Acceptance-tolerance card

For a full scientific review, inspect at least five recent accepted papers from
the exact journal and article type when accessible. Expand toward ten when the
designs or editorial practice are heterogeneous. If fewer than five suitable
comparators exist, record the shortfall and use the closest defensible article
type or specialty-journal comparators without hiding the substitution.

Create `01b_acceptance_tolerance_card.json` and record for every comparator:

- citation, DOI or stable URL, publication date, and article type;
- study design and actual biological unit of inference;
- cohort or experiment scale;
- internal, external, orthogonal, or absent validation;
- acknowledged limitations and unavailable analyses;
- wording used for association, prediction, mechanism, causality, or utility;
- data/code restrictions and the access mechanism, if any;
- public peer-review evidence when available;
- why the paper is comparable and where it is not.

Use these top-level fields:

```text
target_journal
article_type
accessed_at
status
comparators
substitution_reason
synthesis
```

Each comparator object must contain:

```text
id
citation
url
publication_date
journal
article_type
match_level
design
unit_of_inference
scale
validation
limitations
claim_ceiling
data_code_access
comparability_notes
```

Use `EXACT_JOURNAL_AND_TYPE`, `EXACT_JOURNAL_ADJACENT_TYPE`, or
`ADJACENT_JOURNAL_AND_TYPE` for `match_level`. The `synthesis` object contains
`mandatory_official_requirements`, `validity_floor`,
`competitiveness_expectations`, `accepted_with_limitations`,
`optional_strengthening`, and `calibration_boundary`.

Summarize observed practice as:

- `MANDATORY_OFFICIAL_REQUIREMENT`
- `VALIDITY_FLOOR`
- `COMPETITIVENESS_EXPECTATION`
- `ACCEPTED_WITH_LIMITATION`
- `OPTIONAL_STRENGTHENING`

Do not infer acceptance rates or guarantee that a similar limitation will be
accepted again.

Validate the card before reviewer dispatch:

```bash
python3 "$SKILL_ROOT/scripts/validate_acceptance_tolerance.py" \
  01b_acceptance_tolerance_card.json
```

The validator requires at least five comparator records for `PASS`. When fewer
than five are exact journal-and-article-type matches, record a specific
`substitution_reason`; never conceal adjacent-type or adjacent-journal evidence
as an exact comparator.

## Blocking test

Before labeling a scientific concern `BLOCKING`, ask:

> After accurate claim narrowing and transparent limitation disclosure, would
> the central inference remain valid and the manuscript remain a defensible
> submission to this target?

- If yes, the issue is not `BLOCKING`. Classify it as correctable, an acceptable
  inherent limitation, optional strengthening, or a journal-positioning risk.
- If no, identify the exact invalid inference or mandatory requirement that
  remains unsatisfied and anchor it to located manuscript evidence.
- If the available material cannot answer the question, use `NOT_ASSESSABLE`.

Do not require a new trial, cohort, assay, or experiment merely because it would
make the paper stronger. Scope-changing work is required only when the current
central claim cannot remain defensible without it. Otherwise use claim
narrowing, limitation disclosure, justified non-action, or retargeting.

## Four finding classes

Use exactly one class for every ledger concern:

| Class | Meaning |
|---|---|
| `FATAL_VALIDITY_FLAW` | The central inference remains invalid after honest claim narrowing; the current study has no defensible remedy. |
| `CORRECTABLE_BEFORE_SUBMISSION` | A concrete analysis, report, citation, wording, or package correction can resolve the concern. |
| `ACCEPTABLE_INHERENT_LIMITATION` | The limitation is real but the bounded manuscript remains defensible when it is disclosed and not overgeneralized. |
| `OPTIONAL_STRENGTHENING` | The work would improve competitiveness or future certainty but is not required for the current bounded manuscript. |

Scientific integrity, ethics, fabrication, retracted affirmative evidence,
unit-of-analysis errors, leakage, unreconciled data contradictions, and an
unsupported central claim remain non-negotiable. Editorial preference or the
absence of ideal evidence is not equivalent to one of those defects.
