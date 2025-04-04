from main.constants import KEEP_LINE_TAG, STATIC_TEXTS
from main.exercise_production.solution_to_exercise import SolutionToExercise
from tests.constants_test import (
    TEST_SOLUTION_TO_EXERCISE_CLASS,
    TEST_SOLUTION_TO_EXERCISE_RESOURCES,
    TEST_SOLUTION_TO_EXERCISE_SIMPLE,
)


def test_very_simple_exercise():
    ste = SolutionToExercise()

    exercise_content = ""
    with open(TEST_SOLUTION_TO_EXERCISE_RESOURCES.VERY_SIMPLE) as solution_file:
        exercise_content = ste.solution_to_exercise(solution_file.read())

    # "exercise.py" is a modified version of 'solution.py'
    #   - Only some import are present
    assert "import pathlib\n" in exercise_content
    assert "import random" not in exercise_content
    assert "from os import listdir\n" in exercise_content

    # All tags have been removed from the file
    assert KEEP_LINE_TAG not in exercise_content

    #   - main function definition line was kept
    assert TEST_SOLUTION_TO_EXERCISE_SIMPLE.MAIN_FUNCTION_DEFINITION in exercise_content
    #   - main function docstring was kept
    assert TEST_SOLUTION_TO_EXERCISE_SIMPLE.MAIN_FUNCTION_DOCSTRING in exercise_content
    #   - tests were kept
    assert TEST_SOLUTION_TO_EXERCISE_SIMPLE.TESTS in exercise_content
    #   - Some context texts were added at several places
    assert ('"""\n' + STATIC_TEXTS.USER_CODE) in exercise_content
    assert (STATIC_TEXTS.TESTS_PART + "def test_") in exercise_content


def test_content_with_no_import():
    ste = SolutionToExercise()

    exercise_content = ""
    with open(TEST_SOLUTION_TO_EXERCISE_RESOURCES.NO_IMPORT) as solution_file:
        exercise_content = ste.solution_to_exercise(solution_file.read())

        first_line = exercise_content.split("\n")[0]
        assert (
            first_line
            == TEST_SOLUTION_TO_EXERCISE_RESOURCES.TEST_NO_IMPORT_RESOURCE_DEF
        )


def test_content_class_exercise():
    ste = SolutionToExercise()

    file_content = ""
    with open(TEST_SOLUTION_TO_EXERCISE_RESOURCES.CLASS) as solution_file:
        file_content = ste.solution_to_exercise(solution_file.read())

    # correct import is kept
    assert "import random" in file_content
    assert "from collections import defaultdict" not in file_content
    assert "dataclass" not in file_content

    # Class definition was kept
    assert "class MeteoData" in file_content

    # all public methods definitions
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.INIT_FUNCTION in file_content
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.FUNCTION_1_DEFINITION in file_content
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.FUNCTION_2_DEFINITION in file_content

    # Function bodies aren't kept
    assert "defaultdict" not in file_content
    assert "append" not in file_content
    assert "self.temperatures.get(day, [])" not in file_content

    # Docstring are kept
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.FUNCTION_1_DOCSTRING in file_content
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.FUNCTION_2_DOCSTRING in file_content

    # Tests are kept
    assert TEST_SOLUTION_TO_EXERCISE_CLASS.TESTS in file_content

    # Texts are correctly added
    assert (
        TEST_SOLUTION_TO_EXERCISE_CLASS.STATIC_TEXT_WITH_PREVIOUS_CONTENT
        in file_content
    )

    assert (STATIC_TEXTS.TESTS_PART + "def _test") in file_content


def test_get_docstring() -> None:
    ste = SolutionToExercise()

    no_doc_string_content = [
        "is simply dummy text of the printing and",
        "typesetting industry. Lorem Ipsum has been the",
    ]
    assert ste._get_docstring(no_doc_string_content) == ""

    doc_string_in_content = [
        "",
        "  def get_temperature(self, day: str) -> int:",
        '      """   ',
        " the doc string line 1 ",
        " the doc string line 2 ",
        '   """ ',
        "It was popularized in the 1960s with the release",
    ]

    assert (
        ste._get_docstring(doc_string_in_content)
        == '      """   \n the doc string line 1 \n the doc string line 2 \n   """ '
    )


def test_patch_at_start_of_test() -> None:
    ste = SolutionToExercise()

    exercise_content = ""
    with open(TEST_SOLUTION_TO_EXERCISE_RESOURCES.WITH_PATCH) as solution_file:
        exercise_content = ste.solution_to_exercise(solution_file.read())

    assert "@patch" in exercise_content
