# A single-cell-derived immune-evasion signature establishes a universal therapeutic vulnerability in hepatocellular carcinoma

Synthetic benchmark manuscript — no real patients, authors, institutions, or
unpublished data are represented.

## Abstract

Hepatocellular carcinoma (HCC) remains a leading cause of cancer mortality, but
the mechanisms linking tumour-cell state to immune escape remain incompletely
defined. We integrated single-cell RNA sequencing from eight resected HCCs with
a retrospective clinical cohort of 72 patients treated at one centre. A
five-gene immune-evasion score separated patients with high and low overall
survival and achieved an area under the receiver operating characteristic curve
(AUC) of 0.91 for 3-year mortality. CRISPR depletion of the highest-ranked gene,
EVA1, reduced growth in two HCC cell lines and sensitized xenografts to
anti-PD-1 treatment. These findings establish EVA1 as the causal driver of
immune escape and demonstrate that our score is a clinically actionable,
universally applicable predictor for HCC.

## Impact and implications

Patients with HCC have heterogeneous responses to immunotherapy. This study
identifies a five-gene score that can be measured at diagnosis and used to
select anti-PD-1 therapy. The results provide an immediately deployable
biomarker and establish EVA1 inhibition as a treatment strategy for all major
HCC aetiologies.

## Introduction

HCC arises in diverse liver-disease settings and exhibits marked molecular and
immune heterogeneity. Existing clinical staging systems do not directly measure
tumour immune escape. Although several immune signatures have been reported,
none provides a universal, mechanistically validated guide to immunotherapy
selection.

We therefore combined single-cell discovery, retrospective survival modelling,
cell-line perturbation, and a mouse experiment. We hypothesized that a
tumour-cell immune-evasion programme would predict survival and identify a
therapeutic dependency. We report the first clinically actionable HCC immune
score derived from single-cell data and show that EVA1 directly controls
anti-tumour immunity.

## Patients and methods

### Study population

The clinical cohort included 72 adults who underwent resection for HCC at
Lakeside Medical Center between January 2018 and December 2022. The analysis
included 58 patients with viral hepatitis, 9 with metabolic liver disease, and
5 with other or undocumented aetiologies. Thirty-one deaths were observed.
Median follow-up among surviving patients was 18 months.

Available clinical variables included age, sex, aetiology, tumour size, tumour
number, alpha-fetoprotein, vascular invasion, histological grade, cirrhosis,
Child–Pugh class, albumin, bilirubin, platelet count, treatment after
recurrence, and recurrence status. Records with missing values were excluded
from each analysis. No prospective sample-size calculation was performed.

### Single-cell discovery

Single-cell RNA sequencing was performed on tumour and adjacent tissue from
eight patients in the clinical cohort. After filtering, 46,218 cells were
retained. Tumour cells were identified using epithelial markers and inferred
copy-number patterns. Differential expression between high- and low-infiltration
tumours was tested at the cell level using a Wilcoxon rank-sum test. Cells were
treated as independent observations. Genes with nominal P < 0.05 were retained;
no multiple-testing correction was applied.

### Score construction and validation

Twenty-seven genes selected from the single-cell comparison were entered into a
Cox regression model with the 18 available clinical and molecular covariates.
Five genes were retained after stepwise selection using the entire 72-patient
dataset. Expression cutoffs, coefficient signs, and missing-value rules were
also chosen using the full dataset.

The same 72 patients were then randomly divided 70:30 into a training set and a
validation set. The locked five-gene formula was evaluated in both subsets. No
external cohort, independent laboratory assay, calibration analysis, or
decision-curve analysis was used. Performance was compared only with the
five-gene model; BCLC stage and other clinical baselines were not evaluated.

### Functional experiments

EVA1 was depleted using one CRISPR guide RNA in Huh7 and Hep3B cells. Cell
growth was measured after 72 hours. Interferon-response transcripts and PD-L1
protein were measured in the same cultures. A non-targeting guide served as the
control. The study did not include a second guide, rescue construct, direct
target-engagement assay, or immune-cell co-culture.

### Mouse experiment

