from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.items)