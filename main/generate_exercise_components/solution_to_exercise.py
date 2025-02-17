from main.constants import (
    KEEP_LINE_TAG,
    STATIC_TEXTS,
)


class SolutionToExercice:
    def solution_to_exercice(self, solution_content) -> str:
        user_file_conttent = ""
        user_file_conttent += self._get_user_import(solution_content)

        if "class" in solution_content:
            user_file_conttent += self._get_main_class_content(solution_content)
            user_file_conttent += STATIC_TEXTS.CLASS_USER_CODE
        else:
            user_file_conttent += self._get_main_function_decraration(solution_content)
            user_file_conttent += STATIC_TEXTS.USER_CODE
        user_file_conttent += "\n\n"
        user_file_conttent += STATIC_TEXTS.TESTS_PART
        user_file_conttent += self._get_tests(solution_content)

        return user_file_conttent

    def _get_user_import(self, file_content: str) -> str:
        """
        From an exercice file content, return the header that will be prompted to the user
        """
        output = ""
        for line in file_content.split("\n"):
            if KEEP_LINE_TAG in line:
                output += line.split(f"  {KEEP_LINE_TAG}")[0] + "\n"
            elif line == "":
                return output + ("\n\n" if len(output) else "")

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

        msg = f"End of docstring not found: {file_content}"
        raise Exception(msg)

    def _get_tests(self, file_content: str) -> str:
        reading = False
        output = ""
        for line in file_content.split("\n"):
            if "def test_" in line or "def _test" in line:
                reading = True

            if reading:
                output += line + "\n"

        return output

    def _get_main_class_content(self, file_content: str) -> str:
        output = ""

        for line in file_content.split("\n"):
            if line.startswith("class"):
                output += line + "\n    pass\n\n"
            elif line.startswith("    def "):
                output += line + "\n        pass\n\n"

        return output
