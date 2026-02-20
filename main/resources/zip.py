# zip.py


def roman_to_decimal(roman_number: str) -> int:
    """
    Takes a roman number as an input and returns its int value.

    Values are :
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,

    • The maximum number of times a Roman numeral can be repeated is three.
    • The main Roman numbers that can be repeated are I, X, C, and M.
    • V, L, and D cannot be repeated.

    The addition rule applies when the base Roman numeral is followed (on its right) by an equal or smaller.
    eq.: LVI = 50 + 5 + 1 = 56

    The Subtraction rule applies when the base Roman numeral is followed (on its right) by a larger number. The principle of subtraction is as follows.
    • Each subtraction can only be performed once on the same number.
    • I can only be used to subtract V and X.
    • X can only be used to subtract L and C.
    • C can only be used to subtract D and M
    """
    ROMAN_DICT: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    values: list[int] = [ROMAN_DICT[current_symbol] for current_symbol in roman_number]

    return sum(
        [
            current_value if current_value >= next_value else -current_value
            for current_value, next_value in zip(values, values[1:] + [0])
        ]
    )


def test_roman_to_decimal():
    # Simple additions
    assert roman_to_decimal("I") == 1
    assert roman_to_decimal("II") == 2
    assert roman_to_decimal("XIII") == 13

    # Subtractions
    assert roman_to_decimal("IV") == 4
    assert roman_to_decimal("CXIV") == 114
    assert roman_to_decimal("CM") == 900

    # Mixed
    assert roman_to_decimal("XLVIII") == 48
    assert roman_to_decimal("XLIX") == 49
    assert roman_to_decimal("XCIX") == 99
    assert roman_to_decimal("MMXLVIII") == 2048
    assert roman_to_decimal("CCCXCVIII") == 398
