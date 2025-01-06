import random
import shutil
from os import listdir
from os.path import isfile, join

from main.constants import KEEP_LINE_TAG, RESSOUCES_PATH


class PythonFlashCards:
    def generate_exercise(self):
        exercise_file_path = self._get_random_exercise_file_name(RESSOUCES_PATH)

        shutil.copyfile(exercise_file_path, "solution.py")

        exercise = ""
        with open(exercise_file_path) as exercise_file:
            exercise = exercise_file.read()

        user_file_conttent = ""
        user_file_conttent += self._get_user_import(exercise)

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
        for line in file_content:
            if KEEP_LINE_TAG in line:
                output += line
            elif line == "\n":
                return output

        return output


if __name__ == "__main__":
    pfc = PythonFlashCards()
    pfc.generate_exercise()
