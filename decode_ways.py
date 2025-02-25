# decoding the given string of numbers into alphabets in multiple ways

class Solution:
    def decodeWays(self, s):
        count = 0
        
        def dfs(i):
            nonlocal count
            if i == len(s):
                count += 1
                return
            
            if s[i] == "0":
                return 
            
            dfs(i+1)
            if i+1 < len(s) and (s[i]=="1" or (s[i] == "2" and s[i+1] in "0123456")):
                dfs(i+2)

        dfs(0)
        return count

if __name__=="__main__":
    s = "06"
    s1 = Solution()
    print(s1.decodeWays(s))
