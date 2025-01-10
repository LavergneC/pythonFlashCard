import random
import shutil
from os import listdir
from os.path import isfile, join

from main.constants import (
    KEEP_LINE_TAG,
    RESSOUCES_PATH,
    TEXT_TESTS_PART,
    TEXT_USER_CODE,
)


class PythonFlashCards:
    def generate_exercise(self):
        exercise_file_path = self._get_random_exercise_file_name(RESSOUCES_PATH)

        shutil.copyfile(exercise_file_path, "solution.py")

        exercise = ""
        with open(exercise_file_path) as exercise_file:
            exercise = exercise_file.read()

        user_file_conttent = ""
        user_file_conttent += self._get_user_import(exercise)
        user_file_conttent += self._get_main_function_decraration(exercise)
        user_file_conttent += TEXT_USER_CODE
        user_file_conttent += "\n\n"
        user_file_conttent += TEXT_TESTS_PART
        user_file_conttent += self._get_tests(exercise)

        with open("exercise.py", mode="w") as exercise_file:
            exercise_file.write(user_file_conttent)

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

    def _get_user_import(self, file_content: str) -> str:
        """
        From an exercice file content, return the header that will be prompted to the user
        """
        output = ""
        for line in file_content.split("\n"):
            if KEEP_LINE_TAG in line:
                output += line.split(f"  {KEEP_LINE_TAG}")[0] + "\n"
            elif line == "":
                return output + "\n\n"

        raise Exception("End of import not found")

    def _get_main_function_decraration(self, file_content: str) -> str:
        reading = False
        output = ""
        seen_doctring_triple_quote = False

        for line in file_content.split("\n"):
            if "def " in line:
                reading = True

            if reading:
                output += line + "\n"

            if '"""' in line and not seen_doctring_triple_quote:
                seen_doctring_triple_quote = True
            elif '"""' in line and seen_doctring_triple_quote:
                return output

        raise Exception("End of docstring not found")

    def _get_tests(self, file_content: str) -> str:
        reading = False
        output = ""
        for line in file_content.split("\n"):
            if "def test_" in line:
                reading = True

            if reading:
                output += line + "\n"

        return output


if __name__ == "__main__":
    pfc = PythonFlashCards()
    pfc.generate_exercise()
