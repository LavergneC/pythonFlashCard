import random
import re
import string

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


def randomized_question(original_question: str) -> tuple[str, dict[str, str]]:
    if "a) " not in original_question:
        return original_question, {}

    question_bloc, answers_bloc = original_question.split("\na) ")
    answers_bloc = "a) " + answers_bloc

    answers: list[str] = [line for line in answers_bloc.split("\n") if len(line) > 1]

    current_answer_letter: int = 0
    random.shuffle(answers)

    transformer: dict[str, str] = {
        string.ascii_letters[idx]: line[0] for idx, line in enumerate(reversed(answers))
    }

    new_question = question_bloc + "\n"
    while len(answers):
        current_letter = string.ascii_letters[current_answer_letter]
        current_answer = answers.pop()

        new_question += f"{current_letter}{current_answer[1:]}\n"
        current_answer_letter += 1

    return new_question, transformer


def apply_transformer_to_user_response(
    user_input: str, transformer: dict[str, str]
) -> str:
    # TODO use question to know if we transform
    if not re.match(pattern="([a-z] ?,)*[a-z]", string=user_input):
        return user_input

    return "".join(
        [
            transformer[letter] if letter in transformer.keys() else letter
            for letter in user_input
        ]
    )


# TODO class randomized toussa
def prompt_quiz(
    quiz: Quiz,
    use_color: bool = True,
    randomize_multiple_choices_question: bool = False,  # TODO switch to True by default
) -> float:
    question_count = 1

    while quiz.has_next_question():
        header = f"Question {question_count}/{quiz.question_count}: "
        question: str = quiz.pop_question()

        transformer = {}
        if randomize_multiple_choices_question:
            question, transformer = randomized_question(original_question=question)

        print(header + question)
        user_input = input("Your answer(s): ")

        if randomize_multiple_choices_question:
            user_input = apply_transformer_to_user_response(
                user_input=user_input, transformer=transformer
            )

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
