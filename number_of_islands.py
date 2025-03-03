# # finding the total number of islands from a grid
# # 1 represents land, 0 represents water, and we have gird of 1's and 0's

# from collections import deque

# def count_islands(grid):
#     if not grid:
#         return 0
    
#     rows, cols = len(grid), len(grid[0])
#     queue1 = deque()
#     island_visited = set()
#     island_count = 0

#     def bfs(i, j, island_visited):
#         # Base case: if already visited or not land, return
#         if (i, j) in island_visited or not (0 <= i < rows and 0 <= j < cols) or grid[i][j] != 1:
#             return
        
#         # Mark current cell as visited
#         island_visited.add((i, j))
        
#         # Add all 4-directional neighbors to queue
#         for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
#             queue1.append((ni, nj))
        
#         # Process the queue recursively
#         while queue1:
#             ni, nj = queue1.popleft()
#             bfs(ni, nj, island_visited)

#     # Iterate through the grid
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == 1 and (i, j) not in island_visited:
#                 bfs(i, j, island_visited)
#                 island_count += 1  # Increment for each new island
    
#     return island_count

# # Example usage:
# grid = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1]
# ]
# print(count_islands(grid))  # Outputs 3



# let's try on my own
from collections import deque
class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        island_visited = set()
        island_count = 0
        queue = deque()

        def bfs(i, j):
            if (i, j) in island_visited or not (0 <= i < rows and 0 <= j < cols) or grid[i][j] != "1":
                return

            island_visited.add((i, j))

            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if (0<= ni < rows) and (0<= nj < cols) and grid[ni][nj] == "1" and (ni, nj) not in island_visited:
                    queue.append((ni,nj))

            while queue:
                ni, nj = queue.popleft()
                bfs(ni, nj)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in island_visited:
                    bfs(i, j)
                    island_count += 1

        return island_count
    
if __name__=="__main__":
    s = Solution()
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(s.numIslands(grid))
