# itertools-combinaison+set.py
import itertools as it


def flower_field_to_bouquet(flowers: list[str], bouquet_size) -> list[tuple]:
    """
    Given a list of flowers, return a list of all bouquet that you can make.
    There might be identical flowers both in the flower list or in a bouquet
    NB: A bouquet is a tuple of str, the order does NOT matter
    """
    return list(set(it.combinations(flowers, r=bouquet_size)))


def test_flower_field_to_bouquet_basic():
    bouquets = flower_field_to_bouquet(["daisie", "poppie", "lupine"], bouquet_size=2)

    assert ("daisie", "poppie") in bouquets
    assert ("daisie", "lupine") in bouquets
    assert ("poppie", "lupine") in bouquets

    assert len(bouquets) == 3


def test_flower_field_to_bouquet_duplicate():
    bouquets = flower_field_to_bouquet(["daisie", "daisie", "lupine"], bouquet_size=2)

    assert ("daisie", "daisie") in bouquets
    assert ("daisie", "lupine") in bouquets

    assert len(bouquets) == 2
