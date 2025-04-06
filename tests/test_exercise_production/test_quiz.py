from main.exercise_production.quiz import Quiz


def test_simplest_case() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)

    assert simple_quiz.get_question() == "Capital de la france ?\na) Rome\nb) Paris\n"

    assert simple_quiz.test_answer("b") is True
    assert simple_quiz.test_answer("a") is False
    assert simple_quiz.test_answer("z") is False


def test_multiple_simple_question() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b\n\nQ: How many segments in a square ?\na) 2\nb) 3\nc) 4\nA: c"
    multiple_quiz = Quiz(quiz_file_content=quiz_file_content)

    assert multiple_quiz.get_question() == "Capital de la france ?\na) Rome\nb) Paris\n"

    assert multiple_quiz.test_answer("b") is True
    assert multiple_quiz.test_answer("a") is False

    assert (
        multiple_quiz.get_question()
        == "How many segments in a square ?\na) 2\nb) 3\nc) 4\n"
    )

    assert multiple_quiz.test_answer("c") is True
    assert multiple_quiz.test_answer("b") is False


def test_get_correct_answer() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)
    simple_quiz.get_question()

    assert simple_quiz.get_correct_answer() == "b"


def test_answer_is_string() -> None:
    quiz_file_content = "Q: Capital de la france ?\nA: Paris"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)
    simple_quiz.get_question()
    assert simple_quiz.test_answer("Paris") is True


def test_be_cool_with_spaces() -> None:
    quiz_file_content = "Q: Repeat after me: I love python\nA: I love python"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)
    simple_quiz.get_question()
    assert simple_quiz.test_answer("I  lovepython") is True
