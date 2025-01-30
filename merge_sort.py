# implementing the merge sort

# divide the given array from the middle until it the array is single value
# initialize pointers on each array and compare the value

def merge_sort(numbers):
    mid_index = len(numbers) // 2
    left_list = numbers[:mid_index]
    right_list = numbers[mid_index:]

    i = 0 # pointing the left list's first element
    j = 0 # pointing the right list's first element

    sorted_list = []

    while left_list[i] < right_list[j] and i < len(left_list)-1:
        sorted_list.append(left_list[i])
        i += 1

    while right_list[j] < left_list[i] and j < len(right_list)-1:
        sorted_list.append(right_list[j])
        j += 1

    return sorted_list


if __name__=="__main__":
    numbers = [23,56,34,9,78,1,2,45,78,9]
    print(merge_sort(numbers))