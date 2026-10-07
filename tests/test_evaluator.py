import json, tempfile, unittest
from evaluation.evaluator import load_cases, validate_cases, score

class EvaluatorTests(unittest.TestCase):
    def test_score(self):
        result = score([5,4,4,5,4,4,5])
        self.assertEqual(result["total"], 31)
        self.assertEqual(result["max_total"], 35)
        self.assertEqual(result["average"], 4.43)

    def test_validate_dataset(self):
        path = "datasets/seed_cases.jsonl"
        cases = load_cases(path)
        self.assertEqual(validate_cases(cases), 24)
        self.assertEqual(len({c["id"] for c in cases}), 24)

if __name__ == "__main__":
    unittest.main()
