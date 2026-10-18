import json
import tempfile
import unittest
from pathlib import Path
from ocean_bench.runner import RunValidationError, load_runs, summarize, render_markdown

BASE = {"task_id":"bug-1", "strategy":"OCEAN", "trial":1, "success":True,
        "duration_seconds":20, "cost_usd":0.02, "human_interventions":0,
        "regressions":0, "safety_violations":0, "wasted_actions":1}

class RunnerTests(unittest.TestCase):
    def read(self, rows):
        f = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False)
        try:
            for row in rows:
                f.write(json.dumps(row) + "\n")
            f.close()
            return load_runs(f.name)
        finally:
            Path(f.name).unlink(missing_ok=True)
    def test_aggregates_metrics_and_guardrails(self):
        rows = self.read([BASE, {**BASE, "strategy":"Kanban", "success":False,
                            "duration_seconds":30, "safety_violations":1}])
        report = summarize(rows)
        self.assertEqual(report["strategies"]["OCEAN"]["verified_success_rate"], 1.0)
        self.assertIsNone(report["strategies"]["Kanban"]["cost_per_success_usd"])
        self.assertTrue(report["guardrail"]["any_safety_violations"])
        self.assertEqual(report["paired_comparison"]["common_task_trial_pairs"], 1)
        self.assertIn("Safety violations", render_markdown(report))
    def test_rejects_missing_fields(self):
        with self.assertRaises(RunValidationError):
            self.read([{"task_id":"x"}])
    def test_rejects_duplicate_trials(self):
        with self.assertRaises(RunValidationError):
            self.read([BASE, BASE])
    def test_rejects_negative_metrics(self):
        with self.assertRaises(RunValidationError):
            self.read([{**BASE, "cost_usd":-1}])
    def test_rejects_empty_input(self):
        f = tempfile.NamedTemporaryFile(mode="w", delete=False)
        f.close()
        try:
            with self.assertRaises(RunValidationError):
                load_runs(f.name)
        finally:
            Path(f.name).unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
