
# leetcode 2579 :: counting total number of colored cells after n minutes
# from collections import deque

# def solution(n):
#     result = 1

#     for i in range(n):
#         result += 4*i

#     return result


# print(solution(4))


# linear time solution, using formula

def solution(n):
    result = 1+4*((n-1)*(n)//2)
    return result

print(solution(4))