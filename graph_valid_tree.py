# checking if the given graph is a valid tree

# a graph is a tree iff :: 
    # all of it's nodes are connected
    # graph doesn't have a cycle

# given :: n nodes and list of undirected edges

# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

def graphValidTree(n: int, edges: list[list[int]]) -> bool:
    # let's first make the adjacency list of graph
    adj_list = { i: set() for i in range(n) }
    for n1, n2 in edges:
        adj_list[n1].add(n2)
        adj_list[n2].add(n1)  # to represent that it is a undirected graph

    # let's check for a valid tree
    visit = set()
    def dfs(node, prev):
        if node in visit:
            return False
        visit.add(node)
        for nei in adj_list[node]:
            if nei != prev:
                if not dfs(nei, node):
                    return False
        return True

    return True if (dfs(0, -1) and (n == len(visit))) else False

# edges = [[0, 1], [0, 2], [0, 3], [1, 4]
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# edges = [[0,1], [0,2], [1,2]]

print(graphValidTree(5, edges))