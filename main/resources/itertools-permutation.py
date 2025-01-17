# itertools-permutation.py
from itertools import permutations


def all_possible_trip(cities: list[str], trip_duration: int = -1) -> list[tuple]:
    """
    Help the user to plan a trip. You get a list of cities he'd like to visit,
    and a number of cities he can visit.

    When parameter trip_duration is not given (=-1) all cities will be visited
    Return a list of all possible trips
    """
    if trip_duration == -1:
        trip_duration = len(cities)

    return list(permutations(cities, r=trip_duration))


def test_all_possible_trip_basic_trip():
    trips = all_possible_trip(["Bordeaux", "La Rochelle"])

    assert ("Bordeaux", "La Rochelle") in trips
    assert ("La Rochelle", "Bordeaux") in trips

    assert len(trips) == 2


def test_all_possible_trip_longer_trip():
    trips = all_possible_trip(["Paris", "Rome", "Berlin"])

    assert ("Paris", "Rome", "Berlin") in trips
    assert ("Paris", "Berlin", "Rome") in trips
    assert ("Rome", "Paris", "Berlin") in trips
    assert ("Rome", "Berlin", "Paris") in trips
    assert ("Berlin", "Paris", "Rome") in trips
    assert ("Berlin", "Rome", "Paris") in trips

    assert len(trips) == 6


def test_all_possible_trip_time_limited_trip():
    trips = all_possible_trip(["Paris", "Rome", "Berlin"], trip_duration=2)

    assert ("Paris", "Rome") in trips
    assert ("Paris", "Berlin") in trips
    assert ("Rome", "Paris") in trips
    assert ("Rome", "Berlin") in trips
    assert ("Berlin", "Paris") in trips
    assert ("Berlin", "Rome") in trips

    assert len(trips) == 6
