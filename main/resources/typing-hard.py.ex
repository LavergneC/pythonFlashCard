from mypy import api as typing_check


def add_plops(func):
    """
    Decorator function that add '-plop' to all str type arguments of a given function
    """
    ##################
    # Your code here #
    ##################


# The following section should not be modified.
# It contains all the tests used to validate your response
# Test your solution by running '$ pytest exercise.py'
def test_add_plops() -> None:
    @add_plops
    def multiply_str(str_to_multiply: str, nb_time: int) -> str:
        return " ".join([str_to_multiply for _ in range(nb_time)])

    assert multiply_str("Hello", 1) == "Hello-plop"
    assert multiply_str(str_to_multiply="Hello", nb_time=2) == "Hello-plop Hello-plop"

    result = typing_check.run(["exercise.py"])
    assert result[2] == 0, result[0] if result[0] else result[1]
