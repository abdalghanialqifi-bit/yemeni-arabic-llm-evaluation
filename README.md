# Yemeni Arabic LLM Evaluation Benchmark

A reproducible, human-review-oriented benchmark scaffold for evaluating LLM responses to Yemeni Arabic.

## Evaluation dimensions
- Dialect authenticity
- Semantic accuracy
- Contextual understanding
- Cultural relevance
- Naturalness
- Grammar / morphology
- Intent preservation

## Failure taxonomy
`DIALECT_MISMATCH`, `MSA_OVERUSE`, `CULTURAL_MISMATCH`, `INTENT_ERROR`, `LITERAL_TRANSLATION`, `UNNATURAL_PHRASE`, `GRAMMAR_ERROR`, `UNSAFE_OR_INAPPROPRIATE`

## Repository structure
- `datasets/seed_cases.jsonl` — 24 candidate cases for expert review
- `evaluation/rubric.md` — scoring rubric and failure taxonomy
- `evaluation/evaluator.py` — validation and scoring utilities
- `prompts/evaluation_prompts.md` — structured evaluator prompt templates
- `docs/methodology.md` — methodology, review protocol, and limitations
- `reports/sample_report.json` — report schema/example
- `src/cli.py` — command-line interface
- `tests/` — automated tests

## Quick start
```bash
python -m src.cli validate datasets/seed_cases.jsonl
python -m src.cli summary datasets/seed_cases.jsonl
python -m src.cli score 5 4 4 5 4 4 5
python -m unittest discover -s tests
```

## Important methodological note
The seed cases are **candidate evaluation items, not a validated gold-standard dataset**. Yemeni Arabic varies by region, community, age, setting, and speaker. Before using the dataset for model ranking or publishing quantitative claims, each case should be reviewed by multiple qualified Yemeni Arabic speakers and disagreements should be documented.

No model benchmark result is claimed in this repository unless it was actually produced by running the evaluation protocol and recorded in a report.
