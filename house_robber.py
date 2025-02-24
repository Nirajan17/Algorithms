# given an integer array, find the maximum amount you can get from that array(not including the adjacent elements)

class Solution:
    def houseRobber(self, nums):
        dp = [1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        
        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2], max(dp[i-1], nums[i]))
        
        return dp[len(nums)-1]

if __name__=="__main__":
    nums = [2,1,1,2]
    s = Solution()
    value = s.houseRobber(nums)
    print(value)
