# abstract-Base-Classes.py
# from https://realpython.com/lessons/using-abstract-base-classes/

from abc import ABC, abstractmethod
from io import StringIO  # fcPython:keep line
from unittest.mock import patch  # fcPython:keep line

TROPICAL_PLANTS_DRY_LIMIT = 80
PERENNIAL_PLANTS_DEY_LIMIT = 20


class Plant(ABC):
    def __init__(self):
        self.water_level = 0

    @abstractmethod
    def is_dry(self) -> bool:
        raise NotImplementedError("is_dry() must be implemented")

    @abstractmethod
    def water(self, water_quantity: int) -> None:
        raise NotImplementedError("water() must be implemented")


class TropicalPlant(Plant):
    def is_dry(self) -> bool:
        return self.water_level < TROPICAL_PLANTS_DRY_LIMIT

    def water(self, water_quantity: int):
        print("Spraying the tropical plant")
        self.water_level += water_quantity


class PerennialPlant(Plant):
    def is_dry(self) -> bool:
        return self.water_level < PERENNIAL_PLANTS_DEY_LIMIT

    def water(self, water_quantity: int):
        print("Putting water under the perennial plant")
        self.water_level += water_quantity


@patch("sys.stdout", new_callable=StringIO)
def test_water_the_plants(fake_out) -> None:
    monstera = TropicalPlant()
    cactus = PerennialPlant()

    plants = [monstera, cactus]

    while any(plant.is_dry() for plant in plants):
        _water_the_plants(plants)

    assert fake_out.getvalue() == (
        "Spraying the tropical plant\n"
        "Putting water under the perennial plant\n"
        "Spraying the tropical plant\n"
    )


def _water_the_plants(plants: list[Plant]) -> None:
    for plant in plants:
        if plant.is_dry():
            plant.water(water_quantity=50)
