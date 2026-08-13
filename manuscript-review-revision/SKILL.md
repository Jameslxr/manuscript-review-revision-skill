---
name: manuscript-review-revision
description: |
  Run a review-first workflow for biomedical and scientific manuscripts using either a named target-journal route or a journal-neutral general-manuscript route. Support target-journal confirmation or recommendation, neutral high-standard review, official-guideline research, source-strength-aware typography and table resolution, source-linked format plans, five independent reviewers, scientific/statistical review, claim-reference verification, authorized revision and reviewer responses, DOCX/PDF formatting, and fail-closed release auditing. Enforce genuinely empty paragraphs with no spaces or tabs, zero paragraph spacing, semantic list rhythm, top-journal table presentation, one manuscript-wide line-spacing token, exact semantic front-matter block gaps, compact official-role CRediT blocks, body-sized semantic roles, left-aligned front matter, continuous Word line and page numbering, and rendered-page QA. Use for integrated review, revision, response, retargeting, submission preparation, neutral coauthor drafts, or journal-specific formatting. For format-only DOCX repair, prefer `manuscript-docx-formatting`. Fix the manuscript route before full review; never revise before the review gate and user authorization.
---

# Manuscript Review & Revision

## Operating contract

Treat review, revision, and formatting as separate phases. Use this non-negotiable order:

`manuscript route -> route profile -> conditional format/tolerance plan -> frozen input -> independent review -> synthesis -> user gate -> scientific revision -> reference/figure closure -> language -> formatting -> release gate`

- Keep the manuscript read-only through review.
- Do not turn a polished file into a submission-ready claim.
- Do not invent experiments, analyses, citations, journal rules, reviewer identities, line numbers, or completed changes.
- Use `PASS`, `FAIL`, or `NOT ASSESSABLE` for critical gates.
- Classify concerns as fatal flaws, correctable issues, acceptable inherent
  limitations, or optional strengthening; absence of ideal evidence is not an
  automatic blocker.
- Explain findings in the user's language while preserving exact manuscript text, filenames, identifiers, and journal wording.

## Global DOCX formatting invariant

Any mode that creates or modifies a DOCX must run this gate before delivery,
even when the requested change affects only one word, one sentence, one
reference, one comment, or one formatting property. This gate applies to the
entire output file, not only the edited paragraphs, and covers manuscripts,
tracked copies, clean copies, cover letters, response letters, and editable
supplementary text.

- Set effective body-prose `spaceBefore` and `spaceAfter` to `0 pt`.
- Remove or disable OOXML `beforeAutospacing` and `afterAutospacing` from body
  prose, its style chain, and empty separator paragraphs; displayed `0 pt`
  values alone are not sufficient.
- Insert exactly one structurally empty paragraph between adjacent body-prose
  paragraphs. Never simulate it with paragraph spacing or a manual line break.
- A blank paragraph must contain no spaces, tabs, nonbreaking spaces, or other
  whitespace-only text nodes. If a draft uses whitespace to simulate an empty
  line, delete that whitespace and retain one truly empty paragraph. Never keep
  both paragraph spacing and an empty paragraph.
- Give body prose and empty separators the explicit required line-spacing
  token; never inherit Word defaults and never disable the line-spacing check.
- For manuscripts, apply that same resolved token to title, authors,
  affiliations, author notes, correspondence, ORCID/identifiers, Keywords,
  every heading/subheading, and all declaration/CRediT paragraphs. These roles
  use the resolved body font size (12 pt fallback), except the title.
- Resolve table cells independently. Unless a binding/direct current source
  specifies otherwise, use 10 pt table-cell text with single line spacing and
  0/0 pt paragraph spacing; keep table titles/captions at the body size and
  manuscript line-spacing token.
- Resolve table presentation independently from table typography. Load
  [references/table-formatting.md](references/table-formatting.md). When no
  binding/direct current journal rule specifies another scheme, convert every
  editable table to the journal-neutral three-line profile: top rule,
  header-bottom rule, bottom rule, no vertical/internal body rules, no cell
  shading, bold repeating header row, top-aligned cells, and rendered-page QA.
  Do not invent or silently rewrite table data, units, statistics, titles, or
  notes; unresolved content defects fail the table gate.
