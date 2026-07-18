# Formal submission-manuscript formatting

## Source precedence

Apply:

1. specific editor instructions
2. exact journal template for the relevant article type and stage
3. current official journal author guide
4. conservative scholarly manuscript defaults

Initial submission, revision, final submission, and proof correction can require different files and styling. Never reuse a profile from another stage without refreshing it.

## Submission manuscript visual contract

Unless an official template explicitly requires otherwise:

- use black title, author block, headings, subheadings, and body text
- use restrained scholarly typography
- use real paragraph styles redefined to the journal profile
- do not use Word theme-accent blue headings
- do not use report covers, colored bands, cards, callout boxes, icons, dashboards, decorative rules, branding, or oversized title treatments
- do not use tables as layout containers
- do not place audit statuses or reviewer notes inside the clean manuscript
- preserve conventional scientific section hierarchy

The review report may use tables for issue tracking, but its visual system must never be copied into the submission manuscript.

## DOCX workflow

1. Preserve the original.
2. Use the journal template when supplied; otherwise create an explicit neutral style map.
3. Apply only stage-appropriate requirements: fonts, margins, spacing, line numbering, anonymization, section order, citations, captions, tables, and page breaks.
4. Run `python3 "$SKILL_ROOT/scripts/audit_docx_manuscript_style.py" manuscript.docx`.
5. Render DOCX with a reliable renderer available in the current host.
6. Inspect every page at 100% zoom.
7. Check title/heading color, clipping, overlap, tables, captions, page breaks, orphan headings, figures, headers/footers, line numbers, and references.
8. Fix and re-render after every layout-sensitive change.

Codex may use an installed document/PDF capability. Claude Code may use an
available office converter, renderer, script, or MCP tool. If rendering is
unavailable, disclose that visual QA was not completed and return the format
gate `NOT ASSESSABLE`.

## Output separation

When authorized to revise, normally produce:

- `manuscript_tracked.docx` or another clearly reviewable redline
- `manuscript_clean.docx`
- `revision_log.tsv`
- `07_format_audit.json`

Do not strip comments, tracked changes, citation fields, author identity, or metadata until the journal stage and user's requested deliverable are known.

## Mechanical audit boundary

The style script flags explicit non-black or theme-colored title/heading text, title/heading shading, and decorative paragraph borders. It cannot prove compliance with a journal template or visual correctness. Always combine it with official-source review and rendered page inspection.
