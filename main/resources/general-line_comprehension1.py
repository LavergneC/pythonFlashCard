def build_matrix(fillWith: int, number_row: int, number_col: 10) -> list[list[int]]:
    """
    This function will build a matrix using the paramaters
    """
    return [[fillWith for _ in range(number_col)] for _ in range(number_row)]


def test_build_matrix():
    assert build_matrix(0, 2, 3) == [[0, 0, 0], [0, 0, 0]]
