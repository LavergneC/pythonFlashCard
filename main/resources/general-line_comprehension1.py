# general-line_comprehension1.py
def build_matrix(fillWith: int, number_row: int, number_col: 10) -> list[list[int]]:
    """
    This function will build a matrix using the paramaters
    """
    return [[fillWith for _ in range(number_col)] for _ in range(number_row)]


def test_build_matrix():
    assert build_matrix(fillWith=0, number_row=2, number_col=3) == [
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert build_matrix(fillWith=5, number_row=3, number_col=2) == [
        [5, 5],
        [5, 5],
        [5, 5],
    ]