- Resolve typography and line spacing from binding/direct official wording,
  not illustrative examples. `e.g.`, `for example`, `for instance`, and `such
  as` do not override the fallback. When no binding/direct rule exists, use
  Times New Roman, Title 15 pt bold, visible top-level manuscript text 12 pt,
  headings/subheadings 12 pt bold, table-cell text 10 pt, double line spacing
  outside tables, and single table-cell line spacing. Preserve supplied
  capitalization unless an official rule explicitly requires case.
- In a manuscript, place exactly one structurally empty Enter-created paragraph
  between every adjacent present front-matter block: Title, Authors,
  Affiliations, optional Author notes, Correspondence, optional ORCID/identifiers,
  and Abstract. Keep consecutive paragraphs within one role compact. Every
  separator uses `0/0 pt` and the resolved global line-spacing token; there is no
  journal/template bypass for this personal house-style invariant.
- Treat CRediT as a compact semantic block. Use recognized official role
  vocabulary, place no blank between its heading and first entry, and never
  insert empty paragraphs between consecutive author entries. Do not infer or
  rewrite author roles during format-only work.
- Bold only recognized `Keywords:` and inline declaration labels. Place no
  empty paragraph before Keywords, exactly one after Keywords and before each
  new section/subsection/declaration block, and none between a heading and its
  first body paragraph.
- Treat bullet and numbered lists as semantic blocks, not ordinary body-prose
  pairs. Keep a heading directly attached to its first item, use no blank
  paragraph between consecutive items or nested Key Points, and use at most one
  true empty paragraph around the list block when it meets surrounding prose.
- Enable Word-native line numbering in every section with `countBy=1` and
  `restart=continuous`. Remove paragraph-level `suppressLineNumbers`; no section
  or paragraph may opt out.
- Add a dynamic `PAGE` field to every active default, first-page, and even-page
  header/footer story. Keep page numbering continuous across sections; static
  typed numerals do not count.
- Inventory every non-empty top-level paragraph style. Pass every prose style
  with `--body-style` and every semantic non-body style with `--exclude-style`.
  If one style mixes prose with titles, lists, captions, or bibliography,
  restyle those roles before auditing.
- Run the gate on every delivered DOCX, including both tracked and clean
  copies. A one-paragraph edit does not permit a partial-document audit.
- If the gate fails, correct the DOCX automatically and rerun it. Do not
  deliver the file as complete and do not ask the user to repair Word spacing,
  line numbering, or page numbering.
- For a manuscript, normalize and audit title, authors, affiliations, author
  notes, correspondence, and ORCID/identifiers as semantic front-matter roles.
  Use restrained left-aligned journal-neutral defaults unless a current exact
  journal template records a different alignment rule. Do not guess roles from
  appearance or center a title block by default.
- Compare extracted text before and after formatting and render every page
  after the last layout-sensitive change. A mechanical XML pass alone is not a
  release.
- Combine the structural, front-matter, semantic-rhythm, content-preservation,
  journal, and rendered-page gates with `validate_format_release.py`. Every applicable gate
  must pass; `NOT_ASSESSABLE` is never promoted to pass.

```bash
python3 "$SKILL_ROOT/scripts/enforce_docx_line_page_numbers.py" \
  output.docx --out output.numbered.docx \
  --page-number-position upper-right

python3 "$SKILL_ROOT/scripts/audit_docx_manuscript_style.py" \
  output.numbered.docx --paragraph-separation literal-blank \
  --expected-line-spacing <resolved-token> \
  --body-style <each-prose-style> \
  --exclude-style <each-semantic-nonbody-style>
```

There is no journal-template bypass for this personal output invariant. If an
official template conflicts with literal empty paragraphs, continuous line
numbers, or continuous page numbers, preserve the user's DOCX construction,
report the journal-format conflict explicitly, and do not claim simultaneous
template compliance. This gate is a postcondition of DOCX writing; it does not
trigger scientific review, journal research, or `full-run`.

For a format-only request, the standalone sibling
`manuscript-docx-formatting` provides the same paragraph, spacing,
front-matter, line-number, page-number, preservation, rendered-page, and
combined release gates without loading this review workflow. This skill embeds
its own complete implementation for integrated review/revision runs and must
not import the sibling at runtime; keep both copies synchronized when a global
DOCX invariant changes.

