# finding the flow of water in a matrix

# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(i, j, visited):
            visited.add((i, j))
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if (0 <= ni < m and 0 <= nj < n and 
                    (ni, nj) not in visited and 
                    heights[ni][nj] >= heights[i][j]):
                    dfs(ni, nj, visited)
        
        # Pacific borders: top and left edges
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)
            
        # Atlantic borders: bottom and right edges
        for i in range(m):
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(m-1, j, atlantic)
        
        # Return cells that can reach both oceans
        return list(pacific & atlantic)
    


if __name__=="__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    s = Solution()
    print(s.pacificAtlantic(heights))

