# typing-typevar.py
from typing import TypeVar

from mypy import api as typing_check

T = TypeVar("T")


def return_first_true_element(list_of_element: list[T]) -> T | None:
    """
    Returns the first element in the list that evaluates to True.

    Args:
        list_of_element (list): A list of elements of the same type to evaluate.

    Returns:
        The first element with a truthy value, or None if no such element exists.
    """
    return next((e for e in list_of_element if e), None)


def test_return_first_true_element():
    assert return_first_true_element([0, 0, 5]) == 5
    assert return_first_true_element(["", "foo", "bar"]) == "foo"
    assert return_first_true_element([0, 0, 0]) is None
    assert return_first_true_element(["", "", ""]) is None
    assert return_first_true_element([]) is None

    result = typing_check.run(["exercise.py"])
    assert result[2] == 0, result[0] if result[0] else result[1]
