# cloning or copying a graph
# direct assignment of variables creates reference to that object so changing one will reflect in assigned varibale, so we need to make the copy 

class Node(object):
    def __init__(self, val=None, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def display(self):
        print(f"Node's value is {self.val}")
        print(f"It's neighbors are {[neighbor.val for neighbor in self.neighbors]}")



class Solution(object):
    def cloneGraph(self, node):
        hash_map = {}

        def dfs(n):
            if n in hash_map:
                return hash_map[n]
            
            copy_n = Node(n.val)
            hash_map[n] = copy_n

            for ng in n.neighbors:
                copy_n.neighbors.append(dfs(ng))

            return copy_n
        
        return dfs(node) if node else None
    


def graphBuilder(adj_list):
    nodes = [Node(i+1)  for i in range(len(adj_list))]

    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[nei-1] for nei in neighbors]

    return nodes

if __name__=="__main__":
    adj_list = [[2,4],[1,3],[2,4],[1,3]]

    nodes = graphBuilder(adj_list)

    s = Solution()

    cloned_node = s.cloneGraph(nodes[1])
    cloned_node.display()