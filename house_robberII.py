# house robber second
# like house robber I but now the houses are circular

class Solution:
    def houseRobber(self, nums):
        
        def helper(houses):
            dp = [1] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[:2])
            
            for i in range(2,len(houses)):
                dp[i] = max(houses[i]+dp[i-2], max(dp[i-1], houses[i]))
            
            return dp[len(houses)-1]
        
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))
    
if __name__=="__main__":
    nums = [2,3,1]
    s = Solution()
    result = s.houseRobber(nums)
    print(result)
