import pytest
from validator import validate_username


def test_validate_username_valid():
    assert validate_username("alice123") is True


def test_validate_username_invalid_length():
    assert validate_username("ab") is False
    assert validate_username("a" * 25) is False


def test_validate_username_special_chars():
    assert validate_username("user@name") is False


def test_validate_username_none_input():
    # FAILS on buggy code (raises TypeError instead of ValueError)
    with pytest.raises(ValueError):
        validate_username(None)
