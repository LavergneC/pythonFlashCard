import shutil
import sys

from main.constants import RESSOURCE_DB_PATH, RESSOURCES_PATH
from main.generate_exercise_components.ressource_picker import RessourcePicker
from main.generate_exercise_components.ressource_storage import RessouceStorage
from main.generate_exercise_components.solution_to_exercise import SolutionToExercice


class PythonFlashCards:
    def __init__(
        self,
        ressource_csv_path: str = RESSOURCE_DB_PATH,
        ressource_directory_path: str = RESSOURCES_PATH,
    ) -> None:
        self.ressource_directory_path = ressource_directory_path
        self.ressource_storage = RessouceStorage(
            ressource_csv_path=ressource_csv_path,
            ressource_directory_path=ressource_directory_path,
        )
        self.ressource_picker = RessourcePicker(
            ressources=self.ressource_storage.read()
        )

    def generate_exercise(self) -> bool:  # TODO test return
        solution_file_name = self.ressource_picker.pick()
        if solution_file_name is None:
            return False

        solution_file_path = self.ressource_directory_path + "/" + solution_file_name

        shutil.copyfile(solution_file_path, "solution.py")

        solution_content = ""
        with open(solution_file_path) as exercise_file:
            solution_content = exercise_file.read()

        solution_to_ex = SolutionToExercice()
        exercise_content = solution_to_ex.solution_to_exercice(solution_content)

        with open("exercise.py", mode="w") as exercise_file:
            exercise_file.write(exercise_content)

        return True

    def set_exercise_result(self, success: bool) -> None:
        self.ressource_picker.set_result(success=success)
        self.ressource_storage.write(self.ressource_picker.ressources)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "test_exercise":
        with open(sys.argv[2]) as exercise_file:
            ste = SolutionToExercice()
            print(ste.solution_to_exercice(solution_content=exercise_file.read()))
        exit()

    pfc = PythonFlashCards()

    while True:
        exercise_found = pfc.generate_exercise()
        if not exercise_found:
            print("No exercise availiable, come back tomorrow")
            exit()

        print(
            "exercise.py file has been generated, go do it and come back when you're done"
        )
        user_input = input("Did you succeded ? (y/n) ")
        while user_input not in "yYnN":
            user_input = input("Type 'y' or 'n': ")

        pfc.set_exercise_result(user_input in "yY")

        user_input = input("New exercise ? (y/n) ")
        while user_input not in "yYnN":
            user_input = input("Type 'y' or 'n': ")

        if user_input in "Nn":
            print("Have a good day, see you later ! :)")
            exit()
