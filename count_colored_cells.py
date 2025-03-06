# leetcode 2579 :: counting total number of colored cells after n minutes
from collections import deque
def solution(n):
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    visit = set()
    queue = deque()
    queue.append((0,0))

    for _ in range(n-1):

        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()

            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if (new_x, new_y) not in visit:
                    visit.add((new_x, new_y))
                    queue.append((new_x, new_y))
    return len(visit)+1

print(solution(2))
