class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def print_stack(self):
        print(self.items)

    def size(self):
        return len(self.items)

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0


# Example usage
stack = Stack()

# Pushing items onto the stack
stack.push("Sudeshna")
stack.push("Ritam")
stack.push("Modhu")

# Print the items in the stack
print("Items in the stack:")
stack.print_stack()

# Get the size of the stack
print("\nSize of stack:", stack.size())

# Get the top item in the stack
print("\nTop item in the stack:", stack.top())

# Pop an item from the stack
print("\nPopped item:", stack.pop())

# Print the items in the stack after popping
print("\nItems in the stack:")
stack.print_stack()

# Check if the stack is empty
print("\nIs stack empty?", stack.is_empty())







    