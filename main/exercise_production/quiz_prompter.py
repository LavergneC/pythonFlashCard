from main.exercise_production.quiz import Quiz


def prompt_quiz_from_path(quiz_file_path: str) -> float:
    with open(quiz_file_path) as quiz_file:
        return prompt_quiz(quiz=Quiz(quiz_file.read()))

    raise RuntimeError("Could not open quiz file")


def prompt_quiz(quiz: Quiz) -> float:
    while quiz.has_next_question():
        print(quiz.get_question())
        user_input = input("Your answer: ")

        if quiz.test_answer(user_input):
            print("Correct!")
        else:
            print("Wrong, the correct answer was '" + quiz.get_correct_answer() + "'")

    return quiz.get_score()
