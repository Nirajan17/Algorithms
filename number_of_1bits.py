# program to find the hamming weight of a number

class Solution:
    def hammingWeight(self, n):
        n_bin = int(bin(n)[2:])
        count = 0 
        while n_bin:

            if n_bin%2 == 1:
                count += 1

            n_bin = n_bin/10
        return count