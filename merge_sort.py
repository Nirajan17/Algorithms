# implementing the merge sort

# divide the given array from the middle until it the array is single value
# initialize pointers on each array and compare the value

def merge_sorted_lists(l1,l2):

    i = 0 # pointing the left list's first element
    j = 0 # pointing the right list's first element

    sorted_list = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            sorted_list.append(l1[i])
            i += 1
        else:
            sorted_list.append(l2[j])
            j += 1

    while i < len(l1):
            sorted_list.append(l1[i])
            i += 1
            
    while j < len(l2):
            sorted_list.append(l2[j])
            j += 1

    return sorted_list

def merge_sort(numbers):
    if len(numbers) <=1:
         return numbers
    mid_index = len(numbers) // 2
    left = numbers[:mid_index]
    right = numbers[mid_index:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge_sorted_lists(left_list, right_list)
     


if __name__=="__main__":
    numbers = [23,56,34,9,78,1,2,45,78,9]
    l2 = [1,2,3,4,5,67]
    # print(merge_sorted_lists(numbers,l2))
    print(merge_sort(numbers))