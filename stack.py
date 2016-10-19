"""
Author: Alan Lai
Date: Oct 19, 2016

Task:
Implementing a stack

>>> s = Stack()
>>> s.is_empty()
True
>>> s.push(4)
>>> s.push('dog')
>>> s.peek()
'dog'
>>> s.push(True)
>>> s.size()
3
>>> s.is_empty()
False
>>> s.push(8.4)
>>> s.pop()
8.4
>>> s.pop()
True
>>> s.size()
2
"""
class Stack:
    def __init__(self):
        self.content = []

    def push(self, item):
        self.content.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.content.pop()
    
    def peek(self):
        return self.content[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.content)


if __name__ == '__main__':
    import doctest
    doctest.testmod()