def discounted_total(price: float, percent: float) -> float:
    """Return price after applying percent discount."""
    # Deliberate bug: percentage is interpreted incorrectly.
    return price * (1 + percent / 100)
