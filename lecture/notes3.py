# populate_graph()

def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
​
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
​
        Creates that number of users and a randomly distributed friendships
        between those users.
​
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()
​
        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")
​
        # Create friendships
        possible_friendships = []
        
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
​
        random.shuffle(possible_friendships)
​
        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])


    # islands.py

# Write a function that takes a 2D binary array and returns the number of 1
# islands. An island consists of 1s that are connected to the north, south, east
# or west. For example:
​
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
​
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
​
islands2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
​
def island_counter(islands):
    # Create a way to keep track of visited nodes
    visited = []
    for _ in range(len(islands)):
        new_row = [False] * len(islands[0])
        visited.append(new_row)
​
    island_count = 0
​
    # Walk through each cell in the grid
​
    for row in range(len(islands)):
        for col in range(len(islands[0])):
            # If it's not visited
            if not visited[row][col]:
                # If it's a 1:
                if islands[row][col] == 1:
                    # Do a traversal
                    dft(row, col, islands, visited)
​
                    # increment the counter
                    island_count += 1
​
    return island_count
​
def dft(row, col, islands, visited):
    s = Stack()
​
    s.push( (row, col) )
​
    while s.size() > 0:
        v = s.pop()
        row, col = v
​
        if not visited[row][col]:
            visited[row][col] = True
​
            for neighbor in get_neighbors(row, col, islands):
                s.push(neighbor)
​
def get_neighbors(row, col, islands):
    neighbors = []
​
    # Check north
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))
​
    # Check south
    if row < len(islands) - 1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))
​
    # Check west
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))
​
    # Check east
    if col < len(islands[0]) - 1 and islands[row][col+1] == 1:
        neighbors.append((row, col+1))
​
    return neighbors
​
print(island_counter(islands2))


# Connected Components notes

# Connected Components
# --------------------
# A set of nodes that is connected to one another in some way.
# Graphs can have multiple sets of connected nodes that are disjoint.
# A set of connected nodes is called a "connected component".
# Counting connected components:
# Algorithm 1:
# While there are unvisited nodes:
#     Choose an unvisited node
#     Traverse from that node, marking each as visited
#     Increment connected component counter
# Algorithm 2:
# (Same as algorithm 1, but more like we might code it.)
# For each node in the graph:
#     If it's unvisited:
#         Traverse from that node, marking each as visited
#         Increment connected component counter
