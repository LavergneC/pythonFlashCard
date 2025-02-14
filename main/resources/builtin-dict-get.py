# builtin-dict-get.py
# From https://realpython.com/lessons/dictionary-default-values/


def read_dict(fools_count: dict[str, int], player_name: str) -> int:
    """
    fools_count is a dict of player with at least one fool. Given a player name
    return it's number of fools
    """
    return fools_count.get(player_name, 0)


def test_read_dict() -> None:
    fools_count = {"Jean": 1, "Jaques": 10}
    assert read_dict(fools_count=fools_count, player_name="Jean") == 1
    assert read_dict(fools_count=fools_count, player_name="Jaques") == 10
    assert read_dict(fools_count=fools_count, player_name="Clement") == 0
