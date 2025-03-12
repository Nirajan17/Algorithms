# finding the number of connected components in an undirected graph

# Input: n=5, edges =[[0,1], [1,2], [3,4]]
# here are 2 connected components 1. 0,1,2 and 2. 3,4

class Solution:
    def NumberOfConnectedComp(self, n, edges):
        adj_list = { i:[] for i in range(n)}

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # now let's implement the DFS
        visited = set()
        count = 0
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for nei in adj_list[n]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                count += 1
            dfs(i)
        return count
    


if __name__=="__main__":
    n=7
    edges =[[0,1], [1,2], [3,4], [5,6], [4,5]]

    s= Solution()
    print(s.NumberOfConnectedComp(n, edges))

