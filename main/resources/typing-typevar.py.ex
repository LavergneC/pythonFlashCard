from mypy import api as typing_check


def return_first_true_element(list_of_element):
    """
    Returns the first element of the same type in the list that evaluates to True.

    Args:
        list_of_element (list): A list of elements of the same type to evaluate.

    Returns:
        The first element with a truthy value, or None if no such element exists.
    """
    ##################
    # Your code here #
    ##################


# The following section should not be modified.
# It contains all the tests used to validate your response
# Test your solution by running '$ pytest exercise.py'
def test_return_first_true_element():
    assert return_first_true_element([0, 0, 5]) == 5
    assert return_first_true_element(["", "foo", "bar"]) == "foo"
    assert return_first_true_element([0, 0, 0]) is None
    assert return_first_true_element(["", "", ""]) is None
    assert return_first_true_element([]) is None

    result = typing_check.run(["exercise.py"])
    assert result[2] == 0, result[0] if result[0] else result[1]
