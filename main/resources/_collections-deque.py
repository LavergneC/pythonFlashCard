from collections import deque

# Using deque will help adding and poping from left and right
# It's also faster, O(1) vs O(n) from adding in front


class TicketQueue(object):
    def __init__(self):
        self.ticket_queue = deque()

    def add_person(self, name):
        print(f"{name} has been added to the queue")
        self.ticket_queue.append(name)

    def service_person(self):
        """
        >>> my_queue = TicketQueue()
        >>> my_queue.add_person("Jack")
        Jack has been added to the queue
        >>> my_queue.add_person("Joe")
        Joe has been added to the queue
        >>> my_queue.service_person()
        Jack has been serviced
        >>> my_queue.service_person()
        Joe has been serviced
        """
        # print(f"{self.ticket_queue[0]} has been serviced")
        # self.ticket_queue = self.ticket_queue[1:]
        # name = self.ticket_queue.pop(0) <- another solution
        name = self.ticket_queue.popleft()
        print(f"{name} has been serviced")

    def bypass_queue(self, name):
        """
        >>> my_queue = TicketQueue()
        >>> my_queue.add_person("Jack")
        Jack has been added to the queue
        >>> my_queue.bypass_queue("Joe l'emprouille")
        Joe l'emprouille has been serviced
        >>> my_queue.service_person()
        Jack has been serviced
        """
        # self.ticket_queue = [name] + self.ticket_queue
        # self.ticket_queue.insert(0, name)
        self.ticket_queue.appendleft(name)
        self.service_person()
