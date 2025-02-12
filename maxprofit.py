# Leetcode problem :: best time to buy and sell stock

class Solution:
    def maxProfit(self, prices) -> int:
        # start two pointers left and right
        # update the pointer left to right if right is lesser than left
        # update the pointer right to further right if further right is lesser than current right
        # calculate left VS right and assign it to max_value
        # update max_value after updating the left or right pointer

        if not prices:
            return 0

        left = 0, right = 1, max_price = 0
        left_price = prices[left], right_price = prices[right]
        # diff = right_price-left_price
        # if diff > max_price:
        #     max_price = diff
        
        while(right < len(prices)):
            if prices[right] > prices[left]:  
                max_price = max(max_price, prices[right] - prices[left])
            else:  
                left = right  # Move left pointer to right (new buy day)
            right += 1  # Always move right pointer
        
        return max_price
        