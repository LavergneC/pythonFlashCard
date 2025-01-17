# builtin-set-base.py
def count_unique(s: str) -> int:
    """
    Count number of unique charaters in the given string
    """
    # This works fine but it's super slow
    # seen = []
    # for c in s:
    #     if c not in seen:
    #         seen.append(c)
    # return len(seen)

    # way faster
    # seen = set()
    # for c in s:
    #     if c not in seen:
    #         seen.add(c)
    # return len(seen)

    # Does the same with SET comprehension
    # return len({c for c in s})

    # Does the same using set(List) constructor, works with any iterable
    return len(set(s))


def test_count_unique():
    assert count_unique("aabb") == 2
    assert count_unique("abcdef") == 6
