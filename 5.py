# finding a duplicate number in a array

numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 10]

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             print(f"{numbers[i]} is a duplicate number in the list")
#             break


duplicate = []
print(type(duplicate))
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate.append(numbers[i])
            break

print(duplicate)