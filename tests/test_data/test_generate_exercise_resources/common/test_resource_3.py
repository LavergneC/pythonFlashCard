# test_resource_3.py
import pathlib  # fcPython:keep line
import random
import string
from os import listdir  # fcPython:keep line


def str_to_sentences(long_str: str) -> list[str]:
    """
    split the given string on punctuation symbols
    """
    sentences = []
    current_sentence = ""

    for current_char in long_str:
        if current_char in string.punctuation:
            sentences.append(current_sentence)
            current_sentence = ""
        else:
            current_sentence += current_char

    if current_sentence:
        sentences.append(current_sentence)

    return sentences


def _test_str_to_sentences():
    assert str_to_sentences("Hello word. How are you?") == [
        "Hello word",
        " How are you",
    ]

    assert str_to_sentences("Hello word") == ["Hello word"]
    assert str_to_sentences("Hello word: this will go down! So do This & this too") == [
        "Hello word",
        " this will go down",
        " So do This ",
        " this too",
    ]
