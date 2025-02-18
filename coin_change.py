# you are given an integer array of coins having different denominations 
# using those coins, you have to make up to "amount" using fewest number of coins

class Solution:
    def coinChange(self, coins, amount):
        result = 0
        if amount in coins:
            return 1
        
        coins.sort()

        for i in range(len(coins)):
            result = amount // coins[len(coins)-1-i]
            num = result * coins[len(coins)-1-i]
            amount = amount - num
            if amount in coins:
                return result

