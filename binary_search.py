
def binary_search(values, value):
    left_index = 0
    right_index = len(values) - 1

    while(left_index <= right_index):
        mid_index = (left_index + right_index) // 2
        if values[mid_index] == value:
            return mid_index
        elif(values[mid_index] < value):
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def linear_search(values, value):
    for i,v in enumerate(values):
        if v == value:
            return i
    return False
        

if __name__=="__main__":
    values = [12,19,24,36,100,129]
    # print(linear_search(values, 36))
    print(binary_search(values, 12))
    print(binary_search(values, 129))
    print(binary_search(values, 100))