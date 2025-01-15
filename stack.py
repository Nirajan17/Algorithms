# implementing stack in python

# stack = ["Amar", "Akbar", "Anthony", 1, 2, 3]

# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)

# this is also a way to implement stack in python but is not a recommended one

# from collections import deque

# stack = deque()
# stack.append("Nirajan")
# stack.append("hello")
# stack.append(123)
# stack.append("nirajan123")

# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack)

# let's make a stack class of our own using the deque collection

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False
        
    def peek(self):
        return self.container[-1]
    
    def len(self):
        return len(self.container)
    
    def index(self):
        return self.container.index
    
    def __iter__(self):
        return iter(self.container)


def reverse_string(string):
    stack1 = Stack()
    for item in string:
        stack1.push(item)

    for _ in range(stack1.len()):
        print(stack1.peek())


if __name__ == "__main__":
    string = input("Enter the string you want to reverse.")
    reverse_string(string)


