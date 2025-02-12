# check if the array contains a number more than once

# one approach is to bruteforce but it night be done woth hashmap, let's try

# create a hashmap and check whether the element scanned is in the map or not?
# if yes, return TRUE else, return FALSE

class Solution:
    def containsDuplicate(self, nums):
        dup_map = {}
        is_twice = False
        for i in range(0,len(nums)):
            if nums[i] in dup_map:
                is_twice = True
            else:
                dup_map[nums[i]] = i