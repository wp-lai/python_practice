"""
Author: Alan Lai

Task:
Implement a queue

>>> q = Queue()
>>> q.is_empty()
True
>>> q.enqueue(4)
>>> q.enqueue('dog')
>>> q.enqueue(True)
>>> q.size()
3
>>> q.is_empty()
False
>>> q.enqueue(8.4)
>>> q.dequeue()
4
>>> q.dequeue()
'dog'
>>> q.size()
2
"""
from collections import deque


class Queue:
    def __init__(self, iterable=None):
        if iterable is None:
            self.queue = deque()
        else:
            self.queue = deque(iterable)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
