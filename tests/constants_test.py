class TEST_GENERATE_EXERCISE:
    RESSOURCE_DIR = "tests/test_data/test_generate_exercise_ressources"
    SOLUTION_PATH = (
        "tests/test_data/test_generate_exercise_ressources/test_ressource_3.py"
    )
    DB_PATH = RESSOURCE_DIR + "/test_generate_exercise_db.csv"
    DB_PATH_COPY = RESSOURCE_DIR + "/test_generate_exercise_copy_db.csv"
    db_PATH_NEW_DB = RESSOURCE_DIR + "/test_generate_exercise_db_new.csv"


class TEST_RESSOURCE_STORAGE:
    PATH = "tests/test_data/test_ressource_storage"
    RESSOURCE_1 = "test_ressource_10.py"
    RESSOURCE_2 = "test_ressource_20.py"
    DB_PATH = PATH + "/test_ressource_storage_db.csv"
    DB_PATH_COPY = PATH + "/test_ressource_storage_db_copy.csv"
    db_PATH_NEW_DB = PATH + "/test_db_new.csv"


class TEST_SOLUTION_TO_EXERCISE_RESSOUCES:
    PATH = "tests/test_data/test_solution_to_exercise"
    VERY_SIMPLE = PATH + "/" + "very_simple_exercise.py"
    NO_IMPORT = PATH + "/" + "no_import_left.py"
    CLASS = PATH + "/" + "class_ressource.py"
    TEST_NO_IMPORT_RESSOURCE_DEF = "def dishes_from_ingredients(ingredients: list[str], meal_size: int) -> list[tuple]:"


class TEST_SOLUTION_TO_EXERCISE_SIMPLE:
    MAIN_FUNCTION_DEFINITION = "def str_to_sentences(long_str: str) -> list[str]:"
    MAIN_FUNCTION_DOCTSTRING = (
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
def test_temperature_management_get_temperature():
    temperatures = {
        "07/01/2024": [0, 1, 2, 5],
        "05/01/2024": [1, 23, 0],
        "08/10/2024": [10, 15, 20, 17, 7],
    }

    meteo_data = MeteoData(temperatures)

    assert meteo_data.get_temperature("07/01/2024") == [0, 1, 2, 5]
    assert meteo_data.get_temperature("05/05/2000") == []


def test_temperature_management_add_temperature():
    temperatures = {
        "07/01/2024": [0, 1, 2, 5],
        "05/01/2024": [1, 23, 0],
        "08/10/2024": [10, 15, 20, 17, 7],
    }
    meteo_data = MeteoData(temperatures)

    meteo_data.add_temperature("07/01/2024", 9)
    meteo_data.add_temperature("09/01/2024", 1)

    assert meteo_data.get_temperature("07/01/2024") == [0, 1, 2, 5, 9]
    assert meteo_data.get_temperature("09/01/2024") == [1]
    random.random()"""

    INIT_FUNCTION = (
        "def __init__(self, initial_temperatures: dict[str, list[int]]) -> None:"
    )

    FUNCTION_1 = "def get_temperature(self, day: str) -> int:"
    FUNCTION_2 = "def add_temperature(self, day: str, temperature: int) -> None:"
