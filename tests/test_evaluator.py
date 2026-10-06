import unittest
from evaluation.evaluator import DIMENSIONS, summarize

class TestEvaluator(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(summarize({d:5 for d in DIMENSIONS})["average"],5.0)
    def test_invalid(self):
        x={d:5 for d in DIMENSIONS}; x["naturalness"]=6
        with self.assertRaises(ValueError): summarize(x)
