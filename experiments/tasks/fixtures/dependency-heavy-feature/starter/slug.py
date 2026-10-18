import re

def slugify(text: str, max_length: int = 80) -> str:
    """Create a normalized, bounded URL slug."""
    # Deliberate defects: does not normalize runs and truncation can end with '-'.
    value = re.sub(r"[^a-zA-Z0-9]", "-", text).lower()
    return value[:max_length]
