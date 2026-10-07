"""Core validation and scoring utilities for the benchmark."""
import json
from pathlib import Path

DIMENSIONS = [
    "dialect_authenticity", "semantic_accuracy", "contextual_understanding",
    "cultural_relevance", "naturalness", "grammar_morphology", "intent_preservation"
]
FAILURE_CATEGORIES = [
    "DIALECT_MISMATCH", "MSA_OVERUSE", "CULTURAL_MISMATCH", "INTENT_ERROR",
    "LITERAL_TRANSLATION", "UNNATURAL_PHRASE", "GRAMMAR_ERROR", "UNSAFE_OR_INAPPROPRIATE"
]


def load_cases(path):
    rows = []
    for line_no, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON on line {line_no}: {exc}") from exc
    return rows


def validate_cases(cases):
    required = {"id", "region", "intent", "user_input", "evaluation_targets", "risk_flags"}
    ids = set()
    for i, case in enumerate(cases, 1):
        missing = required - set(case)
        if missing:
            raise ValueError(f"Case {i} missing fields: {sorted(missing)}")
        if case["id"] in ids:
            raise ValueError(f"Duplicate case id: {case['id']}")
        ids.add(case["id"])
        if not isinstance(case["evaluation_targets"], list):
            raise ValueError(f"{case['id']}: evaluation_targets must be a list")
        if not isinstance(case["risk_flags"], list):
            raise ValueError(f"{case['id']}: risk_flags must be a list")
    return len(cases)


def score(values):
    if len(values) != len(DIMENSIONS):
        raise ValueError(f"Expected {len(DIMENSIONS)} scores")
    if any(not isinstance(v, int) or not 1 <= v <= 5 for v in values):
        raise ValueError("Scores must be integers from 1 to 5")
    total = sum(values)
    return {"total": total, "max_total": len(DIMENSIONS) * 5, "average": round(total / len(DIMENSIONS), 2)}
