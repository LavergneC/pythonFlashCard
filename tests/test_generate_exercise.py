import random
from os import listdir
from os.path import join
from unittest.mock import MagicMock, patch

from main.generate_exercise import PythonFlashCards
from tests.constants_test import TEST_RESSOURCES_PATH


@patch(
    "main.generate_exercise.PythonFlashCards._get_random_exercise_file_name",
    return_value="tests/test_resources/ressource_test1.py",
)
def test_generate_exercise(mock_method):
    # if "solution.py" in listdir("./pythonFlashCards"): remove solution
    # pareil pour exercise
    # faudra aussi test le cas où il sont déjà présent

    # The user launch the application #TODO more real
    pfc = PythonFlashCards()
    pfc.generate_exercise()

    # A new file named "solution.py" apears in the working dir
    assert "solution.py" in listdir("./")

    # It contains a full exercise solution
    # TODO

    # A new file named "exercise.py" apeared  in the working dir too
    assert "exercise.py" in listdir("./")

    # It contains a modified version of 'solution.py'
    #   - Only some import are present
    #   - main function definition line was kept
    #   - tests were kept
    #   - Some context text has been added at several places


def test_get_exercise_file_name():
    random.choice = MagicMock("choise")

    pfc = PythonFlashCards()
    pfc._get_random_exercise_file_name(TEST_RESSOURCES_PATH)

    random.choice.assert_called_once_with(
        [
            join(TEST_RESSOURCES_PATH, "ressource_test3.py"),
            join(TEST_RESSOURCES_PATH, "ressource_test2.py"),
            join(TEST_RESSOURCES_PATH, "ressource_test1.py"),
        ]
    )
