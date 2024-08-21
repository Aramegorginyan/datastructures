from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

printer_queue = Queue()

printer_queue.enqueue("job1")
printer_queue.enqueue("job2")
printer_queue.enqueue("job3")

print(printer_queue.peek())
print(printer_queue.dequeue())
print(printer_queue.dequeue())
print(printer_queue.peek())
print(printer_queue.is_empty())
print(printer_queue.size())
print(printer_queue.dequeue())
print(printer_queue.is_empty())
print(printer_queue.dequeue())