---
name: manuscript-review-revision
description: |
  Run a platform-independent, journal-aware, review-first workflow for scientific manuscripts, including target-journal confirmation or Top-5 journal recommendation, live official-author-guideline research, at least five independent reviewer agents, scientific and statistical review, claim-reference verification, reviewer-response drafting, revision, formal DOCX/PDF manuscript formatting, and fail-closed release auditing. Use in Codex, Claude Code, or another compatible Agent Skills host when the user asks to review, revise, polish, format, submit, retarget, recommend journals for, verify references in, or respond to reviewers about a biomedical or scientific manuscript. Always establish the exact target journal before full review; never revise or cosmetically polish before the independent review gate is complete and the user authorizes revision.
---

# Manuscript Review & Revision

## Operating contract

Treat review, revision, and formatting as separate phases. Use this non-negotiable order:

`target journal -> journal profile -> frozen input -> independent review -> synthesis -> user gate -> scientific revision -> reference/figure closure -> language -> formatting -> release gate`

- Keep the manuscript read-only through review.
- Do not turn a polished file into a submission-ready claim.
- Do not invent experiments, analyses, citations, journal rules, reviewer identities, line numbers, or completed changes.
- Use `PASS`, `FAIL`, or `NOT ASSESSABLE` for critical gates.
- Explain findings in the user's language while preserving exact manuscript text, filenames, identifiers, and journal wording.

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

For every fixed target, browse current official journal sources. Resolve article type and submission stage from the command or manuscript; ask only when ambiguity would materially change the rules. Record URLs and access dates. If current official sources cannot be inspected, mark journal-specific work `NOT ASSESSABLE`.

## Step 1: freeze and inventory the input

Record:

- manuscript path, modification time, SHA-256, and apparent version
- target journal, article type, and stage
- main text, references, figures, tables, legends, supplements, source data, response letter, and tracked version available
- absent, stale, or mismatched materials

Create `00_input_inventory.json` and `01_journal_profile.json`. Validate the latter with:

```bash
python3 "$SKILL_ROOT/scripts/validate_journal_profile.py" 01_journal_profile.json
```

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
| `format-manuscript` | Apply current official journal requirements after scientific content stabilizes |
| `release-gate` | Run final fail-closed submission audit |
| `full-run` | Run all phases but still pause after review before any revision |

If the user supplies a target and manuscript but no mode, default to `scientific-review`, read-only.

## Step 3: run the independent reviewer panel

Load [references/multi-agent-review.md](references/multi-agent-review.md),
[references/journal-tier-rubrics.md](references/journal-tier-rubrics.md), and
[references/review-panel-receipt-schema.md](references/review-panel-receipt-schema.md),
[references/concern-ledger-and-adjudication.md](references/concern-ledger-and-adjudication.md)
completely. Load the applicable sections of
[references/biomedical-review-gates.md](references/biomedical-review-gates.md).

- Spawn at least five actual independent reviewer agents with the host's
  non-fork, isolated subagent/delegation mechanism when available.
- Use five reviewer agents plus a root synthesis; do not count the root synthesis as a reviewer.
- For high-tier or complex manuscripts, add a sixth specialist or adversarial reviewer.
- Run agents in waves when concurrency is limited; never reduce the reviewer count to fit one wave.
- Give every reviewer the same frozen manuscript, inventory, factual journal
  profile, shared fact base, and role-specific rubric.
- Do not expose one reviewer's output to another before all independent reports finish.
- Use functional review lenses, not fabricated human biographies.
- If actual agent delegation is unavailable, do not claim multi-agent review completion. Mark the panel gate `NOT ASSESSABLE` and ask before using isolated single-agent passes as a fallback.

Create `02_shared_fact_base.md`, `03_review_panel_plan.json`, and
`reviews/reviewer_01.md` through `reviews/reviewer_05.md` or higher. The panel
plan must use schema `2.0` and close every reviewer against a unique host task
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

Use exactly one review posture:

