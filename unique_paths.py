# finding number of unique paths in a grid from 0,0 to m,n

# class Solution:
#     def uniqueWays(self, m, n):
#         grid = [[1 for _ in range(m)] for _ in range(n)]

#         for i in range(m-2, -1, -1):
#             for j in range(n-2, -1, -1):
#                 if i < m and j < n:
#                     grid[j][i] = grid[j][i+1] + grid[j+1][i]

#         return grid[0][0]
    
# if __name__=="__main__":
#     s = Solution()
#     print(s.uniqueWays(3,7))

# let's try the combinatorial solution

import math
class Solution:
    def uniqueWays(self, m, n):
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
    
if __name__=="__main__":
    s = Solution()
    print(s.uniqueWays(3,7))