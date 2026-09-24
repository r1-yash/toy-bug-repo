def is_reorder_needed(stock_level: int, threshold: int) -> bool:
    """Determine if current stock level requires reordering inventory."""
    if stock_level < 0 or threshold < 0:
        raise ValueError("Stock level and threshold must be non-negative")
    # BUG: inverted boolean condition (returns True when stock > threshold)
    return stock_level > threshold
