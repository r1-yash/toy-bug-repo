import pytest
from parser import parse_lines


def test_parse_lines_empty():
    assert parse_lines("") == []


def test_parse_lines_single_line():
    # FAILS on buggy code (range(0) produces empty list)
    assert parse_lines("hello") == ["hello"]


def test_parse_lines_multiple_lines():
    text = "line1\n  line2  \nline3"
    # FAILS on buggy code (returns ["line1", "line2"], omitting "line3")
    assert parse_lines(text) == ["line1", "line2", "line3"]


def test_parse_lines_with_whitespace_lines():
    text = "  apple  \n  \n  banana  "
    assert parse_lines(text) == ["apple", "banana"]