## Mandatory embedded formatting dispatch

Load [references/generated-docx-release-contract.md](references/generated-docx-release-contract.md)
whenever any mode will write a DOCX. After the last content mutation, route
every final manuscript, tracked copy, clean copy, cover letter, response letter,
declaration, and editable supplement through the embedded profile normalizer,
numbering enforcer, content-preservation comparison, applicable audits,
full-page render inspection, and combined release validator. Never bypass this
dispatch because a source already looks formatted or the requested edit is
small. Any later DOCX write invalidates its earlier pass.

Keep final deliverables in one dedicated delivery root. Create a hash-bound
receipt for each final DOCX and run
`scripts/validate_generated_docx_release.py` over that root. Do not deliver any
DOCX unless the scan returns
`GENERATED_DOCX_RELEASE_PASS`; a missing file receipt, stale hash, missing audit
gate, `NOT_ASSESSABLE`, or nonpassing release status blocks delivery. Validate
non-DOCX artifacts with their native schemas instead of claiming DOCX format
coverage; derive a submission PDF only from a released DOCX and inspect it.

## Host capability contract

Load [references/platform-compatibility.md](references/platform-compatibility.md)
before using tools or bundled scripts.

- Resolve the directory containing this `SKILL.md` as `SKILL_ROOT`; never assume
  the current working directory is the Skill directory.
- Map each required behavior to the capabilities available in the current host.
  Tool names are examples, not requirements.
- For full review, use the host's real non-fork subagent/delegation mechanism
  with a fresh isolated context for every reviewer.
- Record actual host-provided Agent task IDs, timestamps, frozen-input hashes,
  and report hashes as the review execution receipt.
- If a required capability is unavailable, mark the affected gate
  `NOT ASSESSABLE`; do not imitate a completed capability in one conversation.

## Step 0: establish the manuscript route

Before reviewing, inspect the invocation for one of three routes.

- `TARGET_JOURNAL`: an exact target journal is named.
- `JOURNAL_NEUTRAL`: the user explicitly requests a neutral, general,
  journal-independent, portable, or coauthor-ready manuscript.
- `JOURNAL_RECOMMENDATION`: the user is unsure and requests recommendations.
- If the route is absent, ask only: `本次采用哪种稿件方案：中立通用稿件、指定目标期刊，还是尚未确定并需要推荐期刊？` Then stop.
- If an abbreviation is ambiguous, confirm the exact journal name and stop.
- If the exact journal or a neutral route is present, do not ask again.
- If the user is unsure, load [references/journal-discovery-and-profile.md](references/journal-discovery-and-profile.md), run `journal-recommendation`, return a verified Top 5, and pause for the user to select a primary target.
- Do not start full review until either a primary target or the neutral route is fixed.

For `JOURNAL_NEUTRAL`, load
[references/journal-neutral-manuscript.md](references/journal-neutral-manuscript.md).
Do not browse or invent journal rules, do not create a journal-specific
acceptance-tolerance card, and do not claim submission compliance. Review
against rigorous general biomedical validity, reporting, evidence, and clarity
standards. Format with the neutral house profile and label the result
`JOURNAL_NEUTRAL`; it may be coauthor-ready but is not journal-submission-ready.

For every `TARGET_JOURNAL` run, browse current official journal sources anew. Resolve article type and submission stage from the command or manuscript; ask only when ambiguity would materially change the rules. Record URLs and access dates. Do not reuse a cached journal profile as current evidence. If current official sources cannot be inspected, mark journal-specific work `NOT ASSESSABLE`.

Load
[references/journal-typography-resolution.md](references/journal-typography-resolution.md)
whenever font or line spacing is resolved. Read the complete sentence and its
scope; never promote an example-only value to a journal requirement.

For full `TARGET_JOURNAL` scientific review, load
[references/evidence-calibration.md](references/evidence-calibration.md),
inspect recent accepted same-type papers, and create
`01b_acceptance_tolerance_card.json`. Official rules and scientific validity
outrank publication precedent. Validate it with:

```bash
python3 "$SKILL_ROOT/scripts/validate_acceptance_tolerance.py" \
  01b_acceptance_tolerance_card.json
```

