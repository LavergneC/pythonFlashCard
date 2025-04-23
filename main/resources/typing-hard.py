# typing-hard.py
# https://realpython.com/lessons/annotating-callable-objects/
# [Python typing]
from collections.abc import Callable

from mypy import api as typing_check  # fcPython:keep line
from typing_extensions import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def add_plops(func: Callable[P, T]) -> Callable[P, T]:
    """
    Decorator function that add '-plop' to all str type arguments of a given function
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        # Modify all string arguments by appending '-plop'
        modified_args: tuple = tuple(
            arg + "-plop" if isinstance(arg, str) else arg for arg in args
        )
        modified_kwargs: dict = {
            k: v + "-plop" if isinstance(v, str) else v for k, v in kwargs.items()
        }
        return func(*modified_args, **modified_kwargs)

    return wrapper


def test_add_plops() -> None:
    @add_plops
    def multiply_str(str_to_multiply: str, nb_time: int) -> str:
        return " ".join([str_to_multiply for _ in range(nb_time)])

    assert multiply_str("Hello", 1) == "Hello-plop"
    assert multiply_str(str_to_multiply="Hello", nb_time=2) == "Hello-plop Hello-plop"

    result = typing_check.run(["exercise.py"])
    assert result[2] == 0, result[0] if result[0] else result[1]
