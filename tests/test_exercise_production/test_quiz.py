from main.exercise_production.quiz import Quiz


def test_simplest_case() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)

    assert simple_quiz.pop_question() == "Capital de la france ?\na) Rome\nb) Paris\n"

    assert simple_quiz.test_answer("b") is True
    assert simple_quiz.test_answer("a") is False
    assert simple_quiz.test_answer("z") is False


def test_multiple_simple_question() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b\n\nQ: How many segments in a square ?\na) 2\nb) 3\nc) 4\nA: c"
    multiple_quiz = Quiz(quiz_file_content=quiz_file_content)

    assert multiple_quiz.pop_question() == "Capital de la france ?\na) Rome\nb) Paris\n"

    assert multiple_quiz.test_answer("b") is True
    assert multiple_quiz.test_answer("a") is False

    assert (
        multiple_quiz.pop_question()
        == "How many segments in a square ?\na) 2\nb) 3\nc) 4\n"
    )

    assert multiple_quiz.test_answer("c") is True
    assert multiple_quiz.test_answer("b") is False


def test_get_correct_answer() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)
    simple_quiz.pop_question()

    assert simple_quiz.get_correct_answer() == "b"


def test_answer_is_string() -> None:
    quiz_file_content = "Q: Capital de la france ?\nA: Paris"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)
    simple_quiz.pop_question()
    assert simple_quiz.test_answer("Paris") is True


def test_be_cool_with_spaces() -> None:
    quiz_file_content = "Q: Repeat after me: I love python\nA: I love python"
    simple_quiz = Quiz(quiz_file_content=quiz_file_content)
    simple_quiz.pop_question()
    assert simple_quiz.test_answer("I  lovepython") is True


def test_has_next_question() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b"
    single_quiz = Quiz(quiz_file_content=quiz_file_content)

    assert single_quiz.has_next_question() is True
    single_quiz.pop_question()
    assert single_quiz.has_next_question() is False

    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b\n\nQ: How many segments in a square ?\na) 2\nb) 3\nc) 4\nA: c"
    double_quiz = Quiz(quiz_file_content=quiz_file_content)

    assert double_quiz.has_next_question() is True
    double_quiz.pop_question()
    assert double_quiz.has_next_question() is True
    double_quiz.pop_question()
    assert double_quiz.has_next_question() is False


def test_score() -> None:
    quiz_file_content = "Q: Capital de la france ?\na) Rome\nb) Paris\nA: b\n\nQ: How many segments in a square ?\na) 2\nb) 3\nc) 4\nA: c"
    quiz = Quiz(quiz_file_content=quiz_file_content)

    quiz.pop_question()
    quiz.test_answer("b")
    quiz.pop_question()
    quiz.test_answer("c")
    assert quiz.get_score() == 1.0

    quiz = Quiz(quiz_file_content=quiz_file_content)

    quiz.pop_question()
    quiz.test_answer("a")
    quiz.pop_question()
    quiz.test_answer("a")
    assert quiz.get_score() == 0.0

    quiz = Quiz(quiz_file_content=quiz_file_content)

    quiz.pop_question()
    quiz.test_answer("a")
    quiz.pop_question()
    quiz.test_answer("c")
    assert quiz.get_score() == 0.5


def test_comment_lines() -> None:
    quiz_file_content = "# This is a comment line\nQ: Capital de la france ?\na) Rome\nb) Paris\nA: b\n\n# This is another comment line\nQ: How many segments in a square ?\na) 2\nb) 3\nc) 4\nA: c"
    quiz = Quiz(quiz_file_content=quiz_file_content)
    quiz.pop_question()
    quiz.test_answer("b")
    quiz.pop_question()
    quiz.test_answer("c")
    assert quiz.get_score() == 1.0
