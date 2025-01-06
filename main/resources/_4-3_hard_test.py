class Link:
    def __init__(self, id: int, linked_link=None):
        self.id = id
        self.linked_link = linked_link

    def __repr__(self):
        if self.linked_link:
            return f"Link({self.id}, {str(self.linked_link)})"
        else:
            return f"Link({self.id})"


def pop_smallest_set_element(link_set: set[tuple]):
    smallest_id = 9999
    smallest_tuple = None

    for id, link in link_set:
        if id < smallest_id:
            smallest_id = id
            smallest_tuple = (id, link)

    if smallest_tuple:
        link_set.remove(smallest_tuple)
        return smallest_tuple
    else:
        return (None, None)


def merge_k_linked_lists(linked_lists: list[Link]) -> Link:
    """
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))

    >>> print(merge_k_linked_lists([
    ...     Link(3, Link(4)),
    ...     Link(1, Link(2))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))

    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2, Link(2))),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(4)))))

    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3)
    ... ]))
    Link(1, Link(2, Link(3)))

    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))

    >>> print(merge_k_linked_lists([]))
    Traceback (most recent call last):
    ...
    ValueError: Invalid input

    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     None,
    ...     Link(3, Link(4))
    ... ]))
    Traceback (most recent call last):
    ...
    ValueError: Invalid input
    """
    if not len(linked_lists) or None in linked_lists:
        raise ValueError("Invalid input")

    input_set = set()
    for link in linked_lists[:]:
        if link and link.linked_link:
            cpy_link = Link(link.linked_link.id, link.linked_link.linked_link)
            input_set.add((link.id, cpy_link))
        elif link:
            input_set.add((link.id, None))

    output_link = Link(0, None)
    tail_link = output_link

    small_id, small_linked_link = pop_smallest_set_element(input_set)
    while small_id:
        tail_link.linked_link = Link(id=small_id)
        tail_link = tail_link.linked_link

        if small_linked_link:
            input_set.add((small_linked_link.id, small_linked_link.linked_link))

        small_id, small_linked_link = pop_smallest_set_element(input_set)

    return output_link.linked_link
