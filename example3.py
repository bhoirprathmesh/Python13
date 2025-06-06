class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()

    def type_text(self, new_text):
        self.undo_stack.push(self.text)
        self.text += new_text

    def delete_text(self, num_chars):
        self.undo_stack.push(self.text)
        self.text = self.text[:-num_chars]

    def format_text(self, formatting):
        self.undo_stack.push(self.text)
        # Implement text formatting here

    def undo(self):
        if not self.undo_stack.is_empty():
            self.text = self.undo_stack.pop()

# Example usage:
editor = TextEditor()

editor.type_text("Hello")
print(editor.text)  # Output: Hello

editor.type_text(", world!")
print(editor.text)  # Output: Hello, world!

editor.delete_text(7)
print(editor.text)  # Output: Hello

editor.undo()
print(editor.text)  # Output: Hello, world!
