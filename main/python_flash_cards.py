import sys

from main.constants import RESOURCE_DB_PATH, RESOURCES_PATH
from main.exercise_production import generate_exercise
from main.exercise_production.solution_to_exercise import SolutionToExercise
from main.resources_management.resource_picker import ResourcePicker
from main.resources_management.resource_storage import ResourceStorage


class PythonFlashCards:
    def __init__(
        self,
        resource_csv_path: str = RESOURCE_DB_PATH,
        resource_directory_path: str = RESOURCES_PATH,
    ) -> None:
        self.resource_directory_path = resource_directory_path
        self.resource_storage = ResourceStorage(
            resource_csv_path=resource_csv_path,
            resource_directory_path=resource_directory_path,
        )
        self.resource_picker = ResourcePicker(resources=self.resource_storage.read())

    def get_exercise(self) -> bool:
        solution_file_name = self.resource_picker.pick()
        if solution_file_name is None:
            return False

        if solution_file_name.endswith(".quiz"):
            return True

        return generate_exercise.generate_exercise(
            resource_directory_path=self.resource_directory_path,
            solution_file_name=solution_file_name,
        )

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
        exercise_found = pfc.get_exercise()
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
