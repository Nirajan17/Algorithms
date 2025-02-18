# finding total number of ways to climb stairs

# this problem is solved similar to that of fibonacci series
# first calculate the base case and later calculate for others based on that base case

class Solution:
    def climbStairs(self, n):
        
        for i in range(n+1):
            if i == n or n+1:
                first, second = 1, 1
            else:
                result = first + second
                first, second = second, result
        return result