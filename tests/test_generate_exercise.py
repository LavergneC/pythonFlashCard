import pathlib
import random
from os import listdir
from os.path import join
from unittest.mock import MagicMock, patch

from main.constants import KEEP_LINE_TAG, TEXT_TESTS_PART
from main.generate_exercise import PythonFlashCards
from tests.constants_test import (
    TEST_MAIN_FUNCTION_DEFINITION,
    TEST_MAIN_FUNCTION_DOCTSTRING,
    TEST_RESSOURCES_PATH,
    TEST_RESSOURCES_TEST,
)


@patch(
    "main.generate_exercise.PythonFlashCards._get_random_exercise_file_name",
    return_value="tests/test_resources/ressource_test1.py",
)
def test_generate_very_simple_exercise(mock_method):
    if "solution.py" in listdir("./"):
        pathlib.Path.unlink("solution.py")  # Remove file

    if "exercise.py" in listdir("./"):
        pathlib.Path.unlink("exercise.py")  # Remove file

    # The user launch the application #TODO more real
    pfc = PythonFlashCards()
    pfc.generate_exercise()

    # A new file named "solution.py" apears in the working dir
    assert "solution.py" in listdir("./")

    # It contains a full exercise solution
    with (
        open("solution.py") as solution_file,
        open("tests/test_resources/ressource_test1.py") as source_file,
    ):
        assert solution_file.read() == source_file.read()

    # A new file named "exercise.py" apeared in the working dir too
    assert "exercise.py" in listdir("./")

    exercise_content = ""
    with open("exercise.py") as exercise_file:
        exercise_content = exercise_file.read()

    # "exercise.py" is a modified version of 'solution.py'
    #   - Only some import are present
    assert "import pathlib\n" in exercise_content
    assert "import random" not in exercise_content
    assert "from os import listdir\n" in exercise_content

    # All tags have been removed from the file
    assert KEEP_LINE_TAG not in exercise_content

    #   - main function definition line was kept
    assert TEST_MAIN_FUNCTION_DEFINITION in exercise_content
    #   - main function doctring was kept
    assert TEST_MAIN_FUNCTION_DOCTSTRING in exercise_content
    #   - tests were kept
    assert TEST_RESSOURCES_TEST in exercise_content
    #   - Some context texts were added at several places
    assert TEXT_TESTS_PART in exercise_content
    assert TEXT_TESTS_PART in exercise_content


def test_get_random_exercise_file_name():
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


# TODO: test if exercise.py and/or solution.py already exists
