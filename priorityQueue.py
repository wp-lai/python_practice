"""
Author: Alan Lai

Task:
Implements a Priority Queue

>>> q = PriorityQueue()
>>> for i in [5, 8, 4, 2]:
...     q.push(i)
>>> q.pop()
2
>>> q.min()
4
"""


class PriorityQueue:
    """Heap-based priority queue implementation"""

    def __init__(self):
        self.heap = [None]

    def __len__(self):
        return len(self.heap) - 1

    def push(self, key):
        self.heap.append(key)
        current = len(self)
        while current > 1:
            parent = current // 2
            if key < self.heap[parent]:
                self.heap[parent], self.heap[current] = key, self.heap[parent]
                current = parent
            else:
                break

    def min(self):
        return self.heap[1]

    def pop(self):
        """Removes the minimum element from the queue"""
        popvalue = self.heap[1]
        swapvalue = self.heap.pop()
        self.heap[1] = swapvalue

        current = 1
        while True:
            left = current * 2
            right = current * 2 + 1
            if len(self) < left:
                break
            elif len(self) < right:
                if self.heap[current] > self.heap[left]:
                    self.heap[current], self.heap[left] = \
                        self.heap[left], self.heap[current]
                    current = left
                else:
                    break
            else:
                current_min = min(self.heap[current], self.heap[left],
                                  self.heap[right])
                if current_min == self.heap[current]:
                    break
                elif current_min == self.heap[left]:
                     self.heap[current], self.heap[left] = \
                        self.heap[left], self.heap[current]
                     current = left
                else:
                    self.heap[current], self.heap[right] = \
                        self.heap[right], self.heap[current]
                    current = right
        return popvalue


if __name__ == '__main__':
    import doctest
    doctest.testmod()

