# Post-optimization independent evaluation

## Result

The post-run package detects all 18 sealed answer-key issues under the strict core-defect rule: `G01;G02;G03;G04;G05;G06;G07;G08;G09;G10;G11;G12;G13;G14;G15;G16;G17;G18`.

- Raw recall: 18/18 = 100%.
- Weighted recall: 42/42 = 100%, contributing 30/30 rubric points.
- Unsupported affirmative concerns: 0.
- Detection-level precision given the specified unsupported-concern rule: 18/(18+0) = 100%.
- Total score: 100/100.

Correct `NOT ASSESSABLE` boundaries were not counted as unsupported concerns. In particular, the package does not assert that approvals were absent, that off-target effects occurred, that full cited papers lack support, or that unseen figures and source outputs contain a specific defect.

## Rubric rationale

| Dimension | Score | Rationale |
|---|---:|---|
| Ground-truth concern recall | 30/30 | All 18 answer-key defects are stated at the core-defect level, including the low-weight figure-unit issue and both citation mismatches. |
| Precision and non-invention | 20/20 | No affirmative packet-unsupported defect, result, misconduct claim, or external fact was identified. Conditional risks and unavailable evidence are labeled as such. |
| Claim/evidence traceability | 15/15 | Stable concern IDs, normalized issue IDs, claim pointers, evidence pointers, evidence status, and cross-review mappings make every scored detection auditable. |
| Resolution-test quality | 10/10 | Closure tests are concrete and proportionate: nested or external validation, patient-aware inference with FDR, rescue and orthogonal perturbation, a factorial anti-PD-1 interaction, censoring-aware performance, governance identifiers, and reproducibility deposits. |
| Consensus and internal consistency | 10/10 | Consensus is claimed only for convergent issues; unique issues remain marked unique; there are no disagreement claims or material factual drifts across the ledger, matrix, and verdict. |
| Journal calibration | 10/10 | The review applies Nature’s outstanding-importance and interdisciplinary-interest bar, separates scientific invalidity from journal breadth, and avoids pretending to make the editor’s final decision. |
| Reproducibility and auditability | 5/5 | Inputs and reports are hashed, reviewer receipts and independence are recorded, runs and artifacts are distinguishable, and the ledger and matrix are machine-checkable. |

No points were awarded for length.

## Operational metrics and budget audit

- Raw-review word-equivalent total: 8,379 units across six reviewer reports, excluding synthesis.
- Concern count: 36.
- Normalized issue count: 18.
- Concern-to-issue ratio: 2.00.
- Maximum pair overlap: 0.75 (75%), above the 0.35 target.
- Final verdict size: 450 word-equivalent units.
- Schema budgets: passed. Every reviewer remained at or below 8 concerns, 1,800 word-equivalent units, 6 BLOCKING+MAJOR concerns, and 2 MINOR+EDITORIAL concerns. The journal-profile, panel, and concern-ledger validators all report `PASS`.

## Remaining duplication and usability limitation

The package is scientifically complete but still expensive to read: 8,379 raw-review units collapse 36 concerns into 18 normalized issues, and the maximum reviewer-pair overlap is 75%. The 450-unit final verdict is usable as an entry point, and the 2.00 concern-to-issue ratio shows successful normalization, but ten overlap warnings remain. The most repeated central topics are universality, actionability, EVA1 causality, and the missing EVA1-by-anti-PD-1 interaction. Further usability gains should come from reducing repeated exposition in role reports or routing readers directly to normalized issues, not from deleting independent support for distinct answer-key defects.

## Scientific coverage after optimization

Against the sealed answer key, scientific coverage was preserved: all 18 issues and all 42 issue-weight units remain detected, with zero unsupported affirmative concerns. This is an answer-key-based post-run conclusion; no baseline output or prior evaluation was inspected, so it is not a direct baseline-to-post comparative claim.
