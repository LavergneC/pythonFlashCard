def build_matrix(fillWith: int, number_row: int, number_col: 10) -> list[list[int]]:
    """
    This function will build a matric using the paramaters
    >>> build_matrix(0, 2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[fillWith for _ in range(number_col)] for _ in range(number_row)]
