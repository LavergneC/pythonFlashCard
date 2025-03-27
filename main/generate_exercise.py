import shutil
import sys

from main.constants import RESOURCE_DB_PATH, RESOURCES_PATH
from main.generate_exercise_components.resource_picker import ResourcePicker
from main.generate_exercise_components.resource_storage import RESOURCEStorage
from main.generate_exercise_components.solution_to_exercise import SolutionToExercise


class PythonFlashCards:
    def __init__(
        self,
        resource_csv_path: str = RESOURCE_DB_PATH,
        resource_directory_path: str = RESOURCES_PATH,
    ) -> None:
        self.resource_directory_path = resource_directory_path
        self.resource_storage = RESOURCEStorage(
            resource_csv_path=resource_csv_path,
            resource_directory_path=resource_directory_path,
        )
        self.resource_picker = ResourcePicker(resources=self.resource_storage.read())

    def generate_exercise(self) -> bool:  # TODO test return
        solution_file_name = self.resource_picker.pick()
        if solution_file_name is None:
            return False

        solution_file_path = self.resource_directory_path + "/" + solution_file_name

        shutil.copyfile(solution_file_path, "solution.py")

        solution_content = ""
        with open(solution_file_path) as exercise_file:
            solution_content = exercise_file.read()

        solution_to_ex = SolutionToExercise()
        exercise_content = solution_to_ex.solution_to_exercise(solution_content)

        with open("exercise.py", mode="w") as exercise_file:
            exercise_file.write(exercise_content)

        return True

    def set_exercise_result(self, success: bool) -> None:
        self.resource_picker.set_result(success=success)
        self.resource_storage.write(self.resource_picker.resources)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "test_exercise":
        with open(sys.argv[2]) as exercise_file:
            ste = SolutionToExercise()
            print(ste.solution_to_exercise(solution_content=exercise_file.read()))
        exit()

    pfc = PythonFlashCards()

    while True:
        exercise_found = pfc.generate_exercise()
        if not exercise_found:
            print("No exercise available, come back tomorrow")
            exit()

        print(
            "exercise.py file has been generated, go do it and come back when you're done"
        )
        user_input = input("Did you succeeded ? (y/n) ")
        while user_input not in "yYnN":
            user_input = input("Type 'y' or 'n': ")

        pfc.set_exercise_result(user_input in "yY")

        user_input = input("New exercise ? (y/n) ")
        while user_input not in "yYnN":
            user_input = input("Type 'y' or 'n': ")

        if user_input in "Nn":
            print("Have a good day, see you later ! :)")
            exit()
