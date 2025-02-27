# let's try different ways to represent graph

edge_list = [[1,2], [2,3], [3,4], [2,4]]

print(edge_list)

# changing the edge_list to adjacency matrix

adj_matrix = [[0 for _ in range(4)] for _ in range(4)]

print(adj_matrix)

for u, v in edge_list:
    # print(u, v)
    adj_matrix[u-1][v-1] = 1

# print(adj_matrix)

# changing into adjanceny list

adj_list = {}

for u,v in edge_list:
    adj_list[u] = [u,v] # this approach is wrong here because the list will be overwritten but instead we should append the value of v every time to that list, this is wrong!!, that is why defaultdict is used.

print(adj_list)

from collections import defaultdict

d = defaultdict(list)

for u, v in edge_list:
    d[u].append(v)

print(d)


