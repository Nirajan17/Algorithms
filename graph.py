
class Graph:
    def __init__(self,edges):
        self.edges = edges

        self.flight_routes = {}
        for start, end in self.edges:
            if start in self.flight_routes:
                self.flight_routes[start].append(end)
            else:
                self.flight_routes[start] = [end]

    def get_path(self, start, dest, path=[]):
        path = path + [start]

        if start == dest:
            return [path]
        
        if start not in self.flight_routes:
            return []
        
        paths = []
        for node in self.flight_routes[start]:
            if node not in path:
                new_path = self.get_path(node, dest, path)
                for item in new_path:
                    print(paths)
                    paths.append(item)

        return paths

if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Paris", "Newyork"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Newyork", "Toronto"),
    ]

    route_graph = Graph(routes)
    print("\n")
    print(route_graph.get_path("Mumbai", "Newyork"))
    print("\n")