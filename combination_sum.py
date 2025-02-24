# finding different combination of numbers that results to "target" value

# it is going to recursive, choose one element in the left tree and do NOT choose that particular element in right tree

class Solution:
    def combinationSum(self,candidates, target):
        result = []

        def recurSum(i, cur, total):
            if total == target:
                # we need to specifically append the copy of the list here because if we append cur directly, reference to cur will be appended which means if cur is changed later in recursive calls the appended cur value will also get changed, ie mutated.
                result.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            recurSum(i, cur, total+candidates[i])
            cur.pop()
            recurSum(i+1, cur, total)

        recurSum(0,[],0)
        return result
    
if __name__=="__main__":
    candidates = [2,3,6,7]
    target = 7
    s = Solution()
    value = s.combinationSum(candidates, target)
    print(value)
            
