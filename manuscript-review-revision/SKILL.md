---
name: manuscript-review-revision
description: |
  Run a journal-aware, review-first workflow for biomedical and scientific manuscripts. Support target-journal confirmation or recommendation, official-guideline research, source-linked format plans, five independent reviewers, scientific/statistical review, claim-reference verification, authorized revision and reviewer responses, DOCX/PDF formatting, and fail-closed release auditing. Enforce natural empty paragraphs, zero paragraph spacing, one manuscript-wide line-spacing token, body-sized author/affiliation/declaration roles, semantic Keywords/section/CRediT spacing, left-aligned front matter, continuous Word line and page numbering, and rendered-page QA. Use for integrated review, revision, response, retargeting, submission preparation, or journal-specific formatting. For format-only DOCX repair, prefer `manuscript-docx-formatting`. Require the exact target journal before full review; never revise before the review gate and user authorization.
---

# Manuscript Review & Revision

## Operating contract

Treat review, revision, and formatting as separate phases. Use this non-negotiable order:

`target journal -> journal profile -> journal format plan -> acceptance-tolerance card -> frozen input -> independent review -> synthesis -> user gate -> scientific revision -> reference/figure closure -> language -> formatting -> release gate`

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
- Give body prose and empty separators the explicit required line-spacing
  token; never inherit Word defaults and never disable the line-spacing check.
- For manuscripts, apply that same resolved token to title, authors,
  affiliations, correspondence, Keywords, every heading/subheading, and all
  declaration/CRediT paragraphs. Authors, affiliations, correspondence,
  Keywords, headings, and declarations use the resolved body font size (12 pt
  fallback).
- Bold only recognized `Keywords:` and inline declaration labels. Place no
  empty paragraph before Keywords, exactly one after Keywords and before each
  new section/subsection/declaration block, and none between a heading and its
  first body paragraph.
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
- For a manuscript, normalize and audit title, authors, affiliations, and
  correspondence as semantic front-matter roles. Use restrained left-aligned
  journal-neutral defaults unless a current exact journal template records a
  different rule. Do not guess roles from appearance or center a title block by
  default.
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

## Step 0: establish the target journal

Before reviewing, inspect the invocation for an exact target journal.

- If absent, ask only: `本次目标期刊是什么？如果尚未确定，请回复“不确定，请推荐期刊”。` Then stop.
- If an abbreviation is ambiguous, confirm the exact journal name and stop.
- If the exact journal is present, do not ask again.
- If the user is unsure, load [references/journal-discovery-and-profile.md](references/journal-discovery-and-profile.md), run `journal-recommendation`, return a verified Top 5, and pause for the user to select a primary target.
- Do not start full review until the primary target is fixed.

For every fixed target and every manuscript run, browse current official journal sources anew. Resolve article type and submission stage from the command or manuscript; ask only when ambiguity would materially change the rules. Record URLs and access dates. Do not reuse a cached journal profile as current evidence. If current official sources cannot be inspected, mark journal-specific work `NOT ASSESSABLE`.

For full scientific review, load
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
- target journal, article type, and stage
- main text, references, figures, tables, legends, supplements, source data, response letter, and tracked version available
- absent, stale, or mismatched materials

Create `00_input_inventory.json`, `01_journal_profile.json`, and
`01a_journal_format_plan.json`. The journal profile records the official rules;
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

Do not begin `format-manuscript` unless the format-plan validator passes with
`--require-pass`. A generic statement such as “follow journal style” is not a
format plan.

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
7. target-journal formatting

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

Load [references/journal-discovery-and-profile.md](references/journal-discovery-and-profile.md),
[references/journal-format-plan.md](references/journal-format-plan.md), and
[references/manuscript-formatting.md](references/manuscript-formatting.md). For
a manuscript, also load
[references/front-matter-contract.md](references/front-matter-contract.md).

