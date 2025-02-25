# house robber second
# like house robber I but now the houses are circular

class Solution:
    def houseRobber(self, nums):
        if not nums:
                return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            dp = [1] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[:2])
            
            for i in range(2,len(houses)):
                dp[i] = max(houses[i]+dp[i-2], max(dp[i-1], houses[i]))
            
            return dp[len(houses)-1]
        
        return max(helper(nums[:len(nums)]), helper(nums[1:]))
    
if __name__=="__main__":
    nums = [1]
    s = Solution()
    result = s.houseRobber(nums)
    print(result)
