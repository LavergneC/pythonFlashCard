from collections import Counter


def top_three_letters(string: str) -> list[tuple[str, int]]:
    """
    Given a string find the three most frequent letters
    This method should return a list of tuples, where the tuple
    contains the character and count
    """
    # Counter(string) returns a dict with:
    #   key = letters in string
    #   value = count
    return Counter(string).most_common(3)


def test_top_three_letters():
    assert top_three_letters("abbcccd") == [("c", 3), ("b", 2), ("a", 1)]
    assert top_three_letters("aabbccd") == [("a", 2), ("b", 2), ("c", 2)]
    assert top_three_letters("aabbbccd") == [("b", 3), ("a", 2), ("c", 2)]
