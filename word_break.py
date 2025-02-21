# given a string s and a word dictionary wordDict, we have to find if s can be segmented into words that are in wordDict

# string = "leetcode" and wordDict = ["leet", "code", "fun"]

class Solution:
    def wordBreak(self, s, word_dict):

        if not s:
            return True  
        
        for i in range(1, len(s) + 1): 
            first = s[:i]
            
            if first in word_dict:
                if self.wordBreak(s[i:], word_dict):  # Check the remaining part
                    return True
        
        return False