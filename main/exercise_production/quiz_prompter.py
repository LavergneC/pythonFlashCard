from main.exercise_production.quiz import Quiz


def colorize(text: str, color_code: str, use_color: bool = True) -> str:
    """Apply color to text if use_color is True."""
    if use_color:
        return f"\033[{color_code}m{text}\033[0m"
    return text


def get_quiz_from_path(quiz_file_path: str) -> Quiz:
    with open(quiz_file_path) as quiz_file:
        return Quiz(quiz_file.read())

    raise FileNotFoundError(f"Could not open quiz file {quiz_file_path}")


def prompt_quiz(quiz: Quiz, use_color: bool = True) -> float:
    question_count = 1

    while quiz.has_next_question():
        print(f"Question {question_count}/{quiz.question_count}: {quiz.get_question()}")
        user_input = input("Your answer(s): ")

        if quiz.test_answer(user_input):
            print(colorize("Correct!", "92", use_color))
        else:
            print(
                colorize(
                    f"Wrong, the correct answer was '{quiz.get_correct_answer()}'",
                    "91",
                    use_color,
                )
            )

        print()
        question_count += 1

    return quiz.get_score()
