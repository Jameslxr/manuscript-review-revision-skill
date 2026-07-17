# Journal discovery and live profile

## Mandatory source order

Use current primary sources in this order:

1. a specific editor instruction or decision letter
2. the exact journal's official author guide, article-type page, policies, templates, and submission checklist
3. the official publisher journal directory or policy page
4. trusted indexing and bibliographic services for discovery
5. recent same-type articles on the official journal site for observed practice

Do not infer a current rule from memory, a search snippet, a commercial journal-ranking page, or one published PDF. Record the access date and the exact stage: `initial`, `revision`, `final`, or `proof`.

## Unknown target: journal-recommendation

Request a full manuscript when available. Minimum usable evidence is the abstract, article type, core methods, principal results, sample/validation scope, and major figures or their descriptions. If only a title or short concept is available, label the output preliminary.

Build a broad candidate pool using sources appropriate to the field, such as Crossref, PubMed/NLM Journal Catalog, DOAJ, official publisher directories, and publisher article searches. Use Web of Science, Scopus, JCR, or proprietary metrics only when legitimately accessible. Do not claim literal coverage of every journal.

Exclude candidates that:

- do not accept the article type
- have a clearly mismatched scope or audience
- cannot be verified on an official site
- show unresolved credibility, indexing, or publishing-integrity concerns
- cannot accommodate material requirements that are essential to the manuscript

## Top-5 scoring

Use a comparative score, not an acceptance probability:

| Dimension | Default weight |
|---|---:|
| scope/topic fit | 20 |
| article-type fit | 10 |
| evidence quality versus journal threshold | 15 |
| novelty and likely impact match | 15 |
| methods, scale, and validation depth | 10 |
| recent same-type comparator fit | 10 |
| readership and scientific value | 10 |
| feasibility of requirements | 5 |
| journal credibility and stable indexing | 5 |

Return one `Stretch`, one `Strong target`, one `Best fit`, one `Safer`, and one `Backup` when the evidence supports those distinctions. For each, show official sources, score components, recent comparators, primary desk-rejection risk, missing upgrades, practical constraints, and confidence. Do not invent impact factors, acceptance rates, APCs, or decision times.

Pause for the user to choose a primary target. Do not mix formatting rules from backup journals into the primary manuscript.

## Journal profile schema

Create `01_journal_profile.json` containing:

- `target_journal`
- `article_type`
- `submission_stage`
- `accessed_at`
- `profile_status`
- `official_sources[]`: `title`, `url`, `accessed_at`, `official`
- `requirements[]`: `id`, `category`, `text`, `source_url`, `applies_to`, `mandatory`, `status`
- `journal_tier`: a reasoned editorial-standard class, not an impact-factor label
- `observed_comparators[]`, when journal benchmarking is requested

Use requirement status `MET`, `NOT_MET`, `NOT_ASSESSABLE`, `NOT_APPLICABLE`, or `PENDING`. If an official rule is inaccessible or conflicting, keep the conflict visible and block a journal-specific pass.

## Required categories

At minimum inspect:

- article type and scope
- word, abstract, reference, figure, and table limits
- manuscript element order
- initial versus revised/final file requirements
- reference style and linked-field policy
- figure, table, extended-data, and supplement requirements
- anonymization and line numbering
- reporting guidelines, statistics, ethics, and registration
- data/code availability and repository requirements
- author contributions, funding, competing interests, and AI-use disclosure
- cover letter, checklist, source data, and other submission-package files
