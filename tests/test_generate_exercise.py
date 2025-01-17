import random
from os import listdir
from unittest.mock import MagicMock, patch

from main.generate_exercise import PythonFlashCards
from tests.constants_test import (
    TEST_GET_RANDOM_EXERCISE,
    TEST_RESSOUCES,
)


@patch(
    "main.generate_exercise.PythonFlashCards._get_random_exercise_file_name",
    return_value=TEST_RESSOUCES.VERY_SIMPLE,
)
def test_generate_exercise(_mock_method):
    # The user launch the application #TODO more real
    pfc = PythonFlashCards()
    pfc.generate_exercise()

    # A new file named "solution.py" apears in the working dir
    assert "solution.py" in listdir("./")

    # It contains a full exercise solution
    with (
        open("solution.py") as solution_file,
        open(TEST_RESSOUCES.VERY_SIMPLE) as source_file,
    ):
        assert solution_file.read() == source_file.read()

    # A new file named "exercise.py" apeared in the working dir too
    assert "exercise.py" in listdir("./")


def test_get_random_exercise_file_name():
    random.choice = MagicMock("choise")

    pfc = PythonFlashCards()
    pfc._get_random_exercise_file_name(TEST_GET_RANDOM_EXERCISE.PATH)

    random.choice.assert_called_once_with(
        [TEST_GET_RANDOM_EXERCISE.RESSOURCE_2, TEST_GET_RANDOM_EXERCISE.RESSOURCE_1]
    )
