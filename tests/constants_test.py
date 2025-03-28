from main.constants import STATIC_TEXTS


class TEST_GENERATE_EXERCISE:
    RESOURCE_DIR = "tests/test_data/test_generate_exercise_resources/common"
    RESOURCE_DIR_PRE_WRITTEN = (
        "tests/test_data/test_generate_exercise_resources/test_pre_written"
    )
    SOLUTION_PATH = (
        "tests/test_data/test_generate_exercise_resources/common/test_resource_3.py"
    )
    DB_PATH = RESOURCE_DIR + "/test_generate_exercise_db.csv"
    DB_PATH_COPY = RESOURCE_DIR + "/test_generate_exercise_copy_db.csv"
    db_PATH_NEW_DB = RESOURCE_DIR + "/test_generate_exercise_db_new.csv"
    DB_TEST_PRE_WRITTEN = "tests/test_data/test_generate_exercise_resources/test_pre_written/test_pre_written.csv"


class TEST_RESOURCE_STORAGE:
    PATH = "tests/test_data/test_resource_storage"
    RESOURCE_1 = "test_resource_10.py"
    RESOURCE_2 = "test_resource_20.py"
    RESOURCE_3 = "test_resource_30.py"
    DB_PATH = PATH + "/test_resource_storage_db.csv"
    DB_PATH_COPY = PATH + "/test_resource_storage_db_copy.csv"
    db_PATH_NEW_DB = PATH + "/test_resource_storage_db_new.csv"
    RESOURCE_3_FROM = PATH + "/test_dir/" + "test_resource_20.py"
    RESOURCE_3_TO = PATH + "/" + "test_resource_30.py"


class TEST_SOLUTION_TO_EXERCISE_RESOURCES:
    PATH = "tests/test_data/test_solution_to_exercise"
    VERY_SIMPLE = PATH + "/" + "very_simple_exercise.py"
    NO_IMPORT = PATH + "/" + "no_import_left.py"
    CLASS = PATH + "/" + "class_resource.py"
    TEST_NO_IMPORT_RESOURCE_DEF = "def dishes_from_ingredients(ingredients: list[str], meal_size: int) -> list[tuple]:"
    WITH_PATCH = PATH + "/" + "simple_with_patch_test.py"


class TEST_SOLUTION_TO_EXERCISE_SIMPLE:
    MAIN_FUNCTION_DEFINITION = "def str_to_sentences(long_str: str) -> list[str]:"
    MAIN_FUNCTION_DOCSTRING = (
        '    """\n    split the given string on punctuation symbols\n    """\n'
    )
    TESTS = """
def test_str_to_sentences():
    assert str_to_sentences("Hello word. How are you?") == [
        "Hello word",
        " How are you",
    ]

    assert str_to_sentences("Hello word\") == ["Hello word"]
    assert str_to_sentences("Hello word: this will go down! So do This & this too") == [
        "Hello word",
        " this will go down",
        " So do This ",
        " this too",
    ]"""


class TEST_SOLUTION_TO_EXERCISE_CLASS:
    TESTS = """
def _test_temperature() -> dict[str, list[int]]:
    return {
        "07/01/2024": [0, 1, 2, 5],
        "05/01/2024": [1, 23, 0],
        "08/10/2024": [10, 15, 20, 17, 7],
    }


def test_temperature_management_get_temperature():
    meteo_data = MeteoData(_test_temperature())

    assert meteo_data.get_temperature("07/01/2024") == [0, 1, 2, 5]
    assert meteo_data.get_temperature("05/05/2000") == []


def test_temperature_management_add_temperature():
    meteo_data = MeteoData(_test_temperature())

    meteo_data.add_temperature("07/01/2024", 9)
    meteo_data.add_temperature("09/01/2024", 1)

    assert meteo_data.get_temperature("07/01/2024") == [0, 1, 2, 5, 9]
    assert meteo_data.get_temperature("09/01/2024") == [1]
    random.random()
"""

    INIT_FUNCTION = "def __init__(self, initial_temperatures: dict[str, list[int]]) -> None:\n        pass"

    FUNCTION_1_DEFINITION = "def get_temperature(self, day: str) -> int:"
    FUNCTION_2_DEFINITION = (
        "def add_temperature(self, day: str, temperature: int) -> None:"
    )

    FUNCTION_1_DOCSTRING = """This function will return the temperature for a given day
        it will return an empty list if the day isn't recorded"""
    FUNCTION_2_DOCSTRING = "Add a temperature to a given day"

    STATIC_TEXT_WITH_PREVIOUS_CONTENT = f'{FUNCTION_2_DOCSTRING}\n        """\n        pass\n\n{STATIC_TEXTS.CLASS_USER_CODE}'
