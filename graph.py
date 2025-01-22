
class Graph:
    def __init__(self,edges):
        self.edges = edges

        self.flight_routes = {}
        for start, end in self.edges:
            if start in self.flight_routes:
                self.flight_routes[start].append(end)
            else:
                self.flight_routes[start] = [end]
        # print(self.flight_routes)

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
                    paths.append(item)

        return paths
    
    # function below also works as a shortest path but it is not computationally efficient

    # def get_shortest_path(self, start, end):
    #     routes = self.get_path(start, end)
    #     shortest_route = []
    #     for i in range(len(routes)):
    #         if(len(routes[i])<=len(routes[i-1])):
    #            shortest_route.append(routes[i])

    #     return shortest_route

    def get_shortest_path(self, start, dest, path=[]):
        path = path + [start]

        if start == dest:
            return path
        
        if start not in self.flight_routes:
            return None

        short_path = None
        for node in self.flight_routes[start]:
            if node not in path:
                sp = self.get_shortest_path(node, dest, path)
                if short_path is None or len(sp) < len(short_path):
                    short_path = sp
        return short_path

if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Paris", "Newyork"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Dubai", "Newyork"),
        ("Newyork", "Toronto"),
    ]

    route_graph = Graph(routes)
    start = "Paris"
    end = "Toronto"
    shortest_path = route_graph.get_shortest_path(start, end)
    print(f"Shortest routes from {start} to {end} are \n{shortest_path}")