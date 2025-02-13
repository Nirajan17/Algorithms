# finding the maximum product subarray

class Solution:
    def prodSubarray(self, nums):
        if not nums:
            return 0
        
        result = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            temp_max = n*cur_max
            cur_max = max(n*cur_min, n*cur_max, n)
            cur_min = min(n*cur_min, temp_max, n)
            result = max(result, cur_max)
        return result