## Step 1: freeze and inventory the input

Record:

- manuscript path, modification time, SHA-256, and apparent version
- manuscript route; target journal when applicable; article type and stage
- main text, references, figures, tables, legends, supplements, source data, response letter, and tracked version available
- absent, stale, or mismatched materials

For `TARGET_JOURNAL`, create `00_input_inventory.json`,
`01_journal_profile.json`, and `01a_journal_format_plan.json`. The journal profile records the official rules;
the format plan converts each applicable rule into an implementation and a
verification method for this exact journal, article type, and stage. Validate
both. Load
[references/journal-format-plan.md](references/journal-format-plan.md) before
creating the format plan:

```bash
python3 "$SKILL_ROOT/scripts/validate_journal_profile.py" 01_journal_profile.json
python3 "$SKILL_ROOT/scripts/validate_journal_format_plan.py" \
  01a_journal_format_plan.json --require-pass
```

Do not begin target-journal `format-manuscript` unless the format-plan validator passes with
`--require-pass`. A generic statement such as “follow journal style” is not a
format plan.

For `JOURNAL_NEUTRAL`, create `00_input_inventory.json` and
`01_neutral_manuscript_profile.json` using the exact contract in
`journal-neutral-manuscript.md`. Do not fabricate journal URLs or place neutral
fallbacks in an artifact labeled as official journal guidance.

Do not silently combine manuscript, figures, or supplements from different versions.

## Step 2: select the task mode

Use one or more modes, but preserve their order:

| Mode | Purpose |
|---|---|
| `journal-recommendation` | Recommend a verified Top 5 when the target is unknown |
| `scientific-review` | Default for a supplied manuscript; review only |
| `reference-audit` | Verify reference reality, integrity, format, placement, and exact claim support |
| `response-to-reviewers` | Triage comments and prepare a traceable response package |
| `revise-manuscript` | Revise only after the review pause and explicit authorization |
| `format-manuscript` | Execute the validated, source-linked target-journal format plan after scientific content stabilizes |
| `release-gate` | Run final fail-closed submission audit |
| `full-run` | Run all phases but still pause after review before any revision |

If the user supplies a target and manuscript but no mode, default to `scientific-review`, read-only.

## Step 3: run the independent reviewer panel

Load [references/multi-agent-review.md](references/multi-agent-review.md),
[references/journal-tier-rubrics.md](references/journal-tier-rubrics.md), and
[references/evidence-calibration.md](references/evidence-calibration.md),
[references/review-panel-receipt-schema.md](references/review-panel-receipt-schema.md),
[references/concern-ledger-and-adjudication.md](references/concern-ledger-and-adjudication.md)
completely. Load the applicable sections of
[references/biomedical-review-gates.md](references/biomedical-review-gates.md).

In `JOURNAL_NEUTRAL`, replace journal-fit/tier calibration with portability,
scientific defensibility, reporting completeness, and claim-ceiling review.
Do not use accepted-paper precedent as an acceptance proxy. Keep the same five
independent core seats and all receipt/budget requirements.

- Spawn at least five actual independent reviewer agents with the host's
  non-fork, isolated subagent/delegation mechanism when available.
- Use five reviewer agents plus a root synthesis; do not count the root synthesis as a reviewer.
- Use exactly five core seats. For high-tier or complex manuscripts, add at
  most one sixth specialist seat, selected by the highest-risk unresolved
  trigger. Never add both a figure reviewer and an adversarial reviewer.
- Assign every applicable review axis to exactly one primary owner before
  dispatch. A reviewer may report outside its owned axes only for a clearly
  blocking concern.
- Limit each reviewer to eight prioritized concerns and 1,800
  word-equivalent units. Completeness means covering the assigned risk surface,
  not repeating a whole-manuscript review.
- Run agents in waves when concurrency is limited; never reduce the reviewer count to fit one wave.
- Give every reviewer the same frozen manuscript, inventory, factual journal
  profile, shared fact base, and role-specific rubric.
- Do not expose one reviewer's output to another before all independent reports finish.
- Use functional review lenses, not fabricated human biographies.
- If actual agent delegation is unavailable, do not claim multi-agent review completion. Mark the panel gate `NOT ASSESSABLE` and ask before using isolated single-agent passes as a fallback.

