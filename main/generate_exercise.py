import random
import shutil
from os import listdir
from os.path import isfile, join

from main.constants import RESSOUCES_PATH
from main.solution_to_exercise import SolutionToExercice


class PythonFlashCards:
    def generate_exercise(self) -> None:
        solution_file_path = self._get_random_exercise_file_name(RESSOUCES_PATH)
        shutil.copyfile(solution_file_path, "solution.py")

        solution_content = ""
        with open(solution_file_path) as exercise_file:
            solution_content = exercise_file.read()

        solution_to_ex = SolutionToExercice()
        exercise_content = solution_to_ex.solution_to_exercice(solution_content)

        with open("exercise.py", mode="w") as exercise_file:
            exercise_file.write(exercise_content)

    def _get_random_exercise_file_name(self, ressources_directory) -> str:
        """
        Return a random file name from the resources directory
        """
        onlyfiles = [
            join(ressources_directory, file_name)
            for file_name in listdir(ressources_directory)
            if isfile(join(ressources_directory, file_name))
        ]

        return random.choice(onlyfiles)


if __name__ == "__main__":
    pfc = PythonFlashCards()
    pfc.generate_exercise()
