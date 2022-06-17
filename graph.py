"""
### GRAPHS ###

--- Components ---
Nodes
Edges

--- Types of graph ---
Un-directed
Directed graphs
Weighted graph

"""


class Graph:
    def __init__(self, edge):
        # 'edge' is the list of pairs/tuples passed while creating object
        self.edge = edge
        # Empty dict to store start and end of paths
        self.graph_dict = {}

        # Unpack the tuple
        for i, j in self.edge:
            # Keep on adding start, end to graph_dict
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)

    def get_paths(self, source, destination, path=None):
        # Create a list to store multiple paths
        if path is None:
            path = []
        # Keep appending the paths as function is called
        # Use re-assignment for 'path'. Dont do 'path += [source]'(In-place addition).
        path = path + [source]

        # When source and destination city are same
        if source == destination:
            return [path]

        # When there is no flight between source and destination
        if source not in self.graph_dict:
            return []

        final_paths = []
        for city in self.graph_dict[source]:
            if city not in path:
                new_path = self.get_paths(city, destination, path)
                for p in new_path:
                    final_paths.append(p)

        return final_paths

    def __str__(self):
        return str(self.graph_dict)


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    g1 = Graph(routes)
    # --- Get all routes ---
    print(g1)  # {'Mumbai': ['Paris', 'Dubai'], 'Paris': ['Dubai', 'New York'],\
    # 'Dubai': ['New York'], 'New York': ['Toronto']}

    # --- Start and end is same ---
    start = "Mumbai"
    end = "New York"
    print(f"Paths between {start} and {end}: {g1.get_paths(start, end)}")
