def calculate_discount(price, age):
    if not isinstance(price, (int, float)) or not isinstance(age, int):
        raise ValueError("Invalid input types")
    if price < 0 or age < 0:
        raise ValueError("Price and age must be non-negative")
    if age >= 65:
        return price * 0.8
    return price
