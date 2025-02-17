# counting bits of numbers up to given n

class Solution:
    def countOnes(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
    
    def countingBits(self, n):
        result = []
        for i in range(n+1):
            no_ones = self.countOnes(i)
            result.append(no_ones)
        return result
    
    # done in a single function
    def countBits(self,n):
        result = []
        for i in range(n+1):
            count = 0
            while i:
                i &= i-1
                count += 1
                result.append(count)
        return result