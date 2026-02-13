# batched.py


from itertools import batched


def get_roller_coaster_rows(clients: list[str], car_size: int) -> list[tuple[str, ...]]:
    """
    Given a list of client that entered the roller coaster, return a list of car with clients name in it.
    Cars are filled in order if the client list.
    """
    return list(batched(clients, n=car_size))


def test_get_roller_coaster_rows() -> None:
    clients = ["Pierre", "Paul", "Jacques", "Alice", "Bob", "David"]

    assert get_roller_coaster_rows(clients=clients, car_size=2) == [
        ("Pierre", "Paul"),
        ("Jacques", "Alice"),
        ("Bob", "David"),
    ]

    assert get_roller_coaster_rows(clients=clients, car_size=3) == [
        ("Pierre", "Paul", "Jacques"),
        ("Alice", "Bob", "David"),
    ]

    assert get_roller_coaster_rows(clients=clients, car_size=4) == [
        ("Pierre", "Paul", "Jacques", "Alice"),
        ("Bob", "David"),
    ]
