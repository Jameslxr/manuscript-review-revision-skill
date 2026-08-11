# Fail-closed release gates

## Required statuses

Use only `PASS`, `FAIL`, or `NOT ASSESSABLE` for critical gates. Missing
evidence is not a pass. Keep manuscript readiness separate from workflow
assurance so that a host limitation is never mislabeled as a scientific flaw.

## Manuscript-readiness gates

Report:

| Gate | Status | Evidence inspected | Blocking defects | Required correction |
|---|---|---|---|---|
| release-candidate integrity |  |  |  |  |
| current journal profile |  |  |  |  |
| source-linked journal format plan |  |  |  |  |
| scientific claims and evidence |  |  |  |  |
| methods, statistics, reproducibility |  |  |  |  |
| reference reality and integrity |  |  |  |  |
| exact claim-citation support |  |  |  |  |
| figure/table/supplement integration |  |  |  |  |
| reporting, ethics, and declarations |  |  |  |  |
| journal-specific manuscript format |  |  |  |  |
| combined DOCX format release |  |  |  |  |
| submission-package DOCX format release |  |  |  |  |
| all-delivered-DOCX receipt and hash closure |  |  |  |  |
| rendered visual QA |  |  |  |  |
| submission-package completeness |  |  |  |  |

## Workflow-assurance gates

Report separately:

| Gate | Status | Evidence inspected | Assurance limitation | Required action |
|---|---|---|---|---|
| five-agent independent review |  |  |  |  |
| required post-revision re-review |  |  |  |  |
| task receipts and frozen-artifact closure |  |  |  |  |

An unavailable fifth reviewer, missing host task identity, or incomplete
adversarial re-review makes workflow assurance `NOT ASSESSABLE`. It does not by
itself make the manuscript scientifically invalid. The overall release remains
`RELEASE NOT ASSESSABLE` until the promised assurance is completed, while the
manuscript-readiness result is still reported independently.

## State distinctions

Keep separate:

- `author-readable`
- `coauthor-review-ready`
- `submission-system-ready`
- `production-ready`

A polished DOCX, clean render, complete review report, or successful specialist
script cannot alone establish submission readiness.

## Mandatory manuscript blockers

Return `RELEASE FAIL` when:

- manuscript components are not demonstrably the same version;
- a mandatory official journal rule or article type is known and unmet;
- the format plan does not match the current journal profile hash, article
  type, submission stage, or release-candidate manuscript;
- a required format-plan category is missing or `NOT_ASSESSABLE` while the
  package is presented as journal-specific;
- a material scientific claim remains unsupported after claim narrowing and
  transparent limitation disclosure;
- a fatal validity, integrity, ethics, unit-of-analysis, leakage, or
  unreconciled data contradiction remains;
- tier-A or tier-B citation integrity or exact support remains unresolved;
- figures, legends, tables, supplements, or source data conflict;
- required ethics, reporting, registration, data/code, authorship, funding, or
  COI material is missing, without an allowed restriction or access mechanism;
- any delivered DOCX uses paragraph spacing in place of the required literal
  empty paragraphs, has unclassified non-empty paragraph styles, omits
  continuous Word-native line numbering in any section, suppresses line
  numbers, omits a dynamic page number on any active page story, restarts page
  numbering, or failed whole-document structural/rendered visual QA;
- any manuscript DOCX has unresolved or decorative front matter, uses centered
  or mixed-alignment title-block roles without a current source-linked
  override, uses undersized author/affiliation/declaration text, mixes line
  spacing across manuscript roles, lacks or duplicates any required semantic
  front-matter block blank, inserts a blank inside a multi-paragraph
  front-matter role, leaves an author note or ORCID block unclassified,
  inserts empty paragraphs between CRediT author entries, uses no recognized
  official role in a CRediT-labelled statement, has a non-bold Keywords label
  or an invalid section/Keywords/CRediT blank-line boundary, lacks the front-matter or
  semantic-rhythm audit, changes unauthorized text during formatting, or does
  not reach `FORMAT_RELEASE_PASS`;
- any editable cover letter, response letter, or other submission-package DOCX
  mixes fonts, sizes, line spacing, or paragraph spacing across roles; lacks
  the required natural blank boundaries, package audit, preservation check, or
  rendered-page review; or does not reach `PACKAGE_FORMAT_RELEASE_PASS`;
- any DOCX under the final delivery root lacks an exact receipt, current file
  hash, embedded profile normalizer, applicable passing release report, or the
  complete root scan does not reach `GENERATED_DOCX_RELEASE_PASS`;
- a revision changed core claims without the scientifically responsible
  re-review.

Do not fail release merely because a study lacks an ideal additional cohort,
mechanistic experiment, or public dataset. Apply the four finding classes and
the blocking test in
[evidence-calibration.md](evidence-calibration.md). A disclosed limitation that
leaves the bounded manuscript defensible is not a mandatory blocker.

## Final output

Report all three lines:

- `MANUSCRIPT READINESS: PASS | FAIL | NOT ASSESSABLE`
- `WORKFLOW ASSURANCE: PASS | NOT ASSESSABLE`
- `RELEASE PASS | RELEASE FAIL | RELEASE NOT ASSESSABLE`

Use `RELEASE PASS` only when both dimensions pass. Use `RELEASE FAIL` for a
known manuscript-readiness blocker. Use `RELEASE NOT ASSESSABLE` when readiness
or promised workflow assurance cannot be completed. List manuscript blockers
before optional improvements, and list workflow limitations separately. Never
predict acceptance.
