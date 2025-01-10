from collections import Counter


def majority_element_indexes(lst):
    """
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times with n the length of lst.
    If there is no majority element, return []
    """
    majority_tuple_list = Counter(lst).most_common(1)
    if majority_tuple_list is None or not len(majority_tuple_list):
        return []

    majority_element, majority_element_count = majority_tuple_list[0]

    if majority_element_count <= len(lst) // 2:
        return []

    return [index for index, value in enumerate(lst) if value == majority_element]


def test_majority_element_indexes():
    assert majority_element_indexes([1, 1, 2]) == [0, 1]
    assert majority_element_indexes([1, 1, 2, 3, 4]) == []
    assert majority_element_indexes([1, 2]) == []
    assert majority_element_indexes([1]) == [0]
    assert majority_element_indexes([]) == []
