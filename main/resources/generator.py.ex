import pytest
from mypy import api as typing_check


def storage_manager(storage_capacity):
    """
    A generator function that manages a storage system with a given capacity.
    It allows adding or removing quantities from the storage and ensures that
    the storage does not exceed its capacity or go below zero.

    Args:
        storage_capacity: The maximum capacity of the storage.

    Yields:
        The remaining capacity of the storage after each operation.

    Receives:
        tuple: A tuple containing an 'operation' and a 'quantity'.
                        'operation' can be '+' to add or '-' to remove
                        'quantity' is an int.

    Returns:
        str: A message indicating an error, such as an invalid operation,
             storage overflow, or storage < 0.

    Raises:
        StopIteration: When an invalid operation is provided or the storage
                       exceeds its capacity or goes below zero.
    """
    ##################
    # Your code here #
    ##################


# The following section should not be modified.
# It contains all the tests used to validate your response
# Test your solution by running '$ pytest exercise.py'
def test_storage_manager() -> None:
    warehouse = storage_manager(storage_capacity=100)

    assert next(warehouse) == 100

    assert warehouse.send(("+", 60)) == 40
    assert warehouse.send(("-", 5)) == 45

    with pytest.raises(StopIteration, match="Storage capacity overflow"):
        warehouse.send(("+", 50))

    garage = storage_manager(storage_capacity=10)
    assert next(garage) == 10

    with pytest.raises(StopIteration, match="Storage capacity < 0"):
        garage.send(("-", 15))

    result = typing_check.run(["exercise.py"])
    assert result[2] == 0, result[0] if result[0] else result[1]
