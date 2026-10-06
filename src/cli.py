import argparse, json
from evaluation.evaluator import DIMENSIONS, summarize

def validate(path):
    n=0
    with open(path, encoding="utf-8") as f:
        for line_no,line in enumerate(f,1):
            x=json.loads(line)
            missing={"id","category","prompt","native_review_required"}-x.keys()
            if missing: raise ValueError(f"Line {line_no}: missing {sorted(missing)}")
            n+=1
    print(f"Validated {n} cases.")

def main():
    p=argparse.ArgumentParser()
    s=p.add_subparsers(dest="command", required=True)
    v=s.add_parser("validate"); v.add_argument("path")
    q=s.add_parser("score"); q.add_argument("values", nargs=7, type=int)
    a=p.parse_args()
    if a.command=="validate": validate(a.path)
    else: print(json.dumps(summarize(dict(zip(DIMENSIONS,a.values))), indent=2))

if __name__=="__main__": main()
