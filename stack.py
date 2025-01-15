# implementing stack in python

# stack = ["Amar", "Akbar", "Anthony", 1, 2, 3]

# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)

# this is also a way to implement stack in python but is not a recommended one

from collections import deque

stack = deque()
stack.append("Nirajan")
stack.append("hello")
stack.append(123)
stack.append("nirajan123")

print(stack)
print(stack.pop())
print(stack.pop())
print(stack)