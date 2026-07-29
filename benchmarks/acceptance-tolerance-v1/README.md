# Acceptance-tolerance calibration audit v1

This bounded audit tests whether the Skill's review rules mistake ideal study
features for universal publication requirements. It is calibration evidence,
not a systematic review, an acceptance-rate study, or proof that every
published conclusion is correct.

## Corpus and method

- 24 recent open-access HCC/iCCA papers were stratified across four editorial
  classes: broad flagship, top specialty, strong specialty, and
  soundness-focused (six per class).
- Full JATS text was inspected for design boundaries, validation, explicit
  limitations, claim wording, and data/code restrictions.
- Public peer-review files were additionally inspected for four Nature
  Communications papers: PMC10928173, PMC11021407, PMC11065883, and
  PMC11327344.
- Current official journal and reviewer guidance was checked separately. It
  remains authoritative over this observed-practice sample.

## Frozen paper set

| Class | Journal | Year | Record |
|---|---|---:|---|
| broad flagship | Nature Medicine | 2024 | [PMC10957471](https://pmc.ncbi.nlm.nih.gov/articles/PMC10957471/) |
| broad flagship | Nature Medicine | 2024 | [PMC11031401](https://pmc.ncbi.nlm.nih.gov/articles/PMC11031401/) |
| broad flagship | Nature Communications | 2024 | [PMC10928173](https://pmc.ncbi.nlm.nih.gov/articles/PMC10928173/) |
| broad flagship | Nature Communications | 2024 | [PMC11021407](https://pmc.ncbi.nlm.nih.gov/articles/PMC11021407/) |
| broad flagship | Nature Communications | 2024 | [PMC11065883](https://pmc.ncbi.nlm.nih.gov/articles/PMC11065883/) |
| broad flagship | Nature Communications | 2024 | [PMC11327344](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327344/) |
| top specialty | Gut | 2024 | [PMC11874287](https://pmc.ncbi.nlm.nih.gov/articles/PMC11874287/) |
| top specialty | Journal of Hepatology | 2025 | [PMC12086051](https://pmc.ncbi.nlm.nih.gov/articles/PMC12086051/) |
| top specialty | Hepatology | 2024 | [PMC12356563](https://pmc.ncbi.nlm.nih.gov/articles/PMC12356563/) |
| top specialty | Hepatology | 2024 | [PMC12356573](https://pmc.ncbi.nlm.nih.gov/articles/PMC12356573/) |
| top specialty | Hepatology | 2024 | [PMC12077336](https://pmc.ncbi.nlm.nih.gov/articles/PMC12077336/) |
| top specialty | Gut | 2024 | [PMC11420749](https://pmc.ncbi.nlm.nih.gov/articles/PMC11420749/) |
| strong specialty | JHEP Reports | 2025 | [PMC12478257](https://pmc.ncbi.nlm.nih.gov/articles/PMC12478257/) |
| strong specialty | JHEP Reports | 2025 | [PMC12800505](https://pmc.ncbi.nlm.nih.gov/articles/PMC12800505/) |
| strong specialty | JHEP Reports | 2025 | [PMC12657762](https://pmc.ncbi.nlm.nih.gov/articles/PMC12657762/) |
| strong specialty | JHEP Reports | 2026 | [PMC12926642](https://pmc.ncbi.nlm.nih.gov/articles/PMC12926642/) |
| strong specialty | Clinical and Translational Medicine | 2024 | [PMC11131356](https://pmc.ncbi.nlm.nih.gov/articles/PMC11131356/) |
| strong specialty | ESMO Open | 2025 | [PMC12514508](https://pmc.ncbi.nlm.nih.gov/articles/PMC12514508/) |
| soundness-focused | PLOS ONE | 2025 | [PMC12360567](https://pmc.ncbi.nlm.nih.gov/articles/PMC12360567/) |
| soundness-focused | BMC Cancer | 2025 | [PMC12066050](https://pmc.ncbi.nlm.nih.gov/articles/PMC12066050/) |
| soundness-focused | BMC Cancer | 2025 | [PMC12100895](https://pmc.ncbi.nlm.nih.gov/articles/PMC12100895/) |
| soundness-focused | Frontiers in Oncology | 2025 | [PMC11933651](https://pmc.ncbi.nlm.nih.gov/articles/PMC11933651/) |
| soundness-focused | Scientific Reports | 2025 | [PMC11994744](https://pmc.ncbi.nlm.nih.gov/articles/PMC11994744/) |
| soundness-focused | Scientific Reports | 2024 | [PMC11375009](https://pmc.ncbi.nlm.nih.gov/articles/PMC11375009/) |

## Observed calibration signals

- The extraction identified an explicit limitation paragraph or equivalent in
  19 of 24 papers. This is a corpus observation, not an estimate for the
  journals as a whole.
- Accepted papers included small or single-arm early-phase trials, exploratory
  biomarker analyses, retrospective cohorts, absent external validation,
  incomplete planned analyses, and restricted data access.
- Their acceptability depended on what the paper claimed. Authors commonly
  narrowed causal or comparative language, labeled analyses exploratory,
  disclosed unresolved limitations, and reserved confirmation for future work.
- The public peer-review files showed a mixture of added analyses, clearer
  reporting, claim narrowing, justified non-action, and scope control. Reviewers
  did not require every theoretically stronger experiment before acceptance.

## Changes motivated in version 1.5.0

1. Journal-tier features are expectations, not universal admission checklists.
2. Every concern is classified as a fatal flaw, correctable issue, acceptable
   inherent limitation, or optional strengthening.
3. `BLOCKING` requires failure of the claim-narrowing and transparent-limitation
   test.
4. Reference auditing is risk-tiered so that incomplete low-consequence context
   sampling cannot block verified material claims.
5. Manuscript readiness is separated from five-Agent workflow assurance.

## Boundary

Publication precedent never overrides ethics, integrity, unit-of-analysis,
leakage, data contradiction, retraction, or unsupported central-claim gates.
This sample is liver-cancer-heavy, open-access-only, and publication-selected;
future calibration should add other fields, article types, rejected manuscripts
when legitimately available, and prospective repeat runs.
