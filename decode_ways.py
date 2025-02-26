# decoding the given string of numbers into alphabets in multiple ways

from functools import lru_cache
from time_wrapper import time_it

class Solution:
    @time_it
    def decodeWays(self, s):
        n = len(s)
        cache = {}
        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return
            if i in cache:
                return cache[i]
            
            ways = dfs(i+1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                ways += dfs(i+2)
            cache[i] = ways
            return ways
        return dfs(0)

if __name__=="__main__":
    s = "1111111111111111"
    s1 = Solution()
    print(s1.decodeWays(s))


# using lrucahche, runtime is 19 units but, without using lrucahce it took 81 units for "111111"