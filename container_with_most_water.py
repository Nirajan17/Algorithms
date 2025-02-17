# finding the container which can hold most water

# height is given as array elemets, and breadth is the index

# first approach is bruteforce

# class Solution:
#     def mostWater(self, nums):
#         max_area = []
#         for i, num_left in enumerate(nums):
#             cur_area = 1
#             for j, num_right in enumerate(nums):
#                 if i > 0 and j > 0:
#                     cur_area_calc = min(num_left, num_right) * (j-i)
#                     if cur_area_calc > cur_area:
#                         cur_area = cur_area_calc
#             max_area.append(cur_area)

#         return max(max_area)


# below is the optimal solution

# initialize left and right pointer to leftmost and rightmost value
# check if the area is greater than the previous value 
# increase or decrease left or right pointer by checking which one is smaller



class Solution:
    def most_water(slef, nums):
        result = 0
        left, right = 0, len(nums)-1

        while left < right:
            result = max(result, (right-left) * min(nums[left], nums[right]))
            if nums[left] > nums[right]:
                right -= 1
            else:
                left += 1

        return result