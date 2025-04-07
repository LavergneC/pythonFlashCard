from io import StringIO
from unittest.mock import patch

from main.exercise_production.quiz import Quiz
from main.exercise_production.quiz_prompter import prompt_quiz


@patch("sys.stdout", new_callable=StringIO)
def test_correct_answer(fake_out, monkeypatch):
    def answer_typing():
        yield "b"

    question = "Capital of France?\na) Rome\nb) Paris\n"
    quiz_file_content = f"Q: {question}A: b"

    quiz = Quiz(quiz_file_content=quiz_file_content)

    a = answer_typing()
    monkeypatch.setattr("builtins.input", lambda _: next(a))
    score = prompt_quiz(quiz=quiz)

    assert fake_out.getvalue() == f"{question}\nCorrect!\n"
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
    score = prompt_quiz(quiz=quiz)

    assert fake_out.getvalue() == f"{question}\nWrong, the correct answer was 'b'\n"
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
    score = prompt_quiz(quiz=quiz)

    assert score == 0.5

    assert (
        fake_out.getvalue()
        == f"{question_1}\nCorrect!\n{question_2}\nWrong, the correct answer was 'c'\n"
    )
