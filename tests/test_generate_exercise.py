import os
import shutil
from os import listdir

from main.generate_exercise import PythonFlashCards
from tests.constants_test import (
    TEST_GENERATE_EXERCISE,
    TEST_RESOURCE_STORAGE,
)


def test_generate_exercise():
    # The user launch the application #TODO more real
    if os.path.exists(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB):
        os.remove(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB)

    pfc = PythonFlashCards(
        resource_csv_path=TEST_RESOURCE_STORAGE.db_PATH_NEW_DB,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR,
    )
    pfc.generate_exercise()

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

    # generate_exercise will returns False once all exercise are picked
    while pfc.generate_exercise():
        with open("solution.py") as solution_file:
            calls_exercises_names.append(solution_file.read().split("\n")[0])
        pfc.set_exercise_result(True)

    assert len(calls_exercises_names) == 3
    assert calls_exercises_names.count("# test_ressource_1.py") == 1

    # Ré-init : The app is relaunched but it's the same day
    pfc = PythonFlashCards(
        resource_csv_path=TEST_RESOURCE_STORAGE.DB_PATH_COPY,
        resource_directory_path=TEST_GENERATE_EXERCISE.RESOURCE_DIR,
    )

    calls_exercises_names = []
    while pfc.generate_exercise():
        with open("solution.py") as solution_file:
            calls_exercises_names.append(solution_file.read().split("\n")[0])
        pfc.set_exercise_result(True)

    assert len(calls_exercises_names) == 0
