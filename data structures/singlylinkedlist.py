class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def push_front(self,data):
        if not isinstance(data,Node):
            data = Node(data)

        if self.head is None:
            self.head = data
            self.tail = data
        else:
            data.next = self.head
            self.head = data

    def pop_front(self):
        current_element = self.head
        self.head = self.head.next
        return current_element.data

    def __str__(self):
        current_element = self.head
        output = ""

        while current_element:
            output += (str(current_element.data) + " -> ")
            current_element = current_element.next
        return output
    
    def insert_after(self,prev_node, data):
        if prev_node != None:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def erase_after(self,prev_node):
        prev_node.next = prev_node.next.next
    
    def clear(self):
        self.head = None
        
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def front(self):
        return self.tail.data
    
    def reverse(self):
        prevnode = None
        current_element = self.head

        while current_element is not None:
            next = current_element.next
            current_element.next = prevnode
            prevnode = current_element
            current_element = next
        self.head = prevnode

    def merge(self,other_list):
        current_element = other_list.head
        if not isinstance(other_list,LinkedList):
            return
        else:
            while current_element:
                self.tail.next = current_element
                current_element = current_element.next
                return

    def sort_list(self):
        swapped = True
        while swapped:
            swapped = False
            current_element = self.head
            while current_element is not None and current_element.next is not None:
                if current_element.data > current_element.next.data:
                    current_element.data, current_element.next.data = current_element.next.data, current_element.data
                    swapped = True
                current_element = current_element.next

    def unique(self):
        current_element = self.head
        
        while current_element is not None and current_element.next is not None:
            if current_element.data == current_element.next.data:
                current_element.next = current_element.next.next
            else:
                current_element = current_element.next

mylist = LinkedList()
mylist2 = LinkedList()