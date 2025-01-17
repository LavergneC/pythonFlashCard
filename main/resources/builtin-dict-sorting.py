def get_animals_sorted_by_older(animals: list[dict]) -> list[dict]:
    """
    This functions gets a list of dict of animals.
    it returns a list of dict of animals, stored from oldest to youngest
    """
    return sorted(animals, key=lambda animal: animal["age"], reverse=True)


def test_get_animals_sorted_by_older():
    ordered_list = get_animals_sorted_by_older(
        [
            {"type": "dog", "age": 8, "name": "Alfred"},
            {"type": "cat", "age": 3, "name": "Puff"},
            {"type": "Panda", "age": 13, "name": "Grug"},
        ]
    )
    assert ordered_list == [
        {"type": "Panda", "age": 13, "name": "Grug"},
        {"type": "dog", "age": 8, "name": "Alfred"},
        {"type": "cat", "age": 3, "name": "Puff"},
    ]


def test_get_animals_sorted_by_older_does_not_edit_parameter():
    my_zoo = [
        {"type": "dog", "age": 8, "name": "Alfred"},
        {"type": "cat", "age": 3, "name": "Puff"},
        {"type": "Panda", "age": 13, "name": "Grug"},
    ]
    get_animals_sorted_by_older(my_zoo)

    assert my_zoo == [
        {"type": "dog", "age": 8, "name": "Alfred"},
        {"type": "cat", "age": 3, "name": "Puff"},
        {"type": "Panda", "age": 13, "name": "Grug"},
    ]
