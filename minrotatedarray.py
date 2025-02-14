# finding the minimum element in the rotated sorted array

# time complexity should be O(logn)

class Solution:
    def minRotated(self, nums):
        left, right = 0, len(nums)-1

        while(left < right):
            mid = (left+right) // 2
            if nums[mid] > nums[left]:
                right = mid-1
            else:
                left = mid
        return nums[right]