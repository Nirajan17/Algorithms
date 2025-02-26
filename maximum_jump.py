# jumping to the last position of the array according to the current element(max jump allowed)
from time_wrapper import time_it

# class Solution:
#     @time_it
#     def canJump(self,nums):
#         n = len(nums)
        
#         dp = [False] * n
#         dp[n-1] = True

#         for i in range(len(nums)-2, -1, -1):
#             j = nums[i]
#             k=i
#             while j:
#                 dp[i] = dp[i] or dp[k+1]
#                 k += 1
#                 j -= 1
#                 if dp[i] == True:
#                     break
#         return dp[0]
    
# if __name__=="__main__":
#     nums = [0,0,16109,19143,15489,5642,4855,3147,19141,13205,2804,4379,13304,18581,15167,4365,3953,5581,15789,1578974,81,164,17730,4578,8776,8109]
#     s = Solution()
#     print(s.canJump(nums))


class Solution:
    def canJump(self, nums):
        n = len(nums)
        goal = n-1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= goal-i:
                goal = i
        
        return True if goal == 0 else False
            
if __name__=="__main__":
    nums = [2,0,1,1,4]
    s = Solution()
    print(s.canJump(nums))