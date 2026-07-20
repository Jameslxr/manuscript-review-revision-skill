#!/usr/bin/env python3
"""Calculate frozen-rubric benchmark scores and two-run stability."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path


SCORE_COLUMNS = {
    "system",
    "run_id",
    "detected_issue_ids",
    "unsupported_concern_count",
    "precision_non_invention",
    "traceability",
    "resolution_quality",
    "consistency",
    "journal_calibration",
    "auditability",
    "posture",
    "notes",
}
RANGES = {
    "precision_non_invention": (0.0, 20.0),
    "traceability": (0.0, 15.0),
    "resolution_quality": (0.0, 10.0),
    "consistency": (0.0, 10.0),
    "journal_calibration": (0.0, 10.0),
    "auditability": (0.0, 5.0),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("answer_key", type=Path)
    parser.add_argument("run_scores", type=Path)
    parser.add_argument("--expected-runs", type=int, default=2)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def read_tsv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            fields = set(reader.fieldnames or [])
            rows = [
                {str(key): str(value or "").strip() for key, value in row.items()}
                for row in reader
            ]
    except OSError as exc:
        return [], [f"Unable to read {path}: {exc}"]
    if not rows:
        errors.append(f"{path} contains no rows.")
    return rows, errors


def parse_issue_ids(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def calculate(
    answer_rows: list[dict[str, str]],
    score_rows: list[dict[str, str]],
    expected_runs: int,
) -> dict[str, object]:
    errors: list[str] = []
    issue_weights: dict[str, int] = {}
    for row_number, row in enumerate(answer_rows, start=2):
        issue_id = row.get("issue_id", "")
        try:
            weight = int(row.get("weight", ""))
        except ValueError:
            errors.append(f"answer key row {row_number}: weight must be an integer.")
            continue
        if not issue_id or issue_id in issue_weights:
            errors.append(
                f"answer key row {row_number}: issue_id is empty or duplicated."
            )
        elif weight <= 0:
            errors.append(f"answer key row {row_number}: weight must be positive.")
        else:
            issue_weights[issue_id] = weight
    total_weight = sum(issue_weights.values())
    if not total_weight:
        errors.append("Answer key has no positive issue weight.")

    systems: dict[str, list[dict[str, object]]] = defaultdict(list)
    seen_runs: set[tuple[str, str]] = set()
    for row_number, row in enumerate(score_rows, start=2):
        missing = SCORE_COLUMNS - row.keys()
        if missing:
            errors.append(f"score row {row_number}: missing columns {sorted(missing)}.")
            continue
        system = row["system"]
        run_id = row["run_id"]
        if not system or not run_id:
            errors.append(f"score row {row_number}: system and run_id are required.")
            continue
        run_key = (system, run_id)
        if run_key in seen_runs:
            errors.append(f"score row {row_number}: duplicate run {run_key}.")
        seen_runs.add(run_key)

        detected = parse_issue_ids(row["detected_issue_ids"])
        unknown = detected - issue_weights.keys()
        if unknown:
            errors.append(
                f"score row {row_number}: unknown issue IDs {sorted(unknown)}."
            )
        try:
            unsupported = int(row["unsupported_concern_count"])
        except ValueError:
            errors.append(
                f"score row {row_number}: unsupported_concern_count must be integer."
            )
            unsupported = 0
        if unsupported < 0:
            errors.append(
                f"score row {row_number}: unsupported_concern_count cannot be negative."
            )

        component_scores: dict[str, float] = {}
        for field, (minimum, maximum) in RANGES.items():
            try:
                value = float(row[field])
            except ValueError:
                errors.append(f"score row {row_number}: {field} must be numeric.")
                value = 0.0
            if not minimum <= value <= maximum:
                errors.append(
                    f"score row {row_number}: {field} must be from "
                    f"{minimum:g} to {maximum:g}."
                )
            component_scores[field] = value

        detected_weight = sum(issue_weights.get(item, 0) for item in detected)
        recall_score = 30.0 * detected_weight / total_weight if total_weight else 0.0
        total_score = recall_score + sum(component_scores.values())
        systems[system].append(
            {
                "run_id": run_id,
                "detected_issue_ids": sorted(detected),
                "detected_weight": detected_weight,
                "recall_score": round(recall_score, 3),
                "unsupported_concern_count": unsupported,
                **component_scores,
                "total_score": round(total_score, 3),
                "posture": row["posture"],
                "notes": row["notes"],
            }
        )

    for system, runs in systems.items():
        if len(runs) != expected_runs:
            errors.append(
                f"{system}: expected {expected_runs} runs, found {len(runs)}."
            )

    summaries: dict[str, object] = {}
    for system, runs in sorted(systems.items()):
        runs = sorted(runs, key=lambda item: str(item["run_id"]))
        average = (
            sum(float(run["total_score"]) for run in runs) / len(runs)
            if runs
            else 0.0
        )
        detected_sets = [set(run["detected_issue_ids"]) for run in runs]
        if len(detected_sets) == 2:
            union = detected_sets[0] | detected_sets[1]
            issue_jaccard = (
                len(detected_sets[0] & detected_sets[1]) / len(union) if union else 1.0
            )
            posture_agreement = runs[0]["posture"] == runs[1]["posture"]
            score_spread = abs(
                float(runs[0]["total_score"]) - float(runs[1]["total_score"])
            )
        else:
            issue_jaccard = None
            posture_agreement = None
            score_spread = None
        summaries[system] = {
            "average_total_score": round(average, 3),
            "issue_jaccard": (
                round(issue_jaccard, 3) if issue_jaccard is not None else None
            ),
            "posture_agreement": posture_agreement,
            "total_score_spread": (
                round(score_spread, 3) if score_spread is not None else None
            ),
            "runs": runs,
        }

    return {
        "status": "PASS" if not errors else "FAIL",
        "answer_key_issue_count": len(issue_weights),
        "answer_key_total_weight": total_weight,
        "systems": summaries,
        "errors": errors,
    }


def render_text(report: dict[str, object]) -> str:
    lines = [f"Benchmark score validation: {report['status']}"]
    systems = report.get("systems", {})
    if isinstance(systems, dict):
        for system, summary in systems.items():
            if not isinstance(summary, dict):
                continue
            lines.extend(
                [
                    f"{system}: {summary.get('average_total_score', 0):.3f}/100",
                    f"  issue Jaccard: {summary.get('issue_jaccard')}",
                    f"  posture agreement: {summary.get('posture_agreement')}",
                    f"  score spread: {summary.get('total_score_spread')}",
                ]
            )
    for error in report.get("errors", []):
        lines.append(f"ERROR: {error}")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    answer_rows, answer_errors = read_tsv(args.answer_key)
    score_rows, score_errors = read_tsv(args.run_scores)
    report = calculate(answer_rows, score_rows, args.expected_runs)
    report["errors"] = answer_errors + score_errors + list(report["errors"])
    if report["errors"]:
        report["status"] = "FAIL"
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_text(report))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
