from io import StringIO
from unittest.mock import patch

import pytest

from main.exercise_production.quiz import Quiz
from main.exercise_production.quiz_prompter import QuizPrompter
from tests.constants_test import TEST_QUIZ


@patch("sys.stdout", new_callable=StringIO)
def test_correct_answer(fake_out, monkeypatch):  # type: ignore
    def answer_typing():
        yield "b"

    question = "Capital of France?\na) Rome\nb) Paris\n"
    quiz_file_content = f"Q: {question}A: b"

    quiz = Quiz(quiz_file_content=quiz_file_content)

    a = answer_typing()
    monkeypatch.setattr("builtins.input", lambda _: next(a))

    quiz_prompter = QuizPrompter(quiz=quiz, use_color=False, use_random=False)
    score = quiz_prompter.prompt_quiz()

    assert fake_out.getvalue() == f"Question 1/1: {question}\nCorrect!\n\n"
    assert score == 1.0


@patch("sys.stdout", new_callable=StringIO)
def test_incorrect_answer(fake_out, monkeypatch):
    def answer_typing():
        yield "a"

    question = "Capital of France?\na) Rome\nb) Paris\n"
    quiz_file_content = f"Q: {question}A: b"
    quiz = Quiz(quiz_file_content=quiz_file_content)

    a = answer_typing()
    monkeypatch.setattr("builtins.input", lambda _: next(a))

    quiz_prompter = QuizPrompter(quiz=quiz, use_color=False, use_random=False)
    score = quiz_prompter.prompt_quiz()

    assert (
        fake_out.getvalue()
        == f"Question 1/1: {question}\nWrong, the correct answer was 'b'\n\n"
    )
    assert score == 0.0


@patch("sys.stdout", new_callable=StringIO)
def test_multiple_questions(fake_out, monkeypatch):
    def answer_typing():
        yield "b"
        yield "a"

    question_1 = "Capital of France?\na) Rome\nb) Paris\n"
    question_2 = "How many sides does a square have?\na) 3\nb) 5\nc) 4\n"

    quiz_file_content = f"Q: {question_1}A: b\nQ: {question_2}\nA: c"
    quiz = Quiz(quiz_file_content=quiz_file_content)

    a = answer_typing()
    monkeypatch.setattr("builtins.input", lambda _: next(a))
    quiz_prompter = QuizPrompter(quiz=quiz, use_color=False, use_random=False)

    score = quiz_prompter.prompt_quiz()

    assert score == 0.5

    assert (
        fake_out.getvalue()
        == f"Question 1/2: {question_1}\nCorrect!\n\nQuestion 2/2: {question_2}\nWrong, the correct answer was 'c'\n\n"
    )


def test_get_quiz_from_path():
    quiz = QuizPrompter.get_quiz_from_path(TEST_QUIZ.PATH)
    assert quiz.pop_question() == "This is the first question.\n"


def test_get_quiz_from_bad_path_raise_error():
    with pytest.raises(FileNotFoundError):
        QuizPrompter.get_quiz_from_path("very/bad/path.quiz")


@pytest.fixture
def mock_random_shuffle():
    with patch("random.shuffle") as mock_shuffle:

        def side_effect(lst):
            # Doing nothing will reverse the answers
            # order within the randomized_question() function
            pass

        mock_shuffle.side_effect = side_effect
        yield mock_shuffle


@patch("sys.stdout", new_callable=StringIO)
def test_randomize_multiple_choices_question_correct_answer(
    fake_out,
    monkeypatch,
    mock_random_shuffle,
):
    def answer_typing():
        yield "a"

    question = "Capital of France?\na) Rome\nb) Paris\n"
    quiz_file_content = f"Q: {question}A: b"

    quiz = Quiz(quiz_file_content=quiz_file_content)

    # User types "a" witch is correct because the order has been randomized
    a = answer_typing()
    monkeypatch.setattr("builtins.input", lambda _: next(a))

    quiz_prompter = QuizPrompter(quiz=quiz, use_color=False, use_random=True)
    quiz_prompter.prompt_quiz()

    # Question choices are reversed
    mixed_question = "Capital of France?\na) Paris\nb) Rome\n"
    assert fake_out.getvalue() == f"Question 1/1: {mixed_question}\nCorrect!\n\n"


def test_randomized_question_on_normal_question():
    question = "Number of finger on a normal hand ?\n"

    quiz_prompter = QuizPrompter(quiz=Quiz(""), use_color=False, use_random=True)

    assert quiz_prompter._randomized_question(question) == question


def test_randomized_question_mix_question(mock_random_shuffle):
    two_choices_question = "Capital de la france ?\na) Rome\nb) Paris\n"
    four_choices_question = (
        "Capital de la france ?\na) Rome\nb) Paris\nc) Berlin\nd) London\n"
    )
    quiz_prompter = QuizPrompter(quiz=Quiz(""), use_color=False, use_random=True)

    new_question = quiz_prompter._randomized_question(two_choices_question)
    assert new_question == "Capital de la france ?\na) Paris\nb) Rome\n"

    new_question = quiz_prompter._randomized_question(four_choices_question)
    assert (
        new_question
        == "Capital de la france ?\na) London\nb) Berlin\nc) Paris\nd) Rome\n"
    )


def test_randomized_question_transformer_matrix(mock_random_shuffle):
    four_choices_question = (
        "Capital de la france ?\na) Rome\nb) Paris\nc) Berlin\nd) London\n"
    )
    quiz_prompter = QuizPrompter(quiz=Quiz(""), use_color=False, use_random=True)

    quiz_prompter._randomized_question(four_choices_question)
    assert quiz_prompter._transformer == {
        "a": "d",
        "b": "c",
        "c": "b",
        "d": "a",
    }


def test_apply_transformer_to_user_response():
    transformer: dict[str, str] = {
        "a": "b",
        "b": "a",
        "c": "c",
    }
    user_input = "a,b,c"
    quiz_prompter = QuizPrompter(quiz=Quiz(""), use_color=False, use_random=True)
    quiz_prompter._transformer = transformer
    assert quiz_prompter._apply_transformer(source=user_input) == "b,a,c"


@patch("sys.stdout", new_callable=StringIO)
def test_wrong_answer_with_random(fake_out, monkeypatch, mock_random_shuffle):
    def answer_typing():
        yield "b"

    question = "Capital of France?\na) Rome\nb) Paris\n"
    quiz_file_content = f"Q: {question}A: b"

    quiz = Quiz(quiz_file_content=quiz_file_content)

    a = answer_typing()
    monkeypatch.setattr("builtins.input", lambda _: next(a))

    quiz_prompter = QuizPrompter(quiz=quiz, use_color=False, use_random=True)
    score = quiz_prompter.prompt_quiz()

    mixed_question = "Capital of France?\na) Paris\nb) Rome\n"
    assert (
        fake_out.getvalue()
        == f"Question 1/1: {mixed_question}\nWrong, the correct answer was 'a'\n\n"
    )
    assert score == 0.0
