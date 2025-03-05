# checking if the number is sum of numbers which are power of 3

# 12 = 3^1 + 3^2

# greedy approach
def powerThree(n):
    i = 0
    value = n
    used = set()
    while value > 0:

        while 3**i <= value:
            i += 1
        i -= 1
        if i in used:
            return False
        used.add(i)
        sub = 3**i
        value = value - sub
        i = 0

    return value == 0

print(powerThree(12))


# let's try ternary representation method

# if the number is continuously divided by 3 and the remainder donot contain "2", then it can be ....

def powersOfThree(num):
    while num > 0:
        if num%3 == 2:
            return False
        num //= 3
    return True