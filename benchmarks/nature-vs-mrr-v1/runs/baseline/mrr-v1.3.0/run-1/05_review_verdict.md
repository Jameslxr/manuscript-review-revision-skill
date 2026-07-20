# Scientific review verdict

## Posture

`MAJOR_SCIENTIFIC_REWORK_REQUIRED`

The manuscript is not scientifically ready for submission as a Nature Article. This is not a language, formatting, or presentational problem: the current designs do not identify the central clinical, causal, or treatment-response conclusions. A narrower exploratory manuscript could be considered for a more specialized venue after claims are corrected, but the present Nature claim architecture requires new analysis, independent validation, and redesigned experiments.

## Controlling blockers

1. **The five-gene score has no independent validation.** Feature selection, coefficient directions, cutoffs, and missing-data rules used all 72 patients before the same cohort was split 70:30. The nominal validation subset is outcome-informed. The full pipeline must be redeveloped without leakage and tested once in a genuinely untouched, adequately powered external cohort.
2. **Clinical actionability and anti-PD-1 treatment selection are not tested.** A retrospective single-centre resection cohort with overall survival cannot identify benefit from anti-PD-1, support a score-by-treatment interaction, or establish universal use across HCC aetiologies and settings.
3. **Anti-PD-1 sensitization is not estimable.** All ten mice received anti-PD-1, so the experiment lacks the untreated arms required to estimate an EVA1-by-treatment interaction. A randomized, blinded, powered factorial study with immune readouts and independent replication is required.
4. **EVA1-specific immune causality is not established.** One CRISPR guide, no rescue or orthogonal perturbation, no direct target-engagement assay, and no immune-effector system cannot distinguish an on-target immune mechanism from guide-specific or general growth effects.
5. **The single-cell discovery uses the wrong biological unit.** Cell-level Wilcoxon testing across eight patients, with cells treated as independent and no multiple-testing correction, does not support patient-level discovery. Patient-aware inference, multiplicity control, and independent replication are required.
6. **The headline three-year result is internally incoherent.** The Abstract, Results, and Figure 3 legend report AUC values of 0.91, 0.84, and 0.86, respectively, while median follow-up among survivors is 18 months. One frozen, censoring-aware analysis with risk-set support and uncertainty is required.
7. **The analysis is not reproducible from the supplied report.** The exact score, coefficients, raw/processed single-cell data, final analysis data, code, seeds, software versions, and figure source data are unavailable.

## Major additional issues

- The survival model is fragile relative to 31 deaths and extensive candidate selection; proportional-hazards diagnostics, confidence intervals, missingness analysis, calibration, and comparison with BCLC or other prespecified clinical baselines are absent.
- The mouse experiment uses cage-order allocation, unblinded measurement, five animals per group, a single day-21 test, and no independent replicate.
- The manuscript does not directly connect the five-gene score, EVA1 state, immune phenotype, survival, and treatment effect into one causal chain.
- The two-reference literature foundation is inadequate for exhaustive novelty and treatment-selection claims. Exact claim support requires a separate cited-paper full-text audit.
- Human and animal ethics reporting lacks committee/protocol identifiers, consent procedure, animal protocol, and humane endpoints.

## Cross-review adjudication

There were **no material reviewer disagreements**. The validated ledger contains 94 concerns normalized to 25 issues, including 17 consensus issues and 8 unique issues. The highest pairwise issue-key overlap was 88%, a validator warning that reflects strong convergence on the same central defects; it is not treated as additional evidence by vote count.

Material unique findings were retained rather than averaged away: the journal-priority reviewer’s Nature contribution-threshold failure is controlling; the xenograft host/antibody immune suitability remains `NOT ASSESSABLE`; and the domain reviewer’s concern that generic growth effects may explain the apparent immune phenotype remains an independent mechanistic alternative.

## Nature calibration

Nature requirement N001 calls for original research of outstanding scientific importance with a conclusion of interdisciplinary interest. The study has a potentially coherent translational concept, but the current evidence is a single-centre retrospective association plus preliminary cell-line and xenograft observations. It does not meet the broad-flagship threshold for independent multi-layer validation, causal completeness, universal clinical consequence, or reproducible methods. The panel does not predict acceptance or make an editorial decision.

## NOT ASSESSABLE boundaries

- Figure images, tables, source data, and raw outputs were not supplied; figure quality and numerical source reconciliation are `NOT ASSESSABLE`.
- Cited-paper full text was outside this scientific-review run; exact semantic citation support is `NOT ASSESSABLE`.
- The existence and adequacy of underlying human approvals, consent, animal approval, and humane endpoints are `NOT ASSESSABLE`; their omission from the manuscript is an assessable reporting failure.
- Mouse host strain/immune status and anti-PD-1 reagent compatibility were not reported; checkpoint-model suitability is `NOT ASSESSABLE`.
- Unreported experiments or procedures were not presumed absent unless the manuscript explicitly stated they were not performed.

## Authorization pause

The manuscript remains read-only. No revision, polishing, reference replacement, formatting, or submission-package work has been performed.

**Pause here. Scientific revision may begin only after explicit author authorization.**
