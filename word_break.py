# given a string s and a word dictionary wordDict, we have to find if s can be segmented into words that are in wordDict

# string = "leetcode" and wordDict = ["leet", "code", "fun"]

class Solution:
    def wordBreak(self, s, word_dict):
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in word_dict:
                if (i+len(w) <= len(s)) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]  # why this, check for the example "catsandog", you will realize why, it might come to your mind that we could have directly written "True" there but NO!!
                if dp[i]:
                    break
        return dp[0]
    
if __name__=="__main__":
    s = "catsandog"
    word_dict = ["cats","dog","sand","and","cat"]

    wb = Solution()
    print(wb.wordBreak(s,word_dict))