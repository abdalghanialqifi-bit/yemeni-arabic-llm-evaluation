import argparse, json
from evaluation.evaluator import load_cases, validate_cases, score

parser = argparse.ArgumentParser(description="Yemeni Arabic LLM evaluation benchmark CLI")
sub = parser.add_subparsers(dest="command", required=True)

p_validate = sub.add_parser("validate")
p_validate.add_argument("path")

p_summary = sub.add_parser("summary")
p_summary.add_argument("path")

p_score = sub.add_parser("score")
p_score.add_argument("scores", nargs=7, type=int)

args = parser.parse_args()

if args.command == "validate":
    count = validate_cases(load_cases(args.path))
    print(f"Validated {count} cases.")
elif args.command == "summary":
    cases = load_cases(args.path)
    validate_cases(cases)
    intents = sorted({c["intent"] for c in cases})
    risks = sorted({r for c in cases for r in c["risk_flags"]})
    print(json.dumps({"cases": len(cases), "intents": len(intents), "risk_flags": risks}, ensure_ascii=False, indent=2))
elif args.command == "score":
    print(json.dumps(score(args.scores), indent=2))
