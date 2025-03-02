# return true if you can finish certain number of courses based on the prerequisites

class Solution:
    def courseSchedule(self, numcourses, prerequities):
        pre_map = { i:[] for i in range(numcourses) }

        for node, pre in prerequities:
            pre_map[node].append(pre)

        visit_set = set()

        def dfs(node_val):
            if node_val in visit_set:
                return False
            if pre_map[node_val] == []:
                return True
            
            visit_set.add(node_val)
            for crs in pre_map[node_val]:
                if not dfs(crs):
                    return False
            visit_set.remove(node_val)
            pre_map[node_val] = []
            return True
        
        for crs in range(numcourses):
            if not dfs(crs): return False
        return True

if __name__=="__main__":
    s = Solution()
    print(s.courseSchedule(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))







# let's try coding this solution again

class Solution:
    def courseSchedule(self, numcourses, prerequisities):
        pre_map = { i:[] for i in range(numcourses)}

        for v1, v2 in prerequisities:
            pre_map[v1].append(v2)

        visit_set = set()
        def dfs(course):
            if course in visit_set:
                return False
            if pre_map[course] == []:
                return True
            
            visit_set.add(course)
            for pre in prerequisities:
                if not dfs(pre): return False

            visit_set.remove(course)
            pre_map[course] = []
            return True
        
        for course in numcourses:
            if not dfs(course): return False
        return True