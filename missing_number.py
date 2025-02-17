# finding a number missing in the array 

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_length = len(nums)
        for i in range(nums_length+1):
            if i not in nums:
                return i
            

# solution above is a bruteforce approach making it very inefficient
# it's time complexity is O(n^2)

# let's try optimal solution