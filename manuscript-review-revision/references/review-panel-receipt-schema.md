# Review-panel receipt schema 2.0

Use this schema for `03_review_panel_plan.json`. The panel validator treats
missing receipt fields as failure. If a host cannot expose a task identity or
equivalent execution log, record that limitation in the verdict and mark the
panel gate `NOT ASSESSABLE`; do not invent a task ID.

## Top-level fields

| Field | Requirement |
|---|---|
| `panel_schema_version` | exactly `2.0` |
| `skill_version` | semantic version, for example `1.3.0` |
| `host` | host name, for example `Codex` or `Claude Code` |
| `host_version` | observed version or `NOT_EXPOSED` |
| `target_journal` | exact journal name |
| `article_type` | resolved article type |
| `manuscript_sha256` | frozen manuscript digest |
| `journal_profile_sha256` | frozen journal-profile digest |
| `shared_fact_base_sha256` | non-evaluative shared-fact-base digest |
| `execution_mode` | exactly `independent_agents` |
| `root_is_reviewer` | exactly `false` |
| `synthesis_started_before_reviews_completed` | exactly `false` |
| `reviewers` | at least five reviewer receipt objects |

## Reviewer receipt fields

| Field | Requirement |
|---|---|
| `agent_id` | unique host-visible Agent identifier |
| `host_task_id` | unique host task ID or execution-log identity |
| `receipt_source` | `HOST_NATIVE` or `HOST_LOG` |
| `context_mode` | exactly `FRESH_NON_FORK` |
| `role_id` | unique functional role ID |
| `role` | readable role label |
| `independent` | exactly `true` |
| `saw_other_reviews` | exactly `false` |
| `status` | `COMPLETED` or `NOT_ASSESSABLE` |
| `started_at`, `completed_at` | ISO-8601 timestamps with timezone |
| `input_hashes` | the three top-level frozen hashes, unchanged |
| `report_path` | non-empty saved report |
| `report_sha256` | digest of the saved report |

## JSON fragment

The following shows one reviewer receipt. Repeat the object for all required
roles; a one-reviewer panel will not pass validation.

```json
{
  "panel_schema_version": "2.0",
  "skill_version": "1.3.0",
  "host": "Codex",
  "host_version": "NOT_EXPOSED",
  "target_journal": "Exact Journal Name",
  "article_type": "Original Article",
  "manuscript_sha256": "<64-hex-digest>",
  "journal_profile_sha256": "<64-hex-digest>",
  "shared_fact_base_sha256": "<64-hex-digest>",
  "execution_mode": "independent_agents",
  "root_is_reviewer": false,
  "synthesis_started_before_reviews_completed": false,
  "reviewers": [
    {
      "agent_id": "<host-agent-id>",
      "host_task_id": "<host-task-id>",
      "receipt_source": "HOST_NATIVE",
      "context_mode": "FRESH_NON_FORK",
      "role_id": "journal-priority",
      "role": "Journal priority and editorial fit",
      "independent": true,
      "saw_other_reviews": false,
      "status": "COMPLETED",
      "started_at": "2026-07-19T10:00:00-05:00",
      "completed_at": "2026-07-19T10:15:00-05:00",
      "input_hashes": {
        "manuscript_sha256": "<same-64-hex-digest>",
        "journal_profile_sha256": "<same-64-hex-digest>",
        "shared_fact_base_sha256": "<same-64-hex-digest>"
      },
      "report_path": "reviews/reviewer_01.md",
      "report_sha256": "<actual-report-64-hex-digest>"
    }
  ]
}
```

Run:

```bash
python3 "$SKILL_ROOT/scripts/validate_review_panel.py" \
  03_review_panel_plan.json
```

The validator checks recorded receipts and saved artifacts. It cannot
cryptographically attest to a proprietary host's internal execution.
