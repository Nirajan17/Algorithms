# python implementation of queue
# queue can be implmented using list as well but it is efficient to use dequeue

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def deqeue(self):
        if len(self.buffer) == 0:
            return "empty queue"
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

q1 = Queue()
q1.enqueue({
    'company': 'Wallmart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})

q1.enqueue({
    'company': 'Wallmart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})

print(q1.size())

print(q1.deqeue()['company'])