# search the particular element in rotated sorted array

# start two pointers pointing left and the right most element
# find mid value and check if it is the one
# else check if the target is smaller than righmost element then search right array
# or else check the left array

class Solution:
    def searchElement(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:  
            mid = (left + right) // 2 

            if nums[mid] == target: 
                return mid

            # Determine which half is sorted
            if nums[mid] >= nums[left]:  
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1  
                else:
                    left = mid + 1 
            else:  
                if nums[mid] < target <= nums[right]:  
                    left = mid + 1  
                else:
                    right = mid - 1  

        return -1  
