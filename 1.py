a=5
b=7
print(a,b)
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

swapped_values = swap(a,b)
print(swapped_values)
print(swap(a,b))