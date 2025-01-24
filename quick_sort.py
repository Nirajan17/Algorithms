# working of quick sort algorithm
# take a pivot element and start positioning it in right place

def swap(elements, start, end):
    elements[start], elements[end] = elements[end], elements[start]
    return elements
    
def partition(elements, start, end):
    pivot_index = start
    pivot_element = elements[pivot_index]

    while start <= end:
        while(elements[start] < pivot_element):
            start += 1

        while(elements[end] > pivot_element):
            end -= 1

        if start < end:
            swap(elements, start, end)
        swap(elements, end, pivot_index)
    print(elements)
    return end

def quick_sort(elements, start, end):
    new_pi = partition(elements)

    while(start<end):
        # for left part
        l_start = 0
        l_end = new_pi - 1
        quick_sort(elements, new_pi, l_start, l_end)

        # for right part
        r_start = new_pi + 1
        r_end = len(elements) - 1
        quick_sort(elements, new_pi, r_start, r_end)


if __name__=="__main__":
    elements = [11,9,29,7,2,15,28]
    partition(elements, 0, len(elements)-1)
    # quick_sort(elements)
    # print(elements)
