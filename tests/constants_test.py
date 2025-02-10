class TEST_RESSOUCES:
    PATH = "tests/test_resources/test_solution_to_exercise"
    VERY_SIMPLE = PATH + "/" + "very_simple_exercise.py"
    NO_IMPORT = PATH + "/" + "no_import_left.py"
    CLASS = PATH + "/" + "class_ressource.py"


class TEST_GET_RANDOM_EXERCISE:
    PATH = "tests/test_resources/test_random"
    RESSOURCE_1 = PATH + "/" + "ressource1.py"
    RESSOURCE_2 = PATH + "/" + "ressource2.py"


class TEST_SIMPLE:
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


TEST_NO_IMPORT_RESSOURCE_DEF = "def dishes_from_ingredients(ingredients: list[str], meal_size: int) -> list[tuple]:"


class TEST_CLASS_RESSOURCE:
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


class TEST_RESSOURCE_STORAGE:
    PATH = "tests/test_resources/test_db.csv"
    PATH_COPY = "tests/test_resources/test_db_copy.csv"
