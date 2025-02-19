# finding the longest increasing subsequence in an array

class Solution:
    def longestSubsequence(self, nums):
        lss = [1]*(len(nums))
        # lss[len(nums)-1] = 1

        for i in range(len(nums)-2, -1, -1):
            j=i+1
            while j<len(nums) and nums[j]>nums[i]:
                if nums[j] > nums[i]:  # check if the array have greater values than of i'th
                    lss[i] = max(lss[i], 1 + max(lss[i+1:])) # not 1 + lss[i+1] but 1+max(lss>i)
                j += 1
        
        return max(lss)
    
if __name__=="__main__":
    nums = [4,10,4,3,8,9]
    solution = Solution()
    value = solution.longestSubsequence(nums)
    print(f"max subsequeunce is {value}")