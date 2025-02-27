# cloning the graph and returning the new reference of a node 
# example of why we are doing this problem

# original_graph = {1:[2,3], 2:[3,4], 3:[1,4]}
# copied_graph = original_graph ,if we do this,changing the copied_graph will also bring change in former

"""
# Definition of a Node
class Node:
    def __init__(self, val=0, neighbours=None):
        self.val = val
        self.neighbours = neighbours
"""

class Solution:
    def cloneGraph(self, node):
        new_graph = {}

        for i,n in enumerate(node):
            if i in new_graph:
                continue 
            new_graph[i] = n
        return new_graph.values()
    

if __name__=="__main__":
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    s = Solution()
    print(s.cloneGraph(adjList))


# input are given in the form of adjacency list and values are nodes are assumed to be the indexes
# input is given always of first node for simplicity
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]