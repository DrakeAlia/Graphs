# graph1.py with recursive

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
​
class Graph:
    def __init__(self):
        self.vertices = {}
​
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
​
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")
​
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
​
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
​
        # Add starting vertex ID
        q.enqueue(starting_vertex_id)
​
        # Create set for visited verts
        visited = set()
​
        # While queue is not empty
        while q.size() > 0:
​
            # Dequeue a vert
            v = q.dequeue()
​
            # If not visited
            if v not in visited:
​
                # Visit it!
                print(v)
​
                # Mark as visited
                visited.add(v)
​
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
​
    def bfs(self, starting_vertex_id, target_vertex_id):
        pass
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                  # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHOR TO THE BACK
​
    def dft_recursive(self, starting_vertex_id, visited=None):
​
        if visited is None:
            visited = set()
​
        visited.add(starting_vertex_id)
​
        print(starting_vertex_id)
​
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
​
    def dfs_recursive(self, starting_vert, ending_vert, visited=None, path=None):
        if visited is None:
            visited = set()
​
        if path is None:
            path = []
​
        visited.add(starting_vert)
​
        path = path + [starting_vert]  # subtly makes a copy of the path
​
        """
        # Line above equivalent to:
​
        path = list(path)  # make a copy
        path.append(starting_vert)
        """
​
        if starting_vert == ending_vert:
            return path
​
        for neighbor in self.get_neighbors(starting_vert):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, ending_vert, visited, path)
                if new_path is not None:
                    return new_path
​
        return None
​
​
g = Graph()
​
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
​
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(3, 6)
g.add_edge(6, 5)
g.add_edge(5, 4)
​
print(g.vertices)
​
#g.bft(3)
#g.dft_recursive(1)
print(g.dfs_recursive(1, 6))
​
​
​
​
"""
Traverse(BST):
    visit current
    Traverse(left)
    Traverse(right)
​
​
Traverse(graph):
    visit current
    For all neighbors:
        Traverse(neighbor)
"""


#  wordsladders.py

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
​
​
# Read words in from the file, add to set of words
​
word_set = set()
​
with open("words.txt") as f:
    for word in f:  # for each line of the file
        word_set.add(word.strip().lower())
​
import string
​
words_by_length = {}
​
for w in word_set:
    l = len(w)
​
    if l not in words_by_length:
        words_by_length[l] = []
​
    words_by_length[l].append(w)
​
​
def get_neighbors_1(word):
    neighbors = []
​
    word_letters = list(word)
​
    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase): # ['a', 'b', 'c' ...
​
            # Make a copy of the word
            temp_word = list(word_letters)
​
            # substitute the letter into the word copy
            temp_word[i] = letter
​
            # Make it string
            temp_word_str = "".join(temp_word)
​
            # If it's a real word, add it to the return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)
​
    return neighbors
​
def get_neighbors_2(word):
​
    def word_diff_by_1(w1, w2):
        if len(w1) != len(w2):
            return False
​
        diff_count = 0
​
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff_count += 1
​
        return diff_count == 1
​
    neighbors = []
​
    # If they differ by one letter, add to return set
    #for word2 in word_set:
    for word2 in words_by_length[len(word)]:
        if word_diff_by_1(word, word2):
            neighbors.append(word2)
​
    return neighbors
​
get_neighbors = get_neighbors_2
​
def find_word_ladder(begin_word, end_word):  # BFS
    visited = set()
​
    q = Queue()
​
    q.enqueue([begin_word])
​
    while q.size() > 0:
        path = q.dequeue()
​
        v = path[-1]
​
        if v not in visited:
            visited.add(v)
​
            if v == end_word:
                return path
    
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
​
    # If we got here, didn't find a path
    return None
​
​
print(find_word_ladder("sail", "boat"))
