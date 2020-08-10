"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # Make a queue
        q = Queue()
        # Enqueue our starting node
        q.enqueue(starting_vertex)

        # Make a set to track if we've been here before
        visited = set()

        # While our queue isn't empty
        while q.size() > 0:
        ## Dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
        # If we haven't visited this node yet,
            if current_node not in visited:
        # Mark as visited
                visited.add(current_node)
                print(current_node)
                # print(f"Visited {current_node}")
        # Get its neighbors
                neighbors = self.get_neighbors(current_node)
        # For each of the neighbors,
                for neighbor in neighbors:
        # Add to queue
                    q.enqueue(neighbor)
        # visited = list(visited)
        # visited_string = ""
        # for node in visited:
        #     visited_string = visited_string + f"{node}\n"
        # print(visited_string[:-1])



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # Make a stack
        # Push on our starting node
        # Make a set to track if we've been here before
        # While our stack isn't empty
        # Pop off whatever's on top, this is current_node

        q = Stack()
        # Enqueue our starting node
        q.push(starting_vertex)

        # Make a set to track if we've been here before
        visited = set()

        # While our stack isn't empty
        while q.size() > 0:
        # pop whatever's at the front of our line, this is our current_node
            current_node = q.pop()
        # If we haven't visited this node yet,
            if current_node not in visited:
        # Mark as visited
                visited.add(current_node)
                print(current_node)
                # print(f"Visited {current_node}")
        # Get its neighbors
                neighbors = self.get_neighbors(current_node)
        # For each of the neighbors,
                for neighbor in neighbors:
        # Add to stack
                    q.push(neighbor)

        # visited_string = ""
        # for node in visited:
        #     visited_string = visited_string + f"{node}\n"
        # print(visited_string[:-1])


    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass 
        # q = Stack()
        # # base case - empty stack
        # if len(visisted) == 0:
        # move towards it  
        # call itself


        # If node hasn't been visited
        if starting_vertex not in visited:
            # Mark as visited
            visited.add(starting_vertex)
            print(starting_vertex)

            # For each of the node's neighbors
            for neighbor in self.vertices[starting_vertex]:
                # Recurse
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #  pass TODO
        # Instantiate an empty queue
        q = Queue()
        # Enqueue a path to the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to track visited nodes
        visited = set()

        # While queue not empty
        while q.size() > 0:
            # Dequeue the path
            path = q.dequeue()
            # Get the last vertex from the path
            node = path[-1]

            # If the node hasn't been visited
            if node not in visited:
                # Return the path if the node is our target
                if node == destination_vertex:
                    return path
                # Mark the node as visited
                visited.add(node)

                # Add a path to its neighbors to the back of the queue
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    # Copy the path
                    new_path = path.copy()
                    # Append the neighbor to the back
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    # def bfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing the shortest path from
    #     starting_vertex to destination_vertex in
    #     breath-first order.
    #     """
    #     # pass  # TODO
    #     # create an empty queue and enqueue A PATH to the starting vertex 
    #     q = Queue()
    #     q.enqueue([starting_vertex])
    #     # create a SET to store visited vertices
    #     visisted = set()

    #     # while the queue is not empty
    #     while q.size() > 0:
    #         # dequeue the first path (front or back?)
    #         current_path = q.dequeue()
    #         # Grab the last vertex from the PATH
    #         current_vertex = current_path[-1]

    #         # if that vertex has not been visited
    #         if current_vertex not in visisted:
    #             # check if it's the target
    #             if current_vertex == destination_vertex:
    #                 # if so, return path
    #                 return current_path
    #             # Mark as visited
    #             visisted.add(current_vertex)
    #             # add PATHs neighbors to the back of the queue
    #             neighbors = self.get_neighbors(current_vertex)
    #             for neighbor in neighbors:
    #                 # copy the PATH
    #                 current_path.append(neighbor)
    #                 print("Path:", current_path)
    #                 # append neighbor to the back
    #                 q.enqueue(current_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  TODO
        # Instantiate an empty queue
        q = Stack()
        # Enqueue a path to the starting vertex
        q.push([starting_vertex])
        # Create a set to track visited nodes
        visited = set()

        # While queue not empty
        while q.size() > 0:
            # Dequeue the path
            path = q.pop()
            # Get the last vertex from the path
            node = path[-1]

            # If the node hasn't been visited 
            if node not in visited:
                # Return the path if the node is our target
                if node == destination_vertex:
                    return path
                # Mark the node as visited
                visited.add(node)

                # Add a path to its neighbors to the back of the queue
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    # Copy the path
                    new_path = path.copy()
                    # Append the neighbor to the back
                    new_path.append(neighbor)
                    q.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO
        # Add the starting node in the visited set
        visited.add(starting_vertex)
        # Add the node in path
        path = path + [starting_vertex]
        # Base case
        # Is the node our target?
        if starting_vertex == destination_vertex:
            # If it is then return to the path
            return path
        # For each node's neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            # Is the node visited?
            if neighbor not in visited:
                # If no then recurse and get the new path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # Is the new path None?
                if new_path is not None:
                    # If its not none, return
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6)) 