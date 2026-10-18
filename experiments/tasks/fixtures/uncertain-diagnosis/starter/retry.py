def retry_delay(attempt: int, base_delay: float = 0.5, max_delay: float = 8.0) -> float:
    """Compute the retry delay in seconds for a zero-indexed attempt."""
    # Deliberate defects: linear growth and cap is applied before growth.
    return min(max_delay, base_delay) + attempt * base_delay
