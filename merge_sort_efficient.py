
def merge_sorted_lists(l1, l2, numbers):

    i = 0 # pointing the left list's first element
    j = 0 # pointing the right list's first element
    k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            numbers[k] = l1[i]
            i += 1
        else:
            numbers[k] = l2[j]
            j += 1
        k += 1

    while i < len(l1):
            numbers[k] = l1[i]
            i += 1
            k += 1
            
    while j < len(l2):
            numbers[k] = l2[j]
            j += 1
            k += 1

def merge_sort(numbers):
    if len(numbers) <=1:
         return numbers
    mid_index = len(numbers) // 2
    left = numbers[:mid_index]
    right = numbers[mid_index:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_lists(left, right, numbers)
     

if __name__=="__main__":
    numbers = [
         [23,56,34,9,78,1,2,45,78,9],
            [1,2,3,4,5,67],
            [1,2,3,4,5,67],
            [32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],
            [],
            [1],
    ]
    
    for number in numbers:
         merge_sort(number)
         print(number)