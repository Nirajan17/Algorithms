# checking if the number is sum of numbers which are power of 3

# 12 = 3^1 + 3^2


def powerThree(n):
    value = n - 1
    i = 1
    
    while value > 0:
        value = n - 3**i
        if value == powerThree():
            return True
        i += 1
    return False

print(powerThree(21))