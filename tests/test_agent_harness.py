import sys
import unittest
from pathlib import Path
from experiments.run_agent import ROOT, run_one

class AgentHarnessTests(unittest.TestCase):
    def test_known_good_test_double_passes_hidden_evaluator(self):
        command = f"{sys.executable} {ROOT / 'testing' / 'fake_agent.py'}"
        for task in ("simple-bug-fix", "uncertain-diagnosis", "dependency-heavy-feature"):
            with self.subTest(task=task):
                result = run_one(task, "ocean", command, trial=1, timeout=10)
                self.assertTrue(result["success"], result["evaluator_output"])
                self.assertTrue(result["cost_measured"])
                self.assertEqual(result["safety_violations"], 0)

if __name__ == "__main__":
    unittest.main()
