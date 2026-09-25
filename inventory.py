def is_reorder_needed(stock_level, threshold):
    if stock_level < 0 or threshold < 0:
        raise ValueError("Stock level and threshold cannot be negative")
    return stock_level <= threshold
