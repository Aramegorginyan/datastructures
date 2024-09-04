class Dequeue:
    def __init__(self):
        self.items = []

    def push_front(self,value):
        self.items.insert(0,value)

    def push_back(self,value):
        self.items.append(value)

    def pop_front(self):
        self.items.pop(0)

    def pop_back(self):
        self.items.pop()
    
    def empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items.pop(0)
    
    def back(self):
        return self.items.pop()
    
    def clear(self):
        for i in range(len(self.items)-1,-1,-1):
            del self.items[i]

    def operator(self,index):
        try:
            return self.items[index]
        except:
            raise IndexError("Out of range")
    
    def insert(self,position,value):
        try:
            self.items[position] = value
        except:
            raise IndexError("Out of range")

    def erase(self,position):
        try:
            del self.items[position]
        except:
            raise IndexError("Out of range")
        
d = Dequeue()
d.push_back(2)
d.push_back(3)
d.push_front(1)
print(d.items)
print(d.back())
print(d.items)