from main.constants import KEEP_LINE_TAG, STATIC_TEXTS
from main.generate_exercise_components.solution_to_exercise import SolutionToExercice
from tests.constants_test import (
    TEST_SOLUTION_TO_EXERCISE_CLASS,
    TEST_SOLUTION_TO_EXERCISE_RESSOUCES,
    TEST_SOLUTION_TO_EXERCISE_SIMPLE,
)


def test_very_simple_exercise():
    ste = SolutionToExercice()

    exercise_content = ""
    with open(TEST_SOLUTION_TO_EXERCISE_RESSOUCES.VERY_SIMPLE) as solution_file:
        exercise_content = ste.solution_to_exercice(solution_file.read())

    # "exercise.py" is a modified version of 'solution.py'
    #   - Only some import are present
    assert "import pathlib\n" in exercise_content
    assert "import random" not in exercise_content
    assert "from os import listdir\n" in exercise_content

    # All tags have been removed from the file
    assert KEEP_LINE_TAG not in exercise_content

    #   - main function definition line was kept
    assert TEST_SOLUTION_TO_EXERCISE_SIMPLE.MAIN_FUNCTION_DEFINITION in exercise_content
    #   - main function doctring was kept
    assert TEST_SOLUTION_TO_EXERCISE_SIMPLE.MAIN_FUNCTION_DOCTSTRING in exercise_content
    #   - tests were kept
    assert TEST_SOLUTION_TO_EXERCISE_SIMPLE.TESTS in exercise_content
    #   - Some context texts were added at several places
    assert ('"""\n' + STATIC_TEXTS.USER_CODE) in exercise_content
    assert (STATIC_TEXTS.TESTS_PART + "def test_") in exercise_content


def test_content_with_no_import():
    ste = SolutionToExercice()

    exercise_content = ""
    with open(TEST_SOLUTION_TO_EXERCISE_RESSOUCES.NO_IMPORT) as solution_file:
        exercise_content = ste.solution_to_exercice(solution_file.read())

        first_line = exercise_content.split("\n")[0]
        assert (
            first_line
            == TEST_SOLUTION_TO_EXERCISE_RESSOUCES.TEST_NO_IMPORT_RESSOURCE_DEF
        )


def test_content_class_exercice():
    ste = SolutionToExercice()

    file_content = ""
    with open(TEST_SOLUTION_TO_EXERCISE_RESSOUCES.CLASS) as solution_file:
        file_content = ste.solution_to_exercice(solution_file.read())

    # Some import are present
    assert "import random" in file_content
    assert "from collections import defaultdict" not in file_content

    # Class definition was kept
    assert "class MeteoData" in file_content

    # all public methods definitions
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.INIT_FUNCTION in file_content
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.FUNCTION_1 in file_content
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.FUNCTION_2 in file_content

    # Function bodies aren't keept
    assert "defaultdict" not in file_content
    assert "append" not in file_content
    assert "return" not in file_content

    # Tests are kept
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.TESTS in file_content

    # Texts are correctly added
    assert (
        f"{TEST_SOLUTION_TO_EXERCISE_CLASS.FUNCTION_2}\n{STATIC_TEXTS.CLASS_USER_CODE}"
        in file_content
    )
    assert (STATIC_TEXTS.TESTS_PART + "def test_") in file_content
