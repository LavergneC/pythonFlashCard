# Meilleur façon de faire :
def f(x):
    """
    >>> f(10)
    Args: 10
    'Valid input'
    >>> f(-1)
    Traceback (most recent call last):
    ...
    ValueError: Invalid input
    """
    if x <= -1:
        raise ValueError("Invalid input")
    print(f"Args: {x}")
    return "Valid input"


# A faire si les outils sont pas présent
def lst_one_more(lst1, lst2):
    assert len(lst1) == len(lst2), "Length of lists are not the same"
    for i in range(len(lst1)):
        lst1[i] = lst2[i] + 1


lst1 = [1, 1, 1]
lst2 = [1, 2, 3]
lst_one_more(lst1, lst2)
for i, x in enumerate(lst1):
    assert x == lst2[i] + 1
