import pytest
from calc import calculate_discount


def test_calculate_discount_standard():
    assert calculate_discount(100.0, 30) == 100.0


def test_calculate_discount_senior_over_65():
    assert calculate_discount(100.0, 70) == 80.0


def test_calculate_discount_senior_exact_65():
    # FAILS on buggy code (returns 100.0 instead of 80.0)
    assert calculate_discount(100.0, 65) == 80.0


def test_calculate_discount_invalid_input():
    with pytest.raises(ValueError):
        calculate_discount(-10.0, 25)
    with pytest.raises(ValueError):
        calculate_discount(100.0, -5)
