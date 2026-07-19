# Biomedical review gates

Load only the sections that match the manuscript. These are internal review
prompts, not claims about a journal's official checklist. Official instructions
and field-specific reporting standards remain authoritative.

For every applicable gate, report `PASS`, `FAIL`, or `NOT ASSESSABLE`, cite the
manuscript location, explain the consequence, and define a resolution test.

## Universal claim gate

For each central conclusion:

1. identify the exact population, system, exposure or intervention, comparator,
   outcome, and time frame
2. identify the design and evidence layer supporting it
3. separate observation, association, prediction, mechanism, and causation
4. check whether validation is internal, external, orthogonal, or absent
5. lower the claim ceiling when the design cannot support the wording

## Clinical cohort and trial manuscripts

Check:

- cohort assembly, inclusion/exclusion, attrition, and analysis population
- endpoint definitions, assessment windows, censoring, and competing risks
- allocation, blinding, protocol deviations, missingness, and multiplicity
- sample-size rationale and event count relative to model complexity
- covariate selection, confounding control, immortal-time and selection bias
- calibration, discrimination, clinical utility, and external validation
- adverse events and clinically meaningful effect sizes, not only P values
- registration, protocol/SAP consistency, ethics, consent, and data access

Do not treat retrospective adjustment as equivalent to randomization.

## Biomarker, diagnostic, and prognostic studies

Check:

- intended use, target population, index test, reference standard, and threshold
- pre-analytic variables, batch effects, assay failure, and blinded assessment
- discovery/validation separation and leakage-free feature selection
- locked cutoffs versus data-derived cutoffs
- sensitivity, specificity, predictive values, likelihood ratios, and intervals
- calibration and decision utility at clinically plausible prevalence
- incremental value over a prespecified clinical baseline
- independent external validation at the intended-use setting

Do not call a correlated marker clinically useful without decision-relevant
validation.

## Wet-lab mechanism studies

Check:

- perturbation specificity, dose, timing, biological replicates, and controls
- orthogonal perturbations, rescue, gain/loss symmetry, and target engagement
- cell-line provenance, contamination/mycoplasma controls, and model diversity
- causal ordering between pathway events and phenotype
- quantification, blinding, randomization, replicate definition, and exclusions
- in vitro versus in vivo evidence boundaries
- whether a proposed mechanism is direct, indirect, or merely consistent

Expression change alone does not establish pathway dependence or mechanism.

## Bulk, single-cell, and spatial omics

Check:

- patient/sample count separately from cells, spots, fields, or technical units
- batch structure, paired design, repeated measures, and pseudoreplication
- QC thresholds, normalization, covariates, doublets/ambient signal, and outliers
- annotation evidence and uncertainty
- differential testing at the correct biological unit
- integration choices and whether biological signal was over-corrected
- spatial neighborhood definition, field selection, and tissue-area comparability
- multiple testing, effect sizes, robustness analyses, and independent validation
- code, processed data, raw data, seeds, environments, and accession readiness

Thousands of cells do not replace an adequate number of independent patients.

## AI and computational-method manuscripts

Check:

- task definition, data provenance, labels, leakage, and split independence
- patient/site/time-level separation and external-domain validation
- baseline selection, ablations, uncertainty, calibration, and failure analysis
- hyperparameter selection and whether the test set remained untouched
- class imbalance, subgroup performance, and clinically relevant operating points
- reproducible code, environment, model weights, and preprocessing
- interpretability claims versus post-hoc association
- comparison fairness, compute budget, and statistical uncertainty

High internal cross-validation performance is not external clinical validity.

## Systematic reviews and meta-analyses

Check:

- protocol/registration, eligibility criteria, search reproducibility, and dates
- duplicate screening/extraction and conflict resolution
- risk-of-bias method appropriate to included designs
- effect-measure compatibility and unit-of-analysis handling
- heterogeneity, prediction intervals, sensitivity analyses, and small-study bias
- duplicate cohorts, overlapping datasets, selective reporting, and certainty
- whether synthesis is justified when studies are clinically or methodologically
  incompatible

Publication count is not evidence quality.

## Animal and translational studies

Check:

- model relevance to the human claim and explicit translational boundary
- sex, age, strain, housing, randomization, blinding, exclusions, and welfare
- biological unit, litter/cage effects, sample-size rationale, and attrition
- exposure equivalence, pharmacokinetics, target engagement, and toxicity
- replication across models and validation in human material when claimed
- whether surrogate endpoints support the stated clinical implication

An animal phenotype does not by itself demonstrate human therapeutic efficacy.
