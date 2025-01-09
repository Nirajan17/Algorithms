# calculating the time and space complexity of sum of array elements

array = (1, 2, 3, 4, 5)

sum=0
def sum_array(array): 
    global sum
    for i in range(len(array)):
        sum += array[i]
    return sum

print(sum_array(array))


# time complexity = 2n+3