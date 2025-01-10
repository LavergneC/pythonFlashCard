TEST_RESSOURCES_PATH = "tests/test_resources"
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
