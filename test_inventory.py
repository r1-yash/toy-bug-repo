import pytest
from inventory import is_reorder_needed


def test_is_reorder_needed_above_threshold():
    # Stock level 10, threshold 5 -> No reorder needed (False)
    # FAILS on buggy code (returns True)
    assert is_reorder_needed(10, 5) is False


def test_is_reorder_needed_below_threshold():
    # Stock level 2, threshold 5 -> Reorder needed (True)
    # FAILS on buggy code (returns False)
    assert is_reorder_needed(2, 5) is True


def test_is_reorder_needed_at_threshold():
    # Stock level 5, threshold 5 -> Reorder needed (True)
    # FAILS on buggy code (returns False)
    assert is_reorder_needed(5, 5) is True


def test_is_reorder_needed_negative_values():
    with pytest.raises(ValueError):
        is_reorder_needed(-1, 5)
