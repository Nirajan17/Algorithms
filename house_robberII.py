# house robber second
# like house robber I but now the houses are circular

class Solution:
    def houseRobber(self, nums):
        result = []

        for i in range(len(nums)):
            if i >= len(nums):
                i=0
            total = nums[i] + nums[i+2]
            result.append(total)
        return max(result)
    
if __name__=="__main__":
    nums = [1,2,3,1]
    s = Solution()
    result = s.houseRobber(nums)
    print(result)
