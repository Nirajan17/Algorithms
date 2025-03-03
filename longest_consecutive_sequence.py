# finding the longest consecutive sequence in unsorted array
# sorting the array and finding the sequence would be easier but it's TC is O(nlogn), we want O(n)


def longSequence(nums):
    nums_set = set(nums)
    long_count = 0
    for n in nums:
        seq_count = 1
        if n-1 in nums_set:
            while n-1 in nums_set:  # here the time to peek in a set is O(1)
                seq_count += 1
                n = n-1
        if seq_count > long_count:
            long_count = seq_count

    return long_count


nums = [0,3,7,2,5,8,4,6,0,1]
print(longSequence(nums))
