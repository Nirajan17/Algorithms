# finding the longest increasing subsequence in an array

class Solution:
    def longestSubsequence(self, nums):
        if not nums:
            return 0

        lss = [1] * len(nums)  
        
        for i in range(len(nums) - 2, -1, -1):  
            for j in range(i + 1, len(nums)): 
                if nums[j] > nums[i]:  
                    lss[i] = max(lss[i], 1 + lss[j]) 
        
        return max(lss)  

    
if __name__=="__main__":
    nums = [4,10,4,3,8,9]
    solution = Solution()
    value = solution.longestSubsequence(nums)
    print(f"max subsequeunce is {value}")