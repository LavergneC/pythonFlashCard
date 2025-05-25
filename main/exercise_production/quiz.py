from dataclasses import dataclass


@dataclass
class QuestionAnswer:
    question: str
    answer: str


class Quiz:
    def __init__(self, quiz_file_content: str) -> None:
        self.question_answers = []
        self.current_question = 0
        self._correct_answer_count = 0

        for line in quiz_file_content.split("\n"):
            if len(line) < 2 or line.startswith("#"):
                continue
            if line.startswith("Q: "):
                self.question_answers.append(
                    QuestionAnswer(question=line[3:].rstrip() + "\n", answer="")
                )
            elif line.startswith("A: "):
                self.question_answers[-1].answer = line[3:].rstrip()
            else:
                self.question_answers[-1].question += line.rstrip() + "\n"

    def pop_question(self) -> str:
        self.current_question += 1
        return self.question_answers[self.current_question - 1].question

    def test_answer(self, answer: str) -> bool:
        answer = answer.replace(" ", "")
        success = answer == self.question_answers[
            self.current_question - 1
        ].answer.replace(" ", "")
        if success:
            self._correct_answer_count += 1
        return success

    def get_correct_answer(self) -> str:
        return self.question_answers[self.current_question - 1].answer

    def has_next_question(self) -> bool:
        return self.current_question < self.question_count

    def get_score(self) -> float:
        return self._correct_answer_count / self.question_count

    @property
    def question_count(self) -> int:
        return len(self.question_answers)
