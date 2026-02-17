# itertools-cycle.py
from itertools import cycle, islice

import pytest


def build_strips_pattern(colors: list[str], length: int) -> list[str]:
    """
    Given a list of colors eq: ['red, 'blue'...] Build a pattern by looping
    on the colors
    """
    if not colors:
        raise ValueError("`colors` must be a non-empty list")
    if length < 0:
        raise ValueError("`length` must be non-negative")
    return list(islice(cycle(colors), length))


def test_build_strips_pattern_simple_even():
    assert build_strips_pattern(["Red", "White"], 6) == [
        "Red",
        "White",
        "Red",
        "White",
        "Red",
        "White",
    ]


def test_build_strips_pattern_simple_odd():
    assert build_strips_pattern(["Red", "White"], 5) == [
        "Red",
        "White",
        "Red",
        "White",
        "Red",
    ]


def test_build_strips_pattern_more_complexe_pattern():
    assert build_strips_pattern(["Blue", "White", "Red"], 10) == [
        "Blue",
        "White",
        "Red",
        "Blue",
        "White",
        "Red",
        "Blue",
        "White",
        "Red",
        "Blue",
    ]


def test_build_strips_pattern_raises():
    with pytest.raises(ValueError, match="`colors` must be a non-empty list"):
        build_strips_pattern([], 4)

    with pytest.raises(ValueError, match="`length` must be non-negative"):
        build_strips_pattern(["Red", "White"], -1)
