# Source-linked journal format plan

## Contents

1. [Purpose and artifact boundary](#purpose-and-artifact-boundary)
2. [Current-source rule](#current-source-rule)
3. [Plan schema](#plan-schema)
4. [Required check categories](#required-check-categories)
5. [Style contract](#style-contract)
6. [Implementation and audit](#implementation-and-audit)

## Purpose and artifact boundary

Use three separate artifacts:

- `01_journal_profile.json` records what current official sources say.
- `01a_journal_format_plan.json` translates those rules into exact actions and
  verification methods for one journal, article type, and submission stage.
- `07_format_audit.json` records whether the delivered manuscript and package
  actually satisfy the plan.

Do not use the manuscript's current appearance as the format plan. Do not turn
an observed convention from one published paper into a mandatory journal rule.
A plan is `PASS` only when every required category has a resolved action or an
explicit, justified `NOT_APPLICABLE` outcome.

## Current-source rule

Refresh official sources for every manuscript run. Keep target journal,
article type, stage, access date, and official URLs explicit. Hash the exact
`01_journal_profile.json` and store the value as `journal_profile_sha256` in the
format plan.

Use this authority order:

1. current editor instruction or decision letter;
2. exact article-type and stage-specific official template;
3. current exact-journal author guide or policy;
4. conservative manuscript fallback.

Load [journal-typography-resolution.md](journal-typography-resolution.md) for
font and line spacing. Read the full source sentence and scope. Example-only
language such as `e.g.` is not an official override.

An earlier profile, a publisher-wide default, a search snippet, or one
published PDF is not current journal-specific authority. If official sources
are inaccessible or contradictory, mark the affected plan rule
`NOT_ASSESSABLE`; never silently substitute remembered requirements.

## Plan schema

Create `01a_journal_format_plan.json` with:

- `schema_version`: `1.1`
- `target_journal`
- `article_type`
- `submission_stage`
- `accessed_at`
- `plan_status`: `DRAFT`, `PASS`, `FAIL`, or `NOT_ASSESSABLE`
- `journal_profile_sha256`
- `official_sources[]`: `title`, `url`, `accessed_at`, `official`
- `style_contract`
- `checks[]`

Every `checks[]` entry must contain:

- `id`
- `category`
- `requirement`: the resolved journal requirement or explicit fallback
- `implementation`: the exact manuscript or package action
- `verification`: the observable pass test
- `deliverable`: the affected file or submission-system field
- `basis`: `EDITOR_INSTRUCTION`, `OFFICIAL_TEMPLATE`, `OFFICIAL_GUIDE`,
  `CONSERVATIVE_FALLBACK`, `USER_GLOBAL_INVARIANT`, or `NOT_APPLICABLE`
- `source_url`: an official URL for every official basis; otherwise `null` is
  allowed
- `mandatory`: boolean
- `status`: `RESOLVED`, `NOT_ASSESSABLE`, or `NOT_APPLICABLE`

Do not write vague actions such as `format references correctly` or `follow
journal style`. Use executable statements such as `convert in-text citations
to numbered square brackets in order of appearance and regenerate the
reference list with the journal's named style` plus a concrete verification
test.

## Required check categories

Cover every category even when the result is `NOT_APPLICABLE`:

| Category | Resolve for this exact journal, type, and stage |
|---|---|
| `article-type` | official article-type name and eligibility |
| `file-format` | accepted main-file formats and whether a template is required |
| `title-page` | title, running title, author, affiliation, corresponding-author, keyword, and count fields |
| `anonymization` | blinded versus identified manuscript and metadata handling |
| `abstract` | structured/unstructured form, headings, and limit |
| `main-text` | word or character limit and what the count includes |
| `section-order` | required order and journal-specific named sections |
| `references` | citation system, list style, limit, DOI/URL, and live-field policy |
| `figures` | count, placement, legends, format, color mode, and resolution |
| `tables` | count, placement, editable format, titles, and footnotes |
| `supplements` | naming, acceptable formats, legends, and upload separation |
| `line-numbering` | journal rule and the overriding continuous personal invariant |
| `page-numbering` | journal rule and the overriding continuous dynamic-page-field invariant |
| `statistics` | journal-specific reporting and statistical-file requirements |
| `reporting-guidelines` | CONSORT, PRISMA, STROBE, ARRIVE, TRIPOD, or other applicable checklist |
| `ethics-registration` | approvals, consent, trial/review registration, and identifiers |
| `data-code` | availability statements, repositories, accessions, source data, and code |
| `declarations` | contributions, funding, conflicts, acknowledgments, AI-use, and other required statements |
| `cover-letter` | whether required and journal-specific content |
| `submission-files` | complete stage-specific upload package and naming rules |

Publisher forms and submission-system fields count as package requirements even
when they do not appear inside the manuscript.

## Style contract

Resolve these machine-usable fields before editing DOCX:

- `paragraph_separation`
- `paragraph_separation_basis`
- `line_spacing`
- `line_spacing_basis`
- `line_numbering`
- `line_numbering_basis`
- `page_numbering`
- `page_numbering_basis`
- `page_number_position`
- `page_number_position_basis`
- `front_matter_alignment`
- `front_matter_alignment_basis`
- `anonymization_mode`
- `body_font_family`
- `body_font_size_pt`
- `title_font_size_pt`
- `table_font_size_pt`
- `font_basis`
- `font_rule_strength`
- `font_source_excerpt`
- `line_spacing_rule_strength`
- `line_spacing_source_excerpt`
- `text_color_hex`
- `space_before_pt`
- `space_after_pt`
- `body_styles[]`
- `page_size`
- `margins`
- `columns`
- `source_urls[]`

Use an explicit line-spacing token accepted by the DOCX audit: `single`,
`1.15`, `1.5`, `double`, another positive multiple, `exact:<pt>pt`, or
`at-least:<pt>pt`.

Always use `paragraph_separation=literal-blank`,
`paragraph_separation_basis=USER_GLOBAL_INVARIANT`, `space_before_pt=0`, and
`space_after_pt=0`. Also use `line_numbering=continuous`,
`line_numbering_basis=USER_GLOBAL_INVARIANT`, `page_numbering=continuous`, and
`page_numbering_basis=USER_GLOBAL_INVARIANT`. The same contract applies to
every modified DOCX, including tracked and clean manuscripts, cover letters,
response letters, and editable supplementary text. An official-template
conflict must be reported; it cannot silently bypass the user's paragraph or
numbering invariants.

Resolve `front_matter_alignment`, `anonymization_mode`, and
`page_number_position` for this exact journal, article type, and submission
stage. Use `left`, `unblinded`, and `upper-right` as conservative fallbacks only
when no current exact source specifies another value. Record official-template
or official-guide decisions with their corresponding basis and source URL.

Use concrete conservative values for unspecified or example-only typography:
Times New Roman, Title 15 pt bold, every other visible manuscript paragraph 12
pt, table text 12 pt, headings/subheadings 12 pt bold, and double line spacing.
Mark their basis `CONSERVATIVE_FALLBACK` and keep them distinct from official
journal rules. Only `MANDATORY` or `EXPLICIT_REQUIREMENT` evidence may use an
official typography basis. Never inherit Word theme defaults.

Validate the plan:

```bash
python3 "$SKILL_ROOT/scripts/validate_journal_format_plan.py" \
  01a_journal_format_plan.json --require-pass
```

Omit `--require-pass` only while diagnosing an incomplete draft plan. Never
start manuscript formatting from a `DRAFT`, `FAIL`, or `NOT_ASSESSABLE` plan.

## Implementation and audit

Execute checks in this order:

1. correct article type, stage, template, and anonymization;
2. required manuscript elements and order;
3. text, abstract, reference, figure, and table limits;
4. references, reporting guidelines, statistics, ethics, data/code, and declarations;
5. DOCX page layout, typography, continuous line/page numbering, and paragraph structure;
6. figures, tables, supplements, cover letter, and all upload files;
7. mechanical DOCX audit and rendered page-by-page visual inspection.

In `07_format_audit.json`, preserve each plan check ID and record `PASS`,
`FAIL`, or `NOT_ASSESSABLE`, the inspected evidence, and the affected output.
Also record the plan SHA-256, manuscript SHA-256, audit command, renderer, page
count, and visual-QA status. A style-script pass cannot close content limits,
required declarations, figures, tables, or submission-package checks.

Validate the completed audit against the exact plan and output files:

```bash
python3 "$SKILL_ROOT/scripts/validate_journal_format_audit.py" \
  01a_journal_format_plan.json 07_format_audit.json
```

The audit validator requires every plan check ID, verifies the plan and
manuscript hashes, confirms that the recorded paragraph, line-spacing,
line-numbering, and page-numbering modes match `style_contract`, and requires
mechanical and page-by-page visual passes before accepting an overall `PASS`.
