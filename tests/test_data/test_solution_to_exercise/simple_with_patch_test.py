from io import StringIO
from unittest.mock import patch


def print_hello_world() -> None:
    print("Hello world !")


@patch("sys.stdout", new_callable=StringIO)
def test_service_person(fake_out):
    print_hello_world()
    assert fake_out.getvalue() == "Hello world !\n"
