import random  # fcPython:keep line
from collections import defaultdict
from dataclasses import dataclass


class MeteoData:
    def __init__(self, initial_temperatures: dict[str, list[int]]) -> None:
        self.temperatures = defaultdict(list, initial_temperatures)

    def get_temperature(self, day: str) -> int:
        """
        This function will return the temperature for a given day
        it will return an empty list if the day isn't recorded
        """
        return self.temperatures.get(day, [])

    def add_temperature(self, day: str, temperature: int) -> None:
        """
        Add a temperature to a given day
        """
        # This syntaxe is only possible thanks to defaultdict
        # if temperatures[day] does not exist, it will be an empty list
        self.temperatures[day].append(temperature)


def _test_temperature() -> dict[str, list[int]]:
    return {
        "07/01/2024": [0, 1, 2, 5],
        "05/01/2024": [1, 23, 0],
        "08/10/2024": [10, 15, 20, 17, 7],
    }


def test_temperature_management_get_temperature():
    meteo_data = MeteoData(_test_temperature())

    assert meteo_data.get_temperature("07/01/2024") == [0, 1, 2, 5]
    assert meteo_data.get_temperature("05/05/2000") == []


def test_temperature_management_add_temperature():
    meteo_data = MeteoData(_test_temperature())

    meteo_data.add_temperature("07/01/2024", 9)
    meteo_data.add_temperature("09/01/2024", 1)

    assert meteo_data.get_temperature("07/01/2024") == [0, 1, 2, 5, 9]
    assert meteo_data.get_temperature("09/01/2024") == [1]
    random.random()