Create `02_shared_fact_base.md`, `03_review_panel_plan.json`, and
`reviews/reviewer_01.md` through `reviews/reviewer_05.md` or higher. The panel
plan must use schema `2.1`, contain five core seats and no more than one
triggered optional seat, record axis ownership and output budgets, and close
every reviewer against a unique host task
ID, `FRESH_NON_FORK` context, start/end time, the three frozen input hashes, and
the resulting report hash. Validate:

```bash
python3 "$SKILL_ROOT/scripts/validate_review_panel.py" 03_review_panel_plan.json
```

## Step 4: synthesize, decide, and pause

After all independent reports are frozen, create and validate
`reviews/concern_ledger.tsv`:

```bash
python3 "$SKILL_ROOT/scripts/validate_concern_ledger.py" \
  reviews/concern_ledger.tsv 03_review_panel_plan.json
```

Then consolidate without averaging away disagreements. Create:

- `04_cross_review_matrix.tsv`
- `05_review_verdict.md`

Every ledger concern must record one of:

- `FATAL_VALIDITY_FLAW`
- `CORRECTABLE_BEFORE_SUBMISSION`
- `ACCEPTABLE_INHERENT_LIMITATION`
- `OPTIONAL_STRENGTHENING`

Use `BLOCKING` only when accurate claim narrowing and transparent limitation
disclosure still leave the central inference invalid or the manuscript not a
defensible submission to the selected target, and the defect is anchored to
located manuscript evidence. Otherwise use a lower class/severity or
`NOT_ASSESSABLE`.

Use one matrix row per normalized issue and keep the author-facing verdict at
or below 900 word-equivalent units. Put detail in the traceable ledger; do not
repeat every reviewer report in the verdict.

Validate the verdict:

```bash
python3 "$SKILL_ROOT/scripts/validate_review_verdict.py" 05_review_verdict.md
```

Use exactly one review posture:

- `PROCEED_TO_REVISION`
- `MAJOR_SCIENTIFIC_REWORK_REQUIRED`
- `RETARGET_RECOMMENDED`
- `NOT_ASSESSABLE`

Then pause and ask whether the user authorizes revision. Do not edit prose, restyle headings, or create a revised manuscript before this authorization, even during `full-run`.

## Step 5: revise in scientific priority order

After authorization, load [references/revision-and-response.md](references/revision-and-response.md).
Load [references/ai-use-declaration.md](references/ai-use-declaration.md) when an
AI-use statement is added, revised, or checked.

Apply:

1. blocking scientific issues
2. major methods, statistics, and validation issues
3. claims, limitations, and references
4. figure-text-legend-data closure
5. article architecture
6. paragraph and sentence language
7. route-specific formatting

Preserve the original. Produce a tracked/review copy, a clean revised copy, and `revision_log.tsv`. Do not state that a change was made unless it is present in the delivered manuscript.

## Step 6: audit references and exact claim support

Load [references/reference-integrity.md](references/reference-integrity.md).
Classify claims as `A_MATERIAL`, `B_SUPPORTING`, or `C_CONTEXT`. Build
`06_reference_audit.tsv` with one row per tier-A/tier-B relationship and each
audited tier-C sample, then run:

```bash
python3 "$SKILL_ROOT/scripts/validate_reference_audit.py" 06_reference_audit.tsv
```

Metadata verification and semantic support are separate. A real paper can
still be the wrong citation. A related title or metadata-only result does not
establish direct support. A full-text review may directly support an
appropriately scoped synthesis or consensus claim, but not a specific primary
experiment, effect estimate, causal result, or safety outcome.

## Step 7: format as a submission manuscript

Always load [references/manuscript-formatting.md](references/manuscript-formatting.md),
[references/journal-typography-resolution.md](references/journal-typography-resolution.md), and
[references/table-formatting.md](references/table-formatting.md). For
a `TARGET_JOURNAL` run, also load
[references/journal-discovery-and-profile.md](references/journal-discovery-and-profile.md)
and [references/journal-format-plan.md](references/journal-format-plan.md). For
a `JOURNAL_NEUTRAL` run, load
[references/journal-neutral-manuscript.md](references/journal-neutral-manuscript.md). For
a manuscript, also load
[references/front-matter-contract.md](references/front-matter-contract.md).

