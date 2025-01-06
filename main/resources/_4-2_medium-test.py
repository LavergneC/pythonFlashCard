import re
import string

"""
Correction : 
    - Levé des erreur si on rentre n'importe quoi et les tester
"""


def input_is_ok(keys: str) -> bool:
    """
    This function checks that all charaters are digits
    >>> input_is_ok('1234894561641180401')
    True
    >>> input_is_ok('1.1')
    False
    >>> input_is_ok('1 51')
    False
    >>> input_is_ok('1 ')
    False
    >>> input_is_ok('45q1')
    False
    """
    return all([c in string.digits for c in keys])


def split_on_digit_change(keys: str) -> list[str]:
    """
    Used to split into identical digits chunck
    >>> split_on_digit_change("4433555555666")
    ['44', '33', '555555', '666']
    >>> split_on_digit_change("02202")
    ['0', '22', '0', '2']
    >>> split_on_digit_change("")
    []
    """
    if not len(keys):
        return []

    current_chunck = str(keys[0])
    output = []

    for index, current_char in enumerate(keys):
        if not index:  # bypass first
            continue

        if current_char == keys[index - 1]:
            current_chunck += current_char
        else:
            output.append(current_chunck)
            current_chunck = str(current_char)

    output.append(current_chunck)

    return output


def split_digit_for_digit_size(chunck: str) -> list[str]:
    """
    Take chunks of identical numbers and sub divide to match keypad length
    >>> split_digit_for_digit_size("0")
    ['0']
    >>> split_digit_for_digit_size("99999")
    ['9999', '9']
    >>> split_digit_for_digit_size("22222")
    ['222', '22']
    """

    keyboad_sizes = {
        "2": 3,
        "3": 3,
        "4": 3,
        "5": 3,
        "6": 3,
        "7": 4,
        "8": 3,
        "9": 4,
        "0": 1,
    }

    digit = chunck[0]
    regex = "." + (".?" * (keyboad_sizes[digit] - 1))

    if len(chunck) > keyboad_sizes[digit]:
        return re.findall(regex, chunck)
    else:
        return [chunck]


def keypad_string(keys: str) -> str:
    """
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    >>> keypad_string("11a1")
    ''
    >>> keypad_string("02222")
    ' ca'
    """
    keys = keys.replace("1", "")

    if not input_is_ok(keys) or not len(keys):
        return ""

    chucks = split_on_digit_change(keys)

    subdivided_chucks = [
        sub_chunk for chuck in chucks for sub_chunk in split_digit_for_digit_size(chuck)
    ]

    keyboad_data = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": " ",
    }

    return "".join(
        [keyboad_data[chuck[0]][len(chuck) - 1] for chuck in subdivided_chucks]
    )