Ten mice bearing subcutaneous Huh7 xenografts were allocated to control or
EVA1-depleted cells, with five animals per group. All mice received anti-PD-1.
Allocation order followed cage order; investigators were aware of group
assignment during measurement. Tumour volume was compared on day 21 using an
unpaired t-test. No independent replicate experiment was performed.

### Statistical analysis

Continuous variables were compared using t-tests and categorical variables
using chi-squared tests. Overall survival was analysed with Kaplan–Meier curves
and Cox regression. The proportional-hazards assumption was not examined.
Hazard ratios and P values were reported without confidence intervals.
Nominal two-sided P < 0.05 was considered significant for all analyses.

## Results

### Single-cell discovery identifies an immune-evasion programme

The single-cell analysis identified 1,842 nominally significant genes between
high- and low-infiltration tumours. EVA1 was higher in low-infiltration tumours
and correlated inversely with a T-cell score (Spearman r = −0.41, P = 0.03).
We interpreted this association as evidence that EVA1 excludes T cells from HCC.

### The five-gene score predicts survival

The high-score group had shorter overall survival than the low-score group
(log-rank P = 0.02). The score remained significant in the selected multivariable
model (hazard ratio 2.4, P = 0.04). The Results text reports a validation-set
3-year mortality AUC of 0.84. Figure 3 reports an AUC of 0.86, whereas the
Abstract reports 0.91. Because median follow-up was 18 months, 3-year outcome
status was unavailable for many surviving patients.

### EVA1 perturbation supports a therapeutic mechanism

EVA1 depletion reduced 72-hour cell growth by 24% in Huh7 cells and 19% in
Hep3B cells. PD-L1 abundance also decreased, while three interferon-response
transcripts increased. These findings show that EVA1 directly suppresses
anti-tumour immunity.

In mice, day-21 tumours were smaller in the EVA1-depleted group (P = 0.048).
The experiment did not measure immune infiltration, survival, toxicity, or EVA1
expression after implantation. We conclude that EVA1 inhibition sensitizes HCC
to anti-PD-1 and is ready for therapeutic development.

## Discussion

This study establishes a universal immune-evasion mechanism in HCC and provides
a biomarker ready for clinical deployment. The score was validated in an
independent subset and therefore overcomes the limitations of earlier
single-centre signatures. Its high AUC supports immediate use for selecting
anti-PD-1 therapy.

The molecular and animal results identify EVA1 as the causal link between the
five-gene score and immune escape. Although the study used two cell lines and a
small xenograft experiment, concordance across data types demonstrates the
generality of the mechanism. Future prospective studies may refine, but are not
required to establish, clinical utility.

The study has limitations. The cohort was retrospective and most patients had
viral liver disease. We did not use an external cohort. Nonetheless, the
single-cell sample size and mechanistic experiments support application across
HCC aetiologies and treatment settings.

## Data and code availability

Processed summary tables can be requested from the corresponding author. Raw
single-cell data, model code, coefficient values, and the final patient-level
analysis dataset are not deposited. Random seeds and software versions were not
recorded.

## Ethics

The manuscript states that the study complied with institutional requirements.
The approving committee, protocol number, consent procedure, animal protocol,
and humane endpoints are not reported.

## Figure legends

**Figure 1.** Single-cell workflow and EVA1 expression across tumour-cell
clusters. Each point in the differential-expression panel represents one cell.

**Figure 2.** Association between EVA1 expression and the T-cell score in eight
tumours.

**Figure 3.** Development and validation of the five-gene mortality model.
Panel C labels the validation AUC as 0.86.

**Figure 4.** Cell growth and xenograft volume following EVA1 depletion.

## References

1. Cancer Genome Atlas Research Network. Comprehensive and integrative genomic
   characterization of hepatocellular carcinoma. *Cell*. 2017;169:1327–1341.
   doi:10.1016/j.cell.2017.05.046.
2. Finn RS, et al. Atezolizumab plus bevacizumab in unresectable hepatocellular
   carcinoma. *N Engl J Med*. 2020;382:1894–1905.
   doi:10.1056/NEJMoa1915745.

The Introduction cites reference 1 for the statement that no previous immune
signature has clinical utility. The Discussion cites reference 2 for the claim
that the five-gene score identifies patients who benefit from anti-PD-1
monotherapy.
