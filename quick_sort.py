# working of quick sort algorithm
# take a pivot element and start positioning it in right place

def swap(elements, start, end):
    elements[start], elements[end] = elements[end], elements[start]
    return elements
    
def partition(elements, start, end):
    pivot_index = start
    pivot_element = elements[pivot_index]

    while start < end:
        while(start < len(elements) and elements[start] <= pivot_element):
            start += 1

        while(elements[end] > pivot_element):
            end -= 1

        if start < end:
            swap(elements, start, end)
    swap(elements, end, pivot_index)
    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)
    return elements


if __name__=="__main__":
    elements = [
        [11,9,29,7,2,15,28],
        [34,56,78,90,23,12,45,67],
        [23,67,12,90,23,56,78,122,7,349,457,5],
        [5,7,9,10,2,4,6,8],
        [1,2,3,4,5,6,7,8,9],
        [12],
        [],
    ]
    
    for element in elements:
        print(quick_sort(element, 0, len(element)-1))

