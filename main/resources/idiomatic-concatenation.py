# idiomatic-concatenation.py
# From https://realpython.com/lessons/built-in-functions-methods


def concatenate(words: list[str], separator: str = "") -> str:
    """
    return a str with the words list concatenated
    """
    return separator.join(words)


def test_concatenate() -> None:
    assert concatenate(words=["cat", "dog", "horse", "human"]) == "catdoghorsehuman"
    assert (
        concatenate(words=["cat", "dog", "horse", "human"], separator=", ")
        == "cat, dog, horse, human"
    )
