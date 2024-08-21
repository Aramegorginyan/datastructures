from collections import deque

class Stack:
    def __init__(self):
        self.elements = deque()

    def push(self,value):
        self.elements.appendleft(value)
    
    def pop(self):
        del self.elements[0]

    def top(self):
        return self.elements[0]
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)
    
st = Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.elements)
print(st.pop())
print(st.elements)
print(st.pop())
print(st.elements)