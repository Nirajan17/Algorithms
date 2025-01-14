# knowing the index of a particular value in an array

numbers = [2,3,4,5,4]

for i in range(len(numbers)):
    if numbers[i] == 4:
        print(f"the number is in {i}th place.")
        