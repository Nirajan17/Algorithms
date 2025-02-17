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
    
# the above code runs for 32 times if the a single number is represented using 32 bits
# but it can be done in way lesser

# basically do n&(n-1) until it reaches 0

class Solution:
    def hammingWeight(self, n):
        n = int(bin(n)[2:])
        count = 0
        while n&(n-1):
            count += 1
            n= n&(n-1)
        return count