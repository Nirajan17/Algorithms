
def swap(elements, first, second):
    elements[first], elements[second] = elements[second], elements[first]
    
# the sorting technique below is not the exact insertion sort or selection sort but is a mixture of both. This sorting is not efficient because the swap function is called many times leading to inefficiency.

def insertion_sort(elements):
    for i in range(len(elements)-1):
        for j in range(i+1, len(elements)):
            if elements[j] < elements[i]:
                swap(elements, j, i)

    return elements

if __name__=="__main__":
    elements = [1,45,67,34,2,89,450,4,56]
    print(insertion_sort(elements))