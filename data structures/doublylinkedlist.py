class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_front(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def push_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_back(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def insert_after(self, prev_node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        if prev_node == self.tail:
            self.tail = new_node

    def erase_after(self, prev_node):
        if prev_node is None or prev_node.next is None:
            return
        node_to_remove = prev_node.next
        prev_node.next = node_to_remove.next
        if node_to_remove.next:
            node_to_remove.next.prev = prev_node
        if node_to_remove == self.tail:
            self.tail = prev_node

    def clear(self):
        self.head = self.tail = None

    def is_empty(self):
        return self.head is None

    def front(self):
        return None if self.head is None else self.head.data

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head

    def merge(self, other_list):
        if self.tail:
            self.tail.next = other_list.head
            if other_list.head:
                other_list.head.prev = self.tail
        else:
            self.head = other_list.head
        if other_list.tail:
            self.tail = other_list.tail
        other_list.clear()

    def __str__(self):
        current_element = self.head
        output = ""

        while current_element:
            output += (str(current_element.data) + " -> ")
            current_element = current_element.next
        return output

    def sort(self):
        if self.head is None:
            return
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        nodes.sort()
        current = self.head
        for data in nodes:
            current.data = data
            current = current.next

    def unique(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                self.erase_after(current)
            else:
                current = current.next

mylist = DoublyLinkedList()
mylist2 = DoublyLinkedList()