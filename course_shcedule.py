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