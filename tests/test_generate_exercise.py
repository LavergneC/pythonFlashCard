import random
from os import listdir
from os.path import join
from unittest.mock import MagicMock, patch

from main.constants import KEEP_LINE_TAG, TEXT_TESTS_PART, TEXT_USER_CODE
from main.generate_exercise import PythonFlashCards
from tests.constants_test import (
    TEST_GET_RANDOM_EXERCISE,
    TEST_MAIN_FUNCTION_DEFINITION,
    TEST_MAIN_FUNCTION_DOCTSTRING,
    TEST_NO_IMPORT_RESSOURCE_DEF,
    TEST_RESSOUCE,
    TEST_RESSOURCES_TEST,
)


@patch(
    "main.generate_exercise.PythonFlashCards._get_random_exercise_file_name",
    return_value=TEST_RESSOUCE.VERY_SIMPLE,
)
def test_generate_very_simple_exercise(mock_method):
    # The user launch the application #TODO more real
    pfc = PythonFlashCards()
    pfc.generate_exercise()

    # A new file named "solution.py" apears in the working dir
    assert "solution.py" in listdir("./")

    # It contains a full exercise solution
    with (
        open("solution.py") as solution_file,
        open(TEST_RESSOUCE.VERY_SIMPLE) as source_file,
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
    assert ('"""\n' + TEXT_USER_CODE) in exercise_content
    assert (TEXT_TESTS_PART + "def test_") in exercise_content


def test_get_random_exercise_file_name():
    random.choice = MagicMock("choise")

    pfc = PythonFlashCards()
    pfc._get_random_exercise_file_name(TEST_GET_RANDOM_EXERCISE.PATH)

    random.choice.assert_called_once_with(
        [TEST_GET_RANDOM_EXERCISE.RESSOURCE_2, TEST_GET_RANDOM_EXERCISE.RESSOURCE_1]
    )


@patch(
    "main.generate_exercise.PythonFlashCards._get_random_exercise_file_name",
    return_value=TEST_RESSOUCE.NO_IMPORT,
)
def test_ressource_with_no_import_kept(mock_method):
    pfc = PythonFlashCards()
    pfc.generate_exercise()

    with open("exercise.py") as exercise_file:
        first_line = exercise_file.read().split("\n")[0]
        assert first_line == TEST_NO_IMPORT_RESSOURCE_DEF
