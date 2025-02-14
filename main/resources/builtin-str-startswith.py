# builtin-str-startswith.py


def village_is_a_saint(village_name: str) -> bool:
    """
    Given a village name, this function returs if it's start with "Saint"
    """
    return village_name.startswith("Saint")


def test_village_is_a_saint() -> None:
    assert village_is_a_saint("Saint-Christophe")
    assert village_is_a_saint("Sainte-Soulle")
    assert not village_is_a_saint("Bordeaux")
