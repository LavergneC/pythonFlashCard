import os
import shutil
from os import listdir

from main.python_flash_cards import PythonFlashCards
from tests.constants_test import (
    TEST_GENERATE_EXERCISE,
    TEST_RESOURCE_STORAGE,
)


def test_get_exercise():
    # The user launch the application #TODO more real
    if os.path.exists(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB):
        os.remove(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB)

    pfc = PythonFlashCards(
        resource_csv_path=TEST_RESOURCE_STORAGE.db_PATH_NEW_DB,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR,
    )
    pfc.get_exercise()

    # A new file named "solution.py" appears in the working dir
    assert "solution.py" in listdir("./")

    # It contains a full exercise solution
    with (
        open("solution.py") as solution_file,
        open(TEST_GENERATE_EXERCISE.SOLUTION_PATH) as source_file,
    ):
        assert solution_file.read() == source_file.read()

    # A new file named "exercise.py" appeared in the working dir too
    assert "exercise.py" in listdir("./")


def test_never_twice_the_same_resource_per_day():
    shutil.copyfile(TEST_RESOURCE_STORAGE.DB_PATH, TEST_RESOURCE_STORAGE.DB_PATH_COPY)
    pfc = PythonFlashCards(
        resource_csv_path=TEST_RESOURCE_STORAGE.DB_PATH_COPY,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR,
    )

    calls_exercises_names = []

    # get_exercise will returns False once all exercise are picked
    while pfc.get_exercise() != PythonFlashCards.ExerciseType.NONE:
        with open("solution.py") as solution_file:
            calls_exercises_names.append(solution_file.read().split("\n")[0])
        pfc.set_exercise_result(True)

    assert len(calls_exercises_names) == 3
    assert calls_exercises_names.count("# test_resource_1.py") == 1

    # Ré-init : The app is relaunched but it's the same day
    pfc = PythonFlashCards(
        resource_csv_path=TEST_RESOURCE_STORAGE.DB_PATH_COPY,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR,
    )

    calls_exercises_names = []
    while pfc.get_exercise() != PythonFlashCards.ExerciseType.NONE:
        with open("solution.py") as solution_file:
            calls_exercises_names.append(solution_file.read().split("\n")[0])
        pfc.set_exercise_result(True)

    assert len(calls_exercises_names) == 0


def test_get_exercise_from_pre_written_file() -> None:
    pfc = PythonFlashCards(
        resource_csv_path=TEST_GENERATE_EXERCISE.DB_TEST_PRE_WRITTEN,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR_PRE_WRITTEN,
    )

    pfc.get_exercise()

    with open("exercise.py") as exercise_file:
        assert "# solution_with_pre_written_exercise.py.ex" in exercise_file.read()

    with open("solution.py") as solution_file:
        content = solution_file.read()
        assert "# solution_with_pre_written_exercise.py" in content
        assert "# solution_with_pre_written_exercise.py.ex" not in content


def test_get_exercise_with_quiz():
    if os.path.exists("exercise.py"):
        os.remove("exercise.py")
    if os.path.exists("solution.py"):
        os.remove("solution.py")

    pfc = PythonFlashCards(
        resource_csv_path=TEST_GENERATE_EXERCISE.DB_TEST_QUIZ,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR_QUIZ,
    )

    assert pfc.get_exercise() == PythonFlashCards.ExerciseType.QUIZ
    assert pfc.next_quiz.get_question() == "This is the first question.\n"

    assert os.path.exists("exercise.py") is False
    assert os.path.exists("solution.py") is False


"""
@patch("sys.stdout", new_callable=StringIO)
def test_get_exercise_quiz(fake_out, monkeypatch) -> None:
    if os.path.exists("exercise.py"):
        os.remove("exercise.py")
    if os.path.exists("solution.py"):
        os.remove("solution.py")

    monkeypatch.setattr("builtins.input", lambda _: "Paris")

    pfc = PythonFlashCards(
        resource_csv_path=TEST_GENERATE_EXERCISE.DB_TEST_QUIZ,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR_QUIZ,
    )

    assert pfc.get_exercise() is True

    assert os.path.exists("exercise.py") is False
    assert os.path.exists("solution.py") is False

    assert "This is the first question.\n" in fake_out.getvalue()
    assert "Wrong, the correct answer was 'Blue'" in fake_out.getvalue()
"""
