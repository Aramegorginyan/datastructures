from collections import deque

class Stack:
    def __init__(self):
        self.elements = deque()

    def push(self, value):
        self.elements.appendleft(value)
    
    def pop(self):
        return self.elements.popleft() if not self.isEmpty() else None

    def top(self):
        return self.elements[0] if not self.isEmpty() else None
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)

class TextEditor:
    def __init__(self):
        self.text = []
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def type_character(self, char):
        self.text.append(char)
        self.undo_stack.push(('type',char))
        self.redo_stack = Stack()

    def undo(self):
        if not self.undo_stack.isEmpty():
            action,char = self.undo_stack.pop()
            if action == 'type':
                self.text.pop()
                self.redo_stack.push(('type',char))

    def redo(self):
        if not self.redo_stack.isEmpty():
            action, char = self.redo_stack.pop()
            if action == 'type':
                self.text.append(char)
                self.undo_stack.push(('type', char))

    def view_text(self):
        return ''.join(self.text)


editor = TextEditor()
editor.type_character('aramee')
editor.type_character('dSb')
editor.type_character('csa')
print(editor.view_text())
editor.undo()
print(editor.view_text())
editor.redo()
print(editor.view_text())