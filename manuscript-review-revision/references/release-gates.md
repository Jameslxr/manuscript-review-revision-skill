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
| scientific claims and evidence |  |  |  |  |
| methods, statistics, reproducibility |  |  |  |  |
| reference reality and integrity |  |  |  |  |
| exact claim-citation support |  |  |  |  |
| figure/table/supplement integration |  |  |  |  |
| reporting, ethics, and declarations |  |  |  |  |
| journal-specific manuscript format |  |  |  |  |
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
- a material scientific claim remains unsupported after claim narrowing and
  transparent limitation disclosure;
- a fatal validity, integrity, ethics, unit-of-analysis, leakage, or
  unreconciled data contradiction remains;
- tier-A or tier-B citation integrity or exact support remains unresolved;
- figures, legends, tables, supplements, or source data conflict;
- required ethics, reporting, registration, data/code, authorship, funding, or
  COI material is missing, without an allowed restriction or access mechanism;
- the clean manuscript failed structural or rendered visual QA;
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
