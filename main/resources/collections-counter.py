from collections import defaultdict
from collections import Counter


def top_three_letters_best_solution(string):
    """
    Given a string find the three most frequent letters
    This method should return a list of tuples, where the tuple
    contains the character and count
    >>> top_three_letters_best_solution("abbcccd")
    [('c', 3), ('b', 2), ('a', 1)]
    >>> top_three_letters_best_solution("aabbccd")
    [('a', 2), ('b', 2), ('c', 2)]
    >>> top_three_letters_best_solution("aabbbccd")
    [('b', 3), ('a', 2), ('c', 2)]
    """
    # Counter(string) returns a dict with:
    #   key = letters in string
    #   value = count

    return Counter(string).most_common(3)


def top_three_letters(string):
    """
    Same as before
    >>> top_three_letters("abbcccd")
    [('c', 3), ('b', 2), ('a', 1)]
    >>> top_three_letters("aabbccd")
    [('a', 2), ('b', 2), ('c', 2)]
    >>> top_three_letters("aabbbccd")
    [('b', 3), ('a', 2), ('c', 2)]
    """
    letters_frequency = defaultdict(int)  # 0 by default
    for letter in string:
        letters_frequency[letter] += 1

    top_three_letters = sorted(
        letters_frequency,
        key=lambda k: letters_frequency[k],
        reverse=True,
    )[:3]

    return [(letter, letters_frequency[letter]) for letter in top_three_letters]
