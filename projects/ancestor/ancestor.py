class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    # pass
    # Use the graph class
    graph = Graph()

    # Build a dictionary of all the connections
    for connection in ancestors:
        graph.add_vertex(connection[1])

    for connection in ancestors:
        graph.add_edge(connection[1], connection[0])

    print("----------------------------------------------------")
    print(graph.vertices)
    # Search dictionary for all possible paths to the earliest ancestor

    # Empty set to store the paths
    paths = []
    visited_paths = []

    visited_paths.append([starting_node])
    # If starting node is stored as a key
    while len(visited_paths) > 0:
        current_path = visited_paths.pop(0)
        current_node = current_path[-1]
        print(current_node)
        if current_node in graph.vertices:
            for parent in graph.vertices[current_node]:
                # Append each value to copy of starting node as a new_path
                new_path = []
                new_path.append(current_path)
                # Append each new_path to the paths set() and end of the list
                new_path.append(parent)
                paths.append(new_path)
                visited_paths.append(new_path)
                # current_node = visited_paths.pop(0)[-1]
