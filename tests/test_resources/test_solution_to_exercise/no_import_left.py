import itertools as it


def dishes_from_ingredients(ingredients: list[str], meal_size: int) -> list[tuple]:
    """
    Given a list of unique ingredients, return a list of all possible dishes using meal_size
    ingredients.
    A dish is a tuple of ingredients
    """
    return list(it.combinations(ingredients, r=meal_size))


def test_dishes_from_ingredients_basic():
    dishes = dishes_from_ingredients(["beans", "pork", "salad"], meal_size=2)

    assert ("beans", "pork") in dishes
    assert ("beans", "salad") in dishes
    assert ("pork", "salad") in dishes

    assert len(dishes) == 3
