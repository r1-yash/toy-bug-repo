def calculate_discount(price: float, age: int) -> float:
    """Calculate final price after applying senior discount for age 65 and older."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age > 65:  # BUG: wrong comparison operator, should be age >= 65
        return round(price * 0.80, 2)
    return round(price, 2)
