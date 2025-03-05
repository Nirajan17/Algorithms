# checking if the number is sum of numbers which are power of 3

# 12 = 3^1 + 3^2


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

print(powerThree(91))