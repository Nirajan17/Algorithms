
from time_wrapper import time_it

def swap(elements, first, second):
    elements[first], elements[second] = elements[second], elements[first]
    
# the sorting technique below is not the exact insertion sort or selection sort but is a mixture of both. This sorting is not efficient because the swap function is called many times leading to inefficiency.

@time_it
def insertion_sort1(elements):
    for i in range(len(elements)-1):
        for j in range(i+1, len(elements)):
            if elements[j] < elements[i]:
                swap(elements, j, i)

    return elements

@time_it
def insertion_sort(elements):
    for i in range(1, len(elements)):
        current = elements[i]
        j = i-1
        while j>=0 and elements[j] > current:
            elements[j+1] = elements[j]
            j -= 1
            elements[j+1] = current
    return elements

if __name__=="__main__":
    elements = [1,45,67,34,2,89,450,4,56]
    print(insertion_sort1(elements))
    print(insertion_sort(elements))

    # just check the time taken by both functions for sorting.