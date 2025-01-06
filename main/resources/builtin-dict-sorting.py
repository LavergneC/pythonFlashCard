def get_animals_sorted_by_older(animals: list[dict]) -> list[dict]:
    """
    This function returns a list of dict of animals, stored from oldest to youghest
    >>> new_list = get_animals_sorted_by_older([
    ...                 {"type": "dog", "age": 8, "name": "Alfred"},
    ...                 {"type": "cat", "age": 3, "name": "Puff"},
    ...                 {"type": "Panda", "age": 13, "name": "Grug"},
    ...              ])
    >>> [animal['name'] for animal in new_list]
    ['Grug', 'Alfred', 'Puff']
    """
    return sorted(animals, key=lambda animal: animal["age"], reverse=True)