- In `TARGET_JOURNAL`, treat the official journal template and current
  stage-specific guidance as authority. In `JOURNAL_NEUTRAL`, use the frozen
  neutral profile and do not run or claim the journal-specific plan gate.
- In `TARGET_JOURNAL`, reconfirm that `01a_journal_format_plan.json` matches the release-candidate
  manuscript's exact journal, article type, stage, and current
  `01_journal_profile.json` SHA-256.
- In `TARGET_JOURNAL`, execute every plan check individually. Record the source rule, concrete
  implementation, verification evidence, and final status in
  `07_format_audit.json`; do not collapse them into a generic format pass.
- Use restrained black manuscript styling unless a current official source
  requires otherwise; never introduce report-style decoration.
- Keep audit reports separate from the clean manuscript.
- Apply the complete global DOCX invariant; resolve line spacing from the exact
  current guide/template or use `double`, and record any journal override.
- Load [references/credit-authorship-contract.md](references/credit-authorship-contract.md)
  for CRediT content or formatting, and preserve bibliography as non-body.
- Run `scripts/apply_manuscript_profile.py`, then
  `scripts/enforce_docx_line_page_numbers.py`,
  `scripts/audit_docx_manuscript_style.py`,
  `scripts/audit_docx_front_matter.py`, and
  `scripts/audit_docx_semantic_rhythm.py` with the resolved role/style,
  font-family, title-size, body-size, table-size, manuscript-spacing,
  table-spacing, and table-rule-scheme inputs.
- Compare content, render and inspect every page, fix failures, then rerun from
  normalization. A mechanical XML pass is not a release.

For `TARGET_JOURNAL`, after all plan checks, mechanical audits, and page
inspections are recorded, validate closure from the plan to the delivered
files:

```bash
python3 "$SKILL_ROOT/scripts/validate_journal_format_audit.py" \
  01a_journal_format_plan.json 07_format_audit.json

python3 "$SKILL_ROOT/scripts/validate_format_release.py" \
  07_structural_format_audit.json 07_front_matter_audit.json \
  07_semantic_rhythm_audit.json \
  --content-preservation-status PASS \
  --journal-status PASS --render-status PASS \
  --output-json 07_format_release.json
```

Do not report journal-specific formatting `PASS` unless the plan-to-output
validator passes. Do not deliver a manuscript DOCX as fully verified unless
the combined validator returns `FORMAT_RELEASE_PASS`. For cover letters,
response letters, and editable package text without manuscript front matter,
load [references/submission-package-contract.md](references/submission-package-contract.md)
and require `PACKAGE_FORMAT_RELEASE_PASS` without fabricating a title block.
For a neutral manuscript, pass `--journal-status NOT_APPLICABLE`, require every
other mechanical/content/render gate, and report `NEUTRAL_FORMAT_PASS`; never
rename it `RELEASE PASS` for a journal submission.

## Step 8: run the release gate

Load [references/release-gates.md](references/release-gates.md). Re-run targeted reviewer agents when revisions changed the claim architecture, core evidence, statistics, figures, or references.

Report manuscript readiness separately from workflow assurance. Missing Agent
capacity or task receipts makes workflow assurance `NOT ASSESSABLE`; it is not
itself a scientific defect in the manuscript.

Return the manuscript-readiness status, workflow-assurance status, and exactly
one route-appropriate overall state from `release-gates.md`: `RELEASE PASS`,
`RELEASE FAIL`, or `RELEASE NOT ASSESSABLE` for a target journal; `NEUTRAL
MANUSCRIPT PASS`, `NEUTRAL MANUSCRIPT FAIL`, or `NEUTRAL MANUSCRIPT NOT
ASSESSABLE` for a general manuscript.

Never predict acceptance.

## Artifact contract

Use this stable order when the corresponding phase runs:

