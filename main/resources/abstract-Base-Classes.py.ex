from io import StringIO
from unittest.mock import patch

DEFAULT_WATER_LEVEL = 0
TROPICAL_PLANTS_DRY_LIMIT = 80
PERENNIAL_PLANTS_DRY_LIMIT = 20


class TropicalPlant:
    pass


class PerennialPlant:
    pass


##############################################
# Fill all the previous class definitions    #
# in order to make the test pass.            #
# Feel free to add some code anywhere below  #
##############################################


# The following section should not be modified.
# It contains all the tests used to validate your response
# Test your solution by running '$ pytest exercise.py'
@patch("sys.stdout", new_callable=StringIO)
def test_water_the_plants(fake_out) -> None:
    monstera = TropicalPlant()
    cactus = PerennialPlant()

    plants = [monstera, cactus]

    while any(plant.is_dry() for plant in plants):
        _water_the_plants(plants)

    assert fake_out.getvalue() == (
        "Spraying the tropical plant\n"
        "Putting water under the perennial plant\n"
        "Spraying the tropical plant\n"
    )


def _water_the_plants(plants: list) -> None:
    for plant in plants:
        if plant.is_dry():
            plant.water(water_quantity=50)
