# given an array find the subarray with the largest sum.

# this approach below works for most of the test cases but not for all  .... ???
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
    

# this question can be done in O(n) time complexity as well 

# initialize two pointers left and right pointing intial element
# increase the right pointer and also calculate the sum
# if right pointer encoutners the positive value and the sum in the left is negative, update the left pointer to right
# repeat the process again

class Solution:
    def maxSubarray(self, nums):
        cur_sum = 0
        max_sum = nums[0]

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
        return max_sum