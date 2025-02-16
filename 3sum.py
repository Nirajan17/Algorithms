# finding the distinct triplets that sums up to 0

# take the first element and apply the two sum approach in remaining array
# first sort the whole array
# take first element, start two pointers left and right in remaining element
# check the sum, if it's greater than 0, decrease the right pointer else, increase left pointer

class Solution:
    def findTriplets(self, nums):
        nums.sort()
        result = []
        
        for i, num in enumerate(nums):
            cur_element = num

            # to remove duplicates
            if i > 0 and cur_element == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                sum = cur_element + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result

