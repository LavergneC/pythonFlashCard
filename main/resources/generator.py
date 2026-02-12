# generator.py

from typing import Generator

import pytest
from mypy import api as typing_check


def storage_manager(storage_capacity: int) -> Generator[int, tuple[str, int], str]:
    """
    A generator function that manages a storage system with a given capacity.
    It allows adding or removing quantities from the storage and ensures that
    the storage does not exceed its capacity or go below zero.

    Args:
        storage_capacity (int): The maximum capacity of the storage.

    Yields:
        int: The remaining capacity of the storage after each operation.

    Receives:
        tuple[str, int]: A tuple containing an operation and a quantity.
                         The operation can be '+' to add or '-' to remove
                         the specified quantity.
    Returns:
        str: A message indicating an error, such as an invalid operation,
             storage overflow, or storage < 0.

    Raises:
        StopIteration: When an invalid operation is provided or the storage
                       exceeds its capacity or goes below zero.
    """
    current_quantity: int = 0

    while True:
        operation, quantity = yield storage_capacity - current_quantity

        if operation == "+":
            current_quantity += quantity
        elif operation == "-":
            current_quantity -= quantity
        else:
            return "Bad operation provided"

        if current_quantity > storage_capacity:
            return "Storage capacity overflow"
        if current_quantity < 0:
            return "Storage capacity < 0"


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

    box = storage_manager(storage_capacity=33)
    next(box)

    with pytest.raises(StopIteration, match="Bad operation provided"):
        box.send(("=", 2))

    result = typing_check.run(["exercise.py"])
    assert result[2] == 0, result[0] if result[0] else result[1]
