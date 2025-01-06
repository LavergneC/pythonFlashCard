from collections import Counter
from math import floor

# Correction :
#   - Commencer par coder un commentaire pour savoir où on va, ce qu'on fait au fur et à mesure
#   - Il faut mieux lire la consigne, il ne peut y avoir qu'UN majority element


# V1
def majority_element_indexes(lst):
    """
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times with n the length of lst.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 1, 2, 3, 4])
    []
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([1])
    [0]
    """
    count = Counter(lst)
    majority_elements = {
        element for element in count if count[element] > floor(len(lst) / 2)
    }

    indexes = [index for index, value in enumerate(lst) if value in majority_elements]

    return indexes


# v2 avec la bonne consigne
def majority_element_indexes_v2(lst):
    """
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times with n the length of lst.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 1, 2, 3, 4])
    []
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([1])
    [0]
    >>> majority_element_indexes([])
    []
    """
    majority_element, majority_element_count = Counter(lst).most_common(1)

    if majority_element_count <= len(lst) // 2:
        return []

    return [index for index, value in enumerate(lst) if value == majority_element]
