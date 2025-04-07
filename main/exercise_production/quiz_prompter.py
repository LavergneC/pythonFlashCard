from main.exercise_production.quiz import Quiz


def prompt_quiz(quiz: Quiz) -> float:
    while quiz.has_next_question():
        print(quiz.get_question())
        user_input = input("Your answer: ")

        if quiz.test_answer(user_input):
            print("Correct!")
        else:
            print("Wrong, the correct answer was '" + quiz.get_correct_answer() + "'")

    return quiz.get_score()