```text
00_input_inventory.json
01_journal_profile.json OR 01_neutral_manuscript_profile.json
01a_journal_format_plan.json (target-journal route only)
01b_acceptance_tolerance_card.json (target-journal route only)
02_shared_fact_base.md
03_review_panel_plan.json
reviews/reviewer_01.md ...
reviews/concern_ledger.tsv
04_cross_review_matrix.tsv
05_review_verdict.md
06_reference_audit.tsv
revision/issue_ledger.tsv
revision/manuscript_tracked.docx
revision/manuscript_clean.docx
revision/revision_log.tsv
07_format_audit.json
07_structural_format_audit.json
07_front_matter_audit.json
07_semantic_rhythm_audit.json
07_format_release.json
07_generated_docx_release_receipt.json
07_generated_docx_release.json
08_release_gate.md
```

Keep review artifacts factual and utilitarian. The submission manuscript must not inherit their tables, colors, status boxes, or report styling.

## Resource routing

| Resource | Load when |
|---|---|
| [references/platform-compatibility.md](references/platform-compatibility.md) | Resolving host tools, subagents, bundled scripts, or install-specific behavior |
| [references/journal-discovery-and-profile.md](references/journal-discovery-and-profile.md) | Target journal is unknown or any journal-specific task begins |
| [references/journal-neutral-manuscript.md](references/journal-neutral-manuscript.md) | The user selects a neutral/general manuscript route |
| [references/journal-format-plan.md](references/journal-format-plan.md) | Translating official journal requirements into a per-manuscript executable format and package plan |
| [references/journal-typography-resolution.md](references/journal-typography-resolution.md) | Classifying binding/direct versus example-only font and line-spacing language and resolving fallbacks |
| [references/multi-agent-review.md](references/multi-agent-review.md) | Planning, running, or synthesizing reviewer agents |
| [references/journal-tier-rubrics.md](references/journal-tier-rubrics.md) | Calibrating reviewer strictness or selecting specialist roles |
| [references/evidence-calibration.md](references/evidence-calibration.md) | Building accepted-paper tolerance cards, applying the blocking test, and separating inherent limitations from fatal flaws |
| [references/review-panel-receipt-schema.md](references/review-panel-receipt-schema.md) | Building and validating host task receipts and report hashes |
| [references/concern-ledger-and-adjudication.md](references/concern-ledger-and-adjudication.md) | Normalizing findings, evidence anchors, consensus, disagreement, and resolution |
| [references/biomedical-review-gates.md](references/biomedical-review-gates.md) | Applying design-specific clinical, wet-lab, omics, AI, review, or animal stress tests |
| [references/reference-integrity.md](references/reference-integrity.md) | Auditing, adding, moving, or formatting citations |
| [references/revision-and-response.md](references/revision-and-response.md) | Revising a manuscript or responding to reviewers |
| [references/ai-use-declaration.md](references/ai-use-declaration.md) | Adding, revising, or checking an AI-use statement |
| [references/credit-authorship-contract.md](references/credit-authorship-contract.md) | Adding, revising, formatting, or auditing a CRediT authorship contribution statement |
| [references/manuscript-formatting.md](references/manuscript-formatting.md) | Creating or checking DOCX/PDF/LaTeX submission files |
| [references/table-formatting.md](references/table-formatting.md) | Creating, normalizing, or auditing any manuscript table |
| [references/generated-docx-release-contract.md](references/generated-docx-release-contract.md) | Closing every generated or modified DOCX against the embedded formatting lane before delivery |
| [references/submission-package-contract.md](references/submission-package-contract.md) | Formatting or auditing cover letters, response letters, and editable package text |
| [references/front-matter-contract.md](references/front-matter-contract.md) | Normalizing or auditing manuscript title, authors, affiliations, correspondence, anonymization, or first-page layout |
| [references/release-gates.md](references/release-gates.md) | Deciding whether a package is ready |

## Boundaries

- Official instructions, specific editor directions, and supplied templates outrank generalized style guidance.
- Neutral mode is deliberately journal-independent. It cannot establish
  article-type eligibility, journal limits, template compliance, or submission
  readiness; retargeting reopens the journal profile, format plan, tolerance
  calibration, and affected review axes.
- A journal profile or format plan from an earlier manuscript, article type,
  stage, or access date is routing evidence only; refresh it before claiming
  current journal-specific compliance.
- A journal benchmark does not authorize imitation or overclaiming.
- Search snippets and metadata do not count as inspected scientific evidence.
- If the user asks only for diagnosis, do not modify files.
- If a scientific direction changes, freeze passed artifacts and reopen review before drafting through the turn.
