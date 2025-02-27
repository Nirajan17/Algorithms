# cloning or copying a graph
# direct assignment of variables creates reference to that object so changing one will reflect in assigned varibale, so we need to make the copy 

class Node(object):
    def __init__(self, val=None, neighbours=None):
        self.val = val
        self.neighbours = neighbours
    
    def display(self):
        print(f"Node's value is {self.val}")
        print(f"It's neighbours are {self.neighbours}")


adjList = [[2,4],[1,3],[2,4],[1,3]]

n=[[] for i in range(len(adjList)-1)]
for i in range(len(adjList)-1):
    n[i] = Node(i, adjList[i])

print(n[1].display())