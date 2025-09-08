import pytest


class Podium:
    """Stores 3 same type objects. Used for a podium display.

    Objects are added using the add() method and will be ranked using the
    add() call order.
    """

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return ""

    def add(self, contestant) -> None:
        pass

    ##############################################
    # Fill all the previous function definitions #
    # in order to make the test pass.            #
    # Feel free to add some private function     #
    ##############################################

# The following section contains all the tests used to validate your response
# Test your solution by running '$ pytest exercise.py'
def test_podium_simple():
    people_podium = Podium()
    people_podium.add("Alice")
    people_podium.add("Bob")
    people_podium.add("Clement")

    assert str(people_podium) == "\n".join(
        ["🎖 First: Alice", "🥈 Second: Bob", "🥉 Third: Clement"]
    )

    best_numbers = Podium()
    best_numbers.add(42)
    best_numbers.add(123)
    best_numbers.add(10)

    assert str(best_numbers) == "\n".join(
        ["🎖 First: 42", "🥈 Second: 123", "🥉 Third: 10"]
    )


def test_podium_runtime_errors():
    best_booleans = Podium()
    best_booleans.add(True)
    best_booleans.add(False)

    with pytest.raises(
        RuntimeError, match="Needs exactly 3 contestants to print podium"
    ):
        str(best_booleans)

    best_booleans.add(False)
    best_booleans.add(False)

    with pytest.raises(
        RuntimeError, match="Needs exactly 3 contestants to print podium"
    ):
        str(best_booleans)
