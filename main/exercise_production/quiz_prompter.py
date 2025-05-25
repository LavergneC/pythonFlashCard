import random
import string

from main.exercise_production.quiz import Quiz


class QuizPrompter:
    RED = "91"
    GREEN = "92"

    @staticmethod
    def get_quiz_from_path(quiz_file_path: str) -> Quiz:
        with open(quiz_file_path) as quiz_file:
            return Quiz(quiz_file.read())

        raise FileNotFoundError(f"Could not open quiz file {quiz_file_path}")

    def __init__(self, quiz: Quiz, use_color=True, use_random=True) -> None:
        self._use_color = use_color
        self._use_random = use_random

        self._quiz = quiz

    def prompt_quiz(self) -> float:
        self._question_count = 1

        while self._quiz.has_next_question():
            self._prompt_question()
            self._question_count += 1

        return self._quiz.get_score()

    def _prompt_question(self):
        header = f"Question {self._question_count}/{self._quiz.question_count}: "
        question: str = self._quiz.pop_question()

        current_question_needs_random: bool = self._use_random and "a) " in question

        if current_question_needs_random:
            question = self._randomized_question(original_question=question)

        print(header + question)
        user_input = input("Your answer(s): ")

        if current_question_needs_random:
            user_input = self._apply_transformer_to_user_response(user_input=user_input)

        if self._quiz.test_answer(user_input):
            print(self._colorize("Correct!", self.GREEN))
        else:
            self._print_wrong_answer()

        print()

    def _randomized_question(self, original_question: str) -> str:
        if "a) " not in original_question:
            return original_question

        question_bloc, answers_bloc = original_question.split("\na) ")
        answers_bloc = "a) " + answers_bloc

        answers: list[str] = [
            line for line in answers_bloc.split("\n") if len(line) > 1
        ]

        current_answer_letter: int = 0
        random.shuffle(answers)

        self._transformer: dict[str, str] = {
            string.ascii_letters[idx]: line[0]
            for idx, line in enumerate(reversed(answers))
        }

        new_question = question_bloc + "\n"
        while len(answers):
            current_letter = string.ascii_letters[current_answer_letter]
            current_answer = answers.pop()

            new_question += f"{current_letter}{current_answer[1:]}\n"
            current_answer_letter += 1

        return new_question

    def _apply_transformer_to_user_response(self, user_input: str) -> str:
        return "".join(
            [
                self._transformer[letter]
                if letter in self._transformer.keys()
                else letter
                for letter in user_input
            ]
        )

    def _print_wrong_answer(self):
        print(
            self._colorize(
                f"Wrong, the correct answer was '{self._quiz.get_correct_answer()}'",
                self.RED,
            )
        )

    def _colorize(self, text: str, color_code: str) -> str:
        """Apply color to text if self.use_color is True."""
        if self._use_color:
            return f"\033[{color_code}m{text}\033[0m"
        return text
