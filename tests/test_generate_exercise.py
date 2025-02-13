import os
import shutil
from os import listdir

from main.generate_exercise import PythonFlashCards
from tests.constants_test import (
    TEST_GENERATE_EXERCISE,
    TEST_RESSOURCE_STORAGE_CSV,
)


def test_generate_exercise():
    # The user launch the application #TODO more real
    if os.path.exists(TEST_RESSOURCE_STORAGE_CSV.PATH_NEW_DB):
        os.remove(TEST_RESSOURCE_STORAGE_CSV.PATH_NEW_DB)

    pfc = PythonFlashCards(
        ressource_csv_path=TEST_RESSOURCE_STORAGE_CSV.PATH_NEW_DB,
        ressource_directory_path=TEST_GENERATE_EXERCISE.RESSOURCE_DIR,
    )
    pfc.generate_exercise()

    # A new file named "solution.py" apears in the working dir
    assert "solution.py" in listdir("./")

    # It contains a full exercise solution
    with (
        open("solution.py") as solution_file,
        open(TEST_GENERATE_EXERCISE.SOLUTION_PATH) as source_file,
    ):
        assert solution_file.read() == source_file.read()

    # A new file named "exercise.py" apeared in the working dir too
    assert "exercise.py" in listdir("./")


def test_never_twice_the_same_ressoure_per_day():
    shutil.copyfile(
        TEST_RESSOURCE_STORAGE_CSV.PATH, TEST_RESSOURCE_STORAGE_CSV.PATH_COPY
    )
    pfc = PythonFlashCards(
        ressource_csv_path=TEST_RESSOURCE_STORAGE_CSV.PATH_COPY,
        ressource_directory_path=TEST_GENERATE_EXERCISE.RESSOURCE_DIR,
    )

    calls_exercises_names = []
    while len(calls_exercises_names) < 10:
        pfc.generate_exercise()
        with open("solution.py") as solution_file:
            calls_exercises_names.append(solution_file.read().split("\n")[0])
        pfc.set_exercise_result(True)

    assert calls_exercises_names.count("# test_ressource_1.py") == 1

    # Ré-init : The app is relaunched but it's the same day
    pfc = PythonFlashCards(
        ressource_csv_path=TEST_RESSOURCE_STORAGE_CSV.PATH_COPY,
        ressource_directory_path=TEST_GENERATE_EXERCISE.RESSOURCE_DIR,
    )

    calls_exercises_names = []
    while len(calls_exercises_names) < 10:
        pfc.generate_exercise()
        with open("solution.py") as solution_file:
            calls_exercises_names.append(solution_file.read().split("\n")[0])
        pfc.set_exercise_result(True)

    assert "# test_ressource_1.py" not in calls_exercises_names
