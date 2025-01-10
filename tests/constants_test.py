class TEST_RESSOUCE:
    PATH = "tests/test_resources"
    VERY_SIMPLE = PATH + "/" + "very_simple_exercise.py"
    NO_IMPORT = PATH + "/" + "no_import_left.py"
    CLASS = PATH + "/" + "class_ressoucerce.py"


class TEST_GET_RANDOM_EXERCISE:
    PATH = "tests/test_resources/test_random"
    RESSOURCE_1 = PATH + "/" + "ressource1.py"
    RESSOURCE_2 = PATH + "/" + "ressource2.py"


TEST_MAIN_FUNCTION_DEFINITION = "def str_to_sentences(long_str: str) -> list[str]:"
TEST_MAIN_FUNCTION_DOCTSTRING = (
    '    """\n    split the given string on punctuation symbols\n    """\n'
)
TEST_RESSOURCES_TEST = """
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
