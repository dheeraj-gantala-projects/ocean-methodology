"""Deterministic harness test double. Never use as methodology benchmark data."""
import json
import os
from pathlib import Path

task = os.environ["OCEAN_TASK_ID"]
solutions = {
    "simple-bug-fix": '''def discounted_total(price: float, percent: float) -> float:
    if price < 0 or percent < 0 or percent > 100:
        raise ValueError("invalid price or percent")
    return price * (1 - percent / 100)
''',
    "uncertain-diagnosis": '''def retry_delay(attempt: int, base_delay: float = 0.5, max_delay: float = 8.0) -> float:
    if attempt < 0 or base_delay <= 0 or max_delay <= 0:
        raise ValueError("invalid retry parameters")
    return min(max_delay, base_delay * (2 ** attempt))
''',
    "dependency-heavy-feature": '''import re

def slugify(text: str, max_length: int = 80) -> str:
    if max_length < 1:
        raise ValueError("max_length must be positive")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", text).lower().strip("-")
    return value[:max_length].rstrip("-")
'''
}
target = {"simple-bug-fix":"discount.py", "uncertain-diagnosis":"retry.py",
          "dependency-heavy-feature":"slug.py"}[task]
Path(target).write_text(solutions[task], encoding="utf-8")
Path(os.environ["OCEAN_RUN_METADATA_PATH"]).write_text(json.dumps({
    "cost_usd": 0.01, "input_tokens": 100, "output_tokens": 20,
    "human_interventions": 0, "wasted_actions": 0
}), encoding="utf-8")
print("Harness test double wrote a known-good solution.")
