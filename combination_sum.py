# finding different combination of numbers that results to "target" value

# it is going to recursive, choose one element in the left tree and do NOT choose that particular element in right tree

class Solution:
    def combinationSum(self,candidates, target):
        result = []
        cur = []

        def recurSum(i):
            cur.append(candidates[i])
            total = sum(cur)

            if total == target:
                result.append(cur)
                return
            
            if i >= len(candidates) or total > target:
                return
            
            recurSum(i)
            cur.clear()
            recurSum(i+1)

        recurSum(0)
        return result
    

if __name__=="__main__":
    candidates = [2,3,6,7]
    target = 7
    s = Solution()
    value = s.combinationSum(candidates, target)
    print(value)
            
