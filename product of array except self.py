# product of the array elements except self

# you must write an algorithm with O(n) but without using division operation

class Solution:
    def arrayProd(self, nums):
        n = len(nums)
        output = [1] * n  # Initialize output with 1s

        # Prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Postfix products (update output in reverse)
        post = 1
        for i in range(n-1, -1, -1):
            output[i] *= post
            post *= nums[i]

        return output