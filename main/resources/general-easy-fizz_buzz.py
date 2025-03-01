# general-easy-fizz_buzz.py
def fizz_buzz(numbers: list) -> None:
    """
    Given a list a interger :
    1- Replace number(s) divisible by 3 with 'fizz'
    2- Replace number(s) divisible by 5 wuth 'buzz'
    3- Replace number(s) divisible by both with 'fizzbuzz'
    """
    for i, number in enumerate(numbers):
        if number % 3 == 0:
            numbers[i] = "fizz"
        if number % 5 == 0:
            numbers[i] = "buzz"
        if number % 3 == 0 and number % 5 == 0:
            numbers[i] = "fizzbuzz"


def test_fizz_buzz():
    numbers = [45, 22, 14, 65, 97, 72]
    fizz_buzz(numbers)
    assert numbers == ["fizzbuzz", 22, 14, "buzz", 97, "fizz"]
