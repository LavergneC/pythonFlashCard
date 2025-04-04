import os
import shutil

from main.exercise_production.solution_to_exercise import SolutionToExercise


def generate_exercise(
    resource_directory_path: str, solution_file_name: str
) -> bool:  # TODO test return
    solution_file_path = resource_directory_path + "/" + solution_file_name

    shutil.copyfile(solution_file_path, "solution.py")

    if os.path.exists(solution_file_path + ".ex"):
        shutil.copyfile(solution_file_path + ".ex", "exercise.py")
        return True

    solution_content = ""
    with open(solution_file_path) as solution_file:
        solution_content = solution_file.read()

    solution_to_ex = SolutionToExercise()
    exercise_content = solution_to_ex.solution_to_exercise(solution_content)

    with open("exercise.py", mode="w") as solution_file:
        solution_file.write(exercise_content)

    return True
