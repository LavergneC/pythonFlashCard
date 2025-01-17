from collections import deque
from io import StringIO  # fcPython:keep line
from unittest.mock import patch  # fcPython:keep line

# Using deque will help adding and poping from left and right
# It's also faster, O(1) vs O(n) from adding in front


class TicketQueue(object):
    def __init__(self):
        self.ticket_queue = deque()

    def add_person(self, name):
        print(f"{name} has been added to the queue")
        self.ticket_queue.append(name)

    def service_person(self):
        """ """
        name = self.ticket_queue.popleft()
        print(f"{name} has been serviced")

    def bypass_queue(self, name):
        """ """
        print(f"{name} has bypassed the queue")
        self.ticket_queue.appendleft(name)


@patch("sys.stdout", new_callable=StringIO)
def test_service_person(fake_out):
    my_queue = TicketQueue()
    my_queue.add_person("Jack")
    my_queue.add_person("Joe")
    my_queue.service_person()
    my_queue.service_person()

    expected_output = (
        "Jack has been added to the queue\n"
        "Joe has been added to the queue\n"
        "Jack has been serviced\n"
        "Joe has been serviced\n"
    )
    assert fake_out.getvalue() == expected_output


@patch("sys.stdout", new_callable=StringIO)
def test_bypass_queue(fake_out):
    my_queue = TicketQueue()

    my_queue.add_person("Jack")
    my_queue.bypass_queue("Joe l'emprouille")
    my_queue.service_person()
    my_queue.service_person()

    expected_output = (
        "Jack has been added to the queue\n"
        "Joe l'emprouille has bypassed the queue\n"
        "Joe l'emprouille has been serviced\n"
        "Jack has been serviced\n"
    )
    assert fake_out.getvalue() == expected_output
