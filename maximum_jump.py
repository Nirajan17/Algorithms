# jumping to the last position of the array according to the current element(max jump allowed)

class Solution:
    def canJump(self,nums):
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(len(nums)-2, -1, -1):
            j = nums[i]
            k=i
            while j:
                dp[i] = dp[i] or dp[k+1]
                k += 1
                j -= 1
        return dp[0]

if __name__=="__main__":
    s = Solution()
    nums = [2,3,1,0,4]
    print(s.canJump(nums))