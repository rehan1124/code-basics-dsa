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
    print(g1)
