
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
    
    def size(self):
        return len(self.container)
    
    def index(self):
        return self.container.index
    
    def __iter__(self):
        return iter(self.container)
    
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0

if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))    