from util import Stack, Queue

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    # Create the queue, most recent parent and the visited set
    q = Queue()
    visited = set()
    most_recent = []

    # Check if the node has no ancestors
    if has_parents(ancestors,starting_node) is False:
        return -1

    # Add the starting Node
    q.enqueue(starting_node)

    while q.size() > 0:
        # Get the first in line
        v = q.dequeue()
        print(f"Current Node {v}")
        # Check if it has been visited or not
        # If so, add it to the visited set
        if v not in visited:
            visited.add(v)
            # Check if the node has parents
            # If true
            if has_parents(ancestors,v):
                # Clear the most recent parents list
                most_recent.clear()
                # Enqueue the parents and add the parents to the most recent
                # Parents list
                for parent,child in ancestors:
                    if child == v:
                        q.enqueue(parent)
                        print(f"queueing {parent} as the parents of {v}")
                        # reset the most recent parents
                        most_recent.append(parent)

                print()
            else:
                print(f"{v} has no parents\n")
    # Return the smaller of the two parents
    return min(most_recent)

def has_parents(ancestors,node):
    children = set()
    for parent, child in ancestors:
        children.add(child)
    if node in children:
        return True
    else:
        return False      

ancestor = earliest_ancestor(test_ancestors,6)           
print(f"The earliest ancestor to the input is {ancestor}")


#  First Attempt

#     class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         self.vertices[v1].add(v2)



# def earliest_ancestor(ancestors, starting_node):
#     ## using the graph class
#     graph = Graph()

#     ## build a dictionary of all the connections
#     for connection in ancestors:
#         graph.add_vertex(connection[1])

#     for connection in ancestors:
#         graph.add_edge(connection[1], connection[0])

#     ## empty set to store the paths (set of lists)
#     paths = []
#     visited_paths = []

#     visited_paths.append([starting_node])

#     while len(visited_paths) > 0:
#         current_path = visited_paths.pop(0)
#         starting_node = current_path[-1]

#         if starting_node in graph.vertices:
#             for parent in graph.vertices[starting_node]:
#                 new_path = current_path.copy()
#                 new_path.append(parent)
#                 paths.append(new_path)
#                 visited_paths.append(new_path)

#     if len(paths) == 0:
#         return -1    
#     longest = max([len(i) for i in paths])
#     plist = []
#     for path in paths:
#         if len(path) == longest:
#             plist.append(path)

#     oldest = []
#     for path in plist:
#         oldest.append(path[-1])

#     return min(oldest)