# finding the longest increasing subsequence in an array

class Solution:
    def longestSubsequence(self, nums):
        lss = [1]*(len(nums))
        lss[len(nums)-1] = 0 # last index has subquence of length 0

        for i in range(len(nums)-2, 1, -1):
            if nums[i+1] > nums[i]:
                lss[i] = max(lss[i], 1 + lss[i+1])
        
        return max(lss)
    

