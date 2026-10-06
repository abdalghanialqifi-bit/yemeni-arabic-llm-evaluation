# Yemeni Arabic LLM Evaluation Benchmark

A reproducible benchmark for evaluating LLMs on Yemeni Arabic, focusing on dialect authenticity, semantic accuracy, context, cultural relevance, naturalness, grammar/morphology, and intent preservation.

## Structure
- `datasets/seed_cases.jsonl` — illustrative starter cases
- `evaluation/rubric.md` — 1–5 scoring rubric and failure categories
- `evaluation/evaluator.py` — validation and scoring utilities
- `prompts/evaluation_prompts.md` — evaluator prompts
- `docs/methodology.md` — methodology and limitations
- `reports/sample_report.json` — result format
- `src/cli.py` — command-line validation/scoring
- `tests/test_evaluator.py` — automated tests

## Important
The seed dataset is illustrative, not a statistically representative sample of Yemeni Arabic. Yemen has regional, social, generational, and situational variation. A serious benchmark should be reviewed by multiple native Yemeni speakers before making empirical claims.

## Quick start
```bash
python -m src.cli validate datasets/seed_cases.jsonl
python -m src.cli score 5 4 4 5 4 4 5
python -m unittest discover -s tests
```

Do not claim model comparisons or benchmark results unless they were actually run.