- `PROCEED_TO_REVISION`
- `MAJOR_SCIENTIFIC_REWORK_REQUIRED`
- `RETARGET_RECOMMENDED`
- `NOT_ASSESSABLE`

Then pause and ask whether the user authorizes revision. Do not edit prose, restyle headings, or create a revised manuscript before this authorization, even during `full-run`.

## Step 5: revise in scientific priority order

After authorization, load [references/revision-and-response.md](references/revision-and-response.md).

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

Load [references/reference-integrity.md](references/reference-integrity.md). Build `06_reference_audit.tsv` with one row per atomic claim-citation relationship, then run:

```bash
python3 "$SKILL_ROOT/scripts/validate_reference_audit.py" 06_reference_audit.tsv
```

Metadata verification and semantic support are separate. A real paper can still be the wrong citation. A related title, metadata-only result, or review article does not establish direct support.

## Step 7: format as a submission manuscript

Load [references/manuscript-formatting.md](references/manuscript-formatting.md).

- Treat the official journal template and current stage-specific guidance as authority.
- When no color is explicitly required, use black title, headings, subheadings, and body text.
- Do not use report-style covers, colored heading themes, cards, callouts, banners, icons, decorative rules, or business-document styling in the submission manuscript.
- Keep audit reports separate from the clean manuscript.
- For DOCX, use a reliable document runtime available in the host, run the mechanical style audit, render every page to PNG/PDF, inspect every page, fix, and re-render.

```bash
python3 "$SKILL_ROOT/scripts/audit_docx_manuscript_style.py" manuscript.docx
```

A mechanical pass does not replace official-template or rendered visual review.

## Step 8: run the release gate

Load [references/release-gates.md](references/release-gates.md). Re-run targeted reviewer agents when revisions changed the claim architecture, core evidence, statistics, figures, or references.

Return exactly one final state:

- `RELEASE PASS`
- `RELEASE FAIL`
- `RELEASE NOT ASSESSABLE`

Never predict acceptance.

## Artifact contract

Use this stable order when the corresponding phase runs:

```text
00_input_inventory.json
01_journal_profile.json
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
08_release_gate.md
```

Keep review artifacts factual and utilitarian. The submission manuscript must not inherit their tables, colors, status boxes, or report styling.

## Resource routing

| Resource | Load when |
|---|---|
| [references/platform-compatibility.md](references/platform-compatibility.md) | Resolving host tools, subagents, bundled scripts, or install-specific behavior |
| [references/journal-discovery-and-profile.md](references/journal-discovery-and-profile.md) | Target journal is unknown or any journal-specific task begins |
| [references/multi-agent-review.md](references/multi-agent-review.md) | Planning, running, or synthesizing reviewer agents |
| [references/journal-tier-rubrics.md](references/journal-tier-rubrics.md) | Calibrating reviewer strictness or selecting specialist roles |
| [references/review-panel-receipt-schema.md](references/review-panel-receipt-schema.md) | Building and validating host task receipts and report hashes |
| [references/concern-ledger-and-adjudication.md](references/concern-ledger-and-adjudication.md) | Normalizing findings, evidence anchors, consensus, disagreement, and resolution |
| [references/biomedical-review-gates.md](references/biomedical-review-gates.md) | Applying design-specific clinical, wet-lab, omics, AI, review, or animal stress tests |
| [references/reference-integrity.md](references/reference-integrity.md) | Auditing, adding, moving, or formatting citations |
| [references/revision-and-response.md](references/revision-and-response.md) | Revising a manuscript or responding to reviewers |
| [references/manuscript-formatting.md](references/manuscript-formatting.md) | Creating or checking DOCX/PDF/LaTeX submission files |
| [references/release-gates.md](references/release-gates.md) | Deciding whether a package is ready |

## Boundaries

- Official instructions, specific editor directions, and supplied templates outrank generalized style guidance.
- A journal benchmark does not authorize imitation or overclaiming.
- Search snippets and metadata do not count as inspected scientific evidence.
- If the user asks only for diagnosis, do not modify files.
- If a scientific direction changes, freeze passed artifacts and reopen review before drafting through the turn.
