import random
import shutil
from os import listdir
from unittest.mock import MagicMock, patch

from main.generate_exercise import PythonFlashCards
from main.ressource_picker import RessourcePicker
from tests.constants_test import (
    TEST_GET_RANDOM_EXERCISE,
    TEST_RESSOUCES,
    TEST_RESSOURCE_STORAGE,
)
from tests.test_ressource_picker import _get_default_ressources


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


def test_never_twice_the_same_ressoure_per_day():
    shutil.copyfile(TEST_RESSOURCE_STORAGE.PATH, TEST_RESSOURCE_STORAGE.PATH_COPY)
    ressource_picker = RessourcePicker(TEST_RESSOURCE_STORAGE.PATH_COPY)

    brute_calls = []
    while len(brute_calls) < 10:
        brute_calls.append(ressource_picker.pick())
        ressource_picker.set_result(success=False)

    assert brute_calls.count("Ressource 1") == 1
    assert brute_calls.count("Ressource 2") == 1

    # Ré-init : The app is relaunched but it's the same day
    ressource_picker = RessourcePicker(TEST_RESSOURCE_STORAGE.PATH_COPY)

    brute_calls = []
    while len(brute_calls) < 10:
        brute_calls.append(ressource_picker.pick())
        ressource_picker.set_result(success=False)

    assert "Ressource 1" not in brute_calls
    assert "Ressource 2" not in brute_calls
