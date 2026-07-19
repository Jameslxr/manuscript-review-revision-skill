# Independent multi-agent review

## Panel contract

Run at least five actual reviewer agents plus a root orchestrator. The root creates factual intake material and synthesizes after all reports finish; it is not counted as one of the five.

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

For high-tier or figure-heavy work add:

6. `figure-narrative-reporting`: figure-text-legend-source closure, article architecture, reporting and compliance

Add an adversarial reviewer when the central claim depends on a fragile causal chain, external validation, clinical utility, or a contested novelty claim.

These are functional lenses, not claims about real human identities, institutions, seniority, or confidential editor knowledge.

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

## Review completion rule

The panel is complete only when:

- at least five independent reports exist
- every required role is covered
- every report uses the same frozen input hashes
- every reviewer has a unique host task receipt and a verified report hash
- no reviewer saw another review before submission
- all `NOT ASSESSABLE` boundaries are retained
- every actionable finding appears in the validated concern ledger
- synthesis was created only after independent reports completed

Then return one posture and pause before revision.
