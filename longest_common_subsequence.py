# finding the length of the longest common subsequence from two strings

class Solution:
    def longcomSubsequence(self, text1, text2):
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
    

if __name__=="__main__":
    sol = Solution()
    r_value = sol.longcomSubsequence("abcd", "ac")
    print(f"Longest subsequence is {r_value}")