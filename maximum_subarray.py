# given an array find the subarray with the largest sum.

class Solution:
    def maxSubarray(self, nums):
        max_array = []
        for i in range(len(nums)):
            sum = 0
            sum_array = []
            for j in range(i,len(nums)):
                sum += nums[j]
                sum_array.append(sum)
            max_array.append(max(sum_array))
        max_number = max(max_array)
        return max_number