- Treat the official journal template and current stage-specific guidance as authority.
- Reconfirm that `01a_journal_format_plan.json` matches the release-candidate
  manuscript's exact journal, article type, stage, and current
  `01_journal_profile.json` SHA-256.
- Execute every plan check individually. Record the source rule, concrete
  implementation, verification evidence, and final status in
  `07_format_audit.json`; do not collapse them into a generic format pass.
- When no color is explicitly required, use black title, headings, subheadings, and body text.
- Do not use report-style covers, colored heading themes, cards, callouts, banners, icons, decorative rules, or business-document styling in the submission manuscript.
- Keep audit reports separate from the clean manuscript.
- Use literal body-paragraph separation: set effective body-paragraph spacing before/after to `0 pt` and insert exactly one structurally empty paragraph between adjacent body-prose paragraphs. Do not simulate that blank line with paragraph spacing or a manual line break.
- Resolve body line spacing to an explicit token from the exact journal template or current author guide; if neither specifies it, use the conservative manuscript fallback `double`. Encode the value in the body style and the empty separator paragraph instead of inheriting Word's default line spacing.
- Apply the resolved token manuscript-wide, including title block, headings,
  Keywords, and declarations. Keep authors, affiliations, correspondence,
  Keywords, headings, and CRediT/declaration text at the resolved body size.
- Enforce the semantic blank-line matrix: no blank before Keywords, exactly one
  after Keywords, exactly one before each section/subsection/declaration block,
  and none between a heading and its first body paragraph. Bold only recognized
  Keywords and inline declaration labels.
- Keep entries after `References`/`Bibliography` in a dedicated non-body role;
  never insert body-prose blank separators between reference entries.
- Apply the same paragraph-structure rule to every modified DOCX. Do not ask the user to repair it manually: correct the generated file and re-run the audit until it passes.
- Apply continuous Word-native line numbering to every section and a dynamic,
  continuous `PAGE` field to every active page story in every modified DOCX.
  Do not allow paragraph suppression, section restarts, typed page numerals, or
  partial-section coverage.
- For DOCX, use a reliable document runtime available in the host, run the mechanical style audit, render every page to PNG/PDF, inspect every page, fix, and re-render.

```bash
python3 "$SKILL_ROOT/scripts/apply_manuscript_profile.py" manuscript.docx \
  --out manuscript.normalized.docx \
  --line-spacing <resolved-token> \
  --body-style <each-prose-style> \
  --title-paragraph <n> --authors-paragraph <n> \
  --affiliation-paragraph <n> --correspondence-paragraph <n>

python3 "$SKILL_ROOT/scripts/enforce_docx_line_page_numbers.py" \
  manuscript.normalized.docx --out manuscript.numbered.docx \
  --page-number-position <resolved-position>

python3 "$SKILL_ROOT/scripts/audit_docx_manuscript_style.py" \
  manuscript.numbered.docx --paragraph-separation literal-blank \
  --expected-line-spacing <resolved-token> \
  --body-style <each-prose-style> \
  --exclude-style <each-semantic-nonbody-style> \
  --output-json 07_structural_format_audit.json

python3 "$SKILL_ROOT/scripts/audit_docx_front_matter.py" \
  manuscript.numbered.docx --mode <blinded-or-unblinded> \
  --front-matter-alignment <resolved-alignment> \
  --expected-page-number-position <resolved-position> \
  --expected-line-spacing <resolved-token> \
  --output-json 07_front_matter_audit.json

python3 "$SKILL_ROOT/scripts/audit_docx_semantic_rhythm.py" \
  manuscript.numbered.docx \
  --expected-line-spacing <resolved-token> \
  --expected-body-font-size <resolved-body-size> \
  --output-json 07_semantic_rhythm_audit.json
```

Replace `double` with the exact `style_contract.line_spacing` token from the
validated journal format plan;
accepted tokens include a multiple such as `1.5`, `exact:24pt`, or
`at-least:14pt`.
The global DOCX paragraph and numbering invariant remains mandatory in this
phase. A mechanical pass does not replace official-template or rendered visual
review.

