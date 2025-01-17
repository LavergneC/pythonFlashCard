# itertools-cycle.py
import itertools as it


def build_strips_pattern(colors: list[str], length=int) -> list[str]:
    """
    Given a list of colors eq: ['red, 'blue'...] Build a pattern by looping
    on the colors
    """
    pattern = []
    cycle = it.cycle(colors)

    while len(pattern) < length:
        pattern.append(next(cycle))

    return pattern


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
