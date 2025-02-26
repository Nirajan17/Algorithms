# decoding the given string of numbers into alphabets in multiple ways

from functools import lru_cache

class Solution:
    def decodeWays(self, s):
        count = 0
        @lru_cache(None)
        def dfs(i):
            nonlocal count
            if i == len(s):
                count += 1
                return
            
            if s[i] == "0":
                return 
            
            dfs(i+1)
            if i+1 < len(s) and ((s[i]=="1" and i<2) or ((s[i] == "2" and s[i+1] in "0123456") and i<2)):
                dfs(i+2)

        dfs(0)
        return count

if __name__=="__main__":
    s = "1111"
    s1 = Solution()
    print(s1.decodeWays(s))