After all plan checks, mechanical audits, and page inspections are recorded,
validate closure from the plan to the delivered files:

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

## Step 8: run the release gate

Load [references/release-gates.md](references/release-gates.md). Re-run targeted reviewer agents when revisions changed the claim architecture, core evidence, statistics, figures, or references.

Report manuscript readiness separately from workflow assurance. Missing Agent
capacity or task receipts makes workflow assurance `NOT ASSESSABLE`; it is not
itself a scientific defect in the manuscript.

Return the manuscript-readiness status, workflow-assurance status, and exactly
one overall state: `RELEASE PASS`, `RELEASE FAIL`, or
`RELEASE NOT ASSESSABLE`, using the mapping in `release-gates.md`.

Never predict acceptance.

## Artifact contract

Use this stable order when the corresponding phase runs:

```text
00_input_inventory.json
01_journal_profile.json
01a_journal_format_plan.json
01b_acceptance_tolerance_card.json
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
08_release_gate.md
```

Keep review artifacts factual and utilitarian. The submission manuscript must not inherit their tables, colors, status boxes, or report styling.

## Resource routing

| Resource | Load when |
|---|---|
| [references/platform-compatibility.md](references/platform-compatibility.md) | Resolving host tools, subagents, bundled scripts, or install-specific behavior |
| [references/journal-discovery-and-profile.md](references/journal-discovery-and-profile.md) | Target journal is unknown or any journal-specific task begins |
| [references/journal-format-plan.md](references/journal-format-plan.md) | Translating official journal requirements into a per-manuscript executable format and package plan |
| [references/multi-agent-review.md](references/multi-agent-review.md) | Planning, running, or synthesizing reviewer agents |
| [references/journal-tier-rubrics.md](references/journal-tier-rubrics.md) | Calibrating reviewer strictness or selecting specialist roles |
| [references/evidence-calibration.md](references/evidence-calibration.md) | Building accepted-paper tolerance cards, applying the blocking test, and separating inherent limitations from fatal flaws |
| [references/review-panel-receipt-schema.md](references/review-panel-receipt-schema.md) | Building and validating host task receipts and report hashes |
| [references/concern-ledger-and-adjudication.md](references/concern-ledger-and-adjudication.md) | Normalizing findings, evidence anchors, consensus, disagreement, and resolution |
| [references/biomedical-review-gates.md](references/biomedical-review-gates.md) | Applying design-specific clinical, wet-lab, omics, AI, review, or animal stress tests |
| [references/reference-integrity.md](references/reference-integrity.md) | Auditing, adding, moving, or formatting citations |
| [references/revision-and-response.md](references/revision-and-response.md) | Revising a manuscript or responding to reviewers |
| [references/ai-use-declaration.md](references/ai-use-declaration.md) | Adding, revising, or checking an AI-use statement |
| [references/manuscript-formatting.md](references/manuscript-formatting.md) | Creating or checking DOCX/PDF/LaTeX submission files |
| [references/submission-package-contract.md](references/submission-package-contract.md) | Formatting or auditing cover letters, response letters, and editable package text |
| [references/front-matter-contract.md](references/front-matter-contract.md) | Normalizing or auditing manuscript title, authors, affiliations, correspondence, anonymization, or first-page layout |
| [references/release-gates.md](references/release-gates.md) | Deciding whether a package is ready |

## Boundaries

- Official instructions, specific editor directions, and supplied templates outrank generalized style guidance.
- A journal profile or format plan from an earlier manuscript, article type,
  stage, or access date is routing evidence only; refresh it before claiming
  current journal-specific compliance.
- A journal benchmark does not authorize imitation or overclaiming.
- Search snippets and metadata do not count as inspected scientific evidence.
- If the user asks only for diagnosis, do not modify files.
- If a scientific direction changes, freeze passed artifacts and reopen review before drafting through the turn.
