from time_wrapper import time_it

@time_it
def bubble_sort(elements):
    size = len(elements)

    for j in range(size-1):
        swapped = False
        for i in range(size-1-j):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
        if swapped == False:
            break
    return elements

if __name__=="__main__":
    elements = [23,67,12,90,23,56,78,122,7,349,457,5]
    sorted_elements = [i for i in range(100)]
    print(bubble_sort(elements))
    print(bubble_sort(sorted_elements))