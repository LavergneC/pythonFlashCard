def get_tower_damage():
    """
    get_tower_damage return the damage dealt by a tower, the first damage is 10,
    then for each call, damage are multiplied by 2.

    yield damages dealt
    """
    ##################
    # Your code here #
    ##################


# The following section should not be modified.
# It contains all the tests used to validate your response
# Test your solution by running '$ pytest exercise.py'
def test_get_tower_damage() -> None:
    player_1_life = 100
    player_2_life = 100

    tower_damage_generator = get_tower_damage()

    # player_1 enter tower range and get hits 3 times, tower inflict 10, 20, 40 damages
    player_1_life -= next(tower_damage_generator)
    assert player_1_life == 90

    player_1_life -= next(tower_damage_generator)
    assert player_1_life == 70

    player_1_life -= next(tower_damage_generator)
    assert player_1_life == 30

    # player_1 enter tower range and get hits 1 times, 80 damages
    player_2_life -= next(tower_damage_generator)
    assert player_2_life == 20
