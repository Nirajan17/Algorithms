# finding the longest consecutive sequence in unsorted array
# sorting the array and finding the sequence would be easier but it's TC is O(nlogn), we want O(n)


# def longSequence(nums):
#     if not nums:
#             return 0
    
#     nums_set = set(nums)
#     long_count = 0
#     visited = set()  
    
#     for n in nums:
#         if n-1 not in nums_set and n not in visited:
#             seq_count = 0
#             current = n

#             while current in nums_set:
#                 seq_count += 1
#                 visited.add(current)
#                 current += 1

#             long_count = max(long_count, seq_count)
    
#     return long_count


# nums = [0,3,7,2,5,8,4,6,0,1]
# print(longSequence(nums))


# let's code again

nums = [9,1,4,7,3,-1,0,5,8,-1,6]

def longestSequence(nums):
    nums_set = set(nums)
    seq_count = 1
    count = 1
    
    for n in nums_set: # remember to loop for members in set not list, if list repeated numbers are also looped and creates problem
        if n-1 not in nums_set:
            # which means start of the sequence like.. 0 don't have "0-1" in above example
            temp=n
            while temp+1 in nums_set:
                count += 1
                temp = temp+1
            seq_count = max(seq_count, count)
            count = 1

    return seq_count

print(longestSequence(nums))
                


