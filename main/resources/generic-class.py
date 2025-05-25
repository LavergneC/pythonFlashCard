import pytest


class Podium[T]:
    """Stores 3 same type object for a str podium.

    Objects are added using the add() method and will be rank using the
    add() call order.
    """

    def __init__(self) -> None:
        self.contestants: list[T] = []

    def __str__(self) -> str:
        if len(self.contestants) < 3:
            raise RuntimeError("Needs 3 contestants to print podium")

        return f"🎖 First: {self.contestants[0]}\n🥈 Second: {self.contestants[1]}\n🥉 Third: {self.contestants[2]}"

    def add(self, contestant: T) -> None:
        self.contestants.append(contestant)


def test_podium():
    people_podium = Podium[str]()
    people_podium.add("Alice")
    people_podium.add("Bob")
    people_podium.add("Clement")

    assert str(people_podium) == "\n".join(
        ["🎖 First: Alice", "🥈 Second: Bob", "🥉 Third: Clement"]
    )

    best_numbers = Podium[int]()
    best_numbers.add(42)
    best_numbers.add(123)
    best_numbers.add(10)

    assert str(best_numbers) == "\n".join(
        ["🎖 First: 42", "🥈 Second: 123", "🥉 Third: 10"]
    )

    best_booleans = Podium[bool]()
    best_booleans.add(True)
    best_booleans.add(False)

    with pytest.raises(RuntimeError, match="Needs 3 contestants to print podium"):
        str(best_booleans)
