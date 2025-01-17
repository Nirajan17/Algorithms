# python implementation of queue
# queue can be implmented using list as well but it is efficient to use dequeue

from collections import deque

queue = deque()

queue.append(12)
queue.append("nirajan")
queue.append(56)
queue.append(120)

print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue)