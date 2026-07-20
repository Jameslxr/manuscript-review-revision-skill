# Independent multi-agent review

## Panel contract

Run exactly five core reviewer agents plus a root orchestrator. The root
creates factual intake material and synthesizes after all reports finish; it is
not counted as one of the five. Add no more than one optional sixth reviewer.
Choose that seat from the highest-risk unresolved trigger rather than adding
every potentially useful lens.

Use the host's real non-fork subagent/delegation tool when available. In Codex,
use independent collaboration/subagent tasks. In Claude Code, use normal
`Agent` subagents with fresh contexts rather than forks that inherit the parent
conversation. With a four-slot limit, run three reviewers in wave 1 and the
remaining reviewers in wave 2. Preserve independence across waves: later
reviewers receive no earlier conclusions.

If agent tools are unavailable or fewer than five reviewer runs complete, label the gate `NOT ASSESSABLE`. Do not rename five sections written by one model as five agents.

## Shared input package

Give every reviewer:

- exact manuscript path and SHA-256
- exact journal-profile path and SHA-256
- article type and submission stage
- input inventory
- a factual, non-evaluative shared fact base
- one functional review role and its rubric
- the common report contract

Do not include another reviewer's report, the expected verdict, suspected defects, planned fixes, or root conclusions. Prefer a fresh context for each reviewer.

After dispatch, record each real host-provided Agent task ID in the panel plan.
For every task, also record the receipt source, fresh-context mode, start/end
timestamps, frozen-input hashes, report path, and report SHA-256. If the host
does not expose a task identity or equivalent execution log, mark the panel
receipt `NOT ASSESSABLE`; do not substitute a self-assigned label.

The receipt validator checks recorded host identity and artifact closure. It
does not cryptographically prove what happened inside a proprietary host.

## Required core roles

1. `journal-priority`: scope, article type, contribution threshold, audience, desk-screen risks
2. `domain-science`: disease/field correctness, biological interpretation, novelty versus prior work
3. `study-design`: clinical, mechanistic, omics, biomarker, AI, systematic-review, or other design-specific validity
4. `statistics-reproducibility`: replicates, sample size, tests, multiplicity, leakage, robustness, data/code reproducibility
5. `claim-evidence-reference`: claim ceilings, exact evidence, citations, contradictory evidence, limitations

For high-tier or figure-heavy work, the one optional seat may be:

6. `figure-narrative-reporting`: figure-text-legend-source closure, article architecture, reporting and compliance

Alternatively, select `adversarial-review` when the central claim depends on a
fragile causal chain, external validation, clinical utility, or a contested
novelty claim. Do not add both. If both triggers are present, choose the trigger
most likely to change the overall verdict and assign the secondary lens to the
closest core role.

These are functional lenses, not claims about real human identities, institutions, seniority, or confidential editor knowledge.

## Axis ownership and output budget

Before dispatch, classify every internal review axis as applicable and assign
each applicable axis to exactly one primary role in
`review_policy.axis_owners`. Copy each role's owned axes into its
`primary_axes` receipt field. This ownership map controls who is responsible
for coverage; it does not tell reviewers what conclusion to reach.

Each reviewer may return:

- no more than eight prioritized concerns;
- no more than 1,800 word-equivalent units;
- findings from its primary axes; and
- an out-of-role finding only when it is independently judged `BLOCKING`.

Do not spend the budget repeating a non-blocking concern owned by another role.
Use `NOT APPLICABLE` for an axis that truly does not apply and `NOT ASSESSABLE`
for an applicable axis that cannot be judged from supplied material. The root
must not hide a missing primary-axis assessment by asking another role to fill
it after reviews are exposed.

## Dynamic role selection

Replace the generic `study-design` lens with the closest manuscript-specific role:

| Manuscript | Specialist lens |
|---|---|
| clinical cohort/trial | clinical design, endpoint, confounding, generalizability |
| biomarker/prediction | TRIPOD/REMARK, leakage, calibration, external validation, utility |
| wet-lab mechanism | perturbation logic, controls, causality, rescue, orthogonal validation |
| bulk/single-cell/spatial omics | preprocessing, batch effects, unit of inference, annotation, validation |
| systematic/scoping review | search coverage, selection, extraction, proof distance, synthesis bias |
| meta-analysis | eligibility, risk of bias, heterogeneity, sensitivity, publication bias |
| AI/methods | splits, leakage, baselines, ablation, calibration, external testing, reproducibility |

## Common report contract

Each reviewer returns:

```text
Reviewer role
Material inspected and assessment boundary
Journal standard applied
Overall assessment
Major strengths
BLOCKING issues
MAJOR issues
MINOR issues
EDITORIAL issues
Claim-ceiling risks
Required versus optional additional work
Journal-fit posture
NOT ASSESSABLE items
Evidence anchors
Confidence and reasons
```

Every issue must include a manuscript anchor: section, quoted phrase, figure, table, supplement, or stable paragraph identifier. Never invent line numbers. Separate work required to establish the claim from optional work that merely strengthens presentation.

Order concerns by consequence. Return at most six `BLOCKING` or `MAJOR`
concerns and use the remaining budget for no more than two `MINOR` or
`EDITORIAL` concerns. If more issues exist, state the omitted count and the
selection rule without listing additional disguised concerns.

Each reported issue must be transferable to `reviews/concern_ledger.tsv` with
a unique concern ID, a cross-review issue key, review axis, severity, exact
claim/evidence pointers, confidence, and a concrete resolution test. Use the
controlled vocabulary in `concern-ledger-and-adjudication.md`.

## Synthesis

After all reports finish, build a cross-review matrix with:

- issue ID
- reviewers raising it
- severity
- manuscript evidence anchor
- consensus or disagreement
- root adjudication
- required action
- gate affected

Do not decide by majority vote alone. A single well-grounded blocking issue can control the outcome. Do not average away a genuine disagreement; state what evidence would resolve it.

Assign `CONSENSUS` only when at least two independent reviewers raised the same
underlying issue. Preserve `DISAGREEMENT` as an explicit state. Treat pairwise
issue-key overlap above 35% as a role-duplication warning, not a command to
invent reviewer diversity.

One normalized issue receives one row in the cross-review matrix even when
several reviewers raised it. Keep the author-facing verdict below 900
word-equivalent units and link it to the ledger instead of reproducing every
review.

## Review completion rule

The panel is complete only when:

- at least five independent reports exist
- every required role is covered
- every report uses the same frozen input hashes
- every reviewer has a unique host task receipt and a verified report hash
- no reviewer saw another review before submission
- all `NOT ASSESSABLE` boundaries are retained
- every actionable finding appears in the validated concern ledger
- no reviewer exceeds eight ledger concerns or 1,800 word-equivalent units
- each `PRIMARY` concern follows the preassigned axis owner
- any `BLOCKING_CROSSOVER` concern is actually `BLOCKING`
- synthesis was created only after independent reports completed

Then return one posture and pause before revision.
