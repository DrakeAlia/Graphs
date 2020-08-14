# You are provided with a pre-generated graph consisting of 500 rooms. 
# You are responsible for filling traversal_path with directions that, when walked in order, will visit every room on the map at least once.
# Open adv.py. There are four parts to the provided code:

# World generation code. Do not modify this!
# An incomplete list of directions. Your task is to fill this with valid traversal directions.
# Test code. Run the tests by typing python3 adv.py in your terminal.
# REPL code. You can uncomment this and run python3 adv.py to walk around the map.
# You may find the commands player.current_room.id, player.current_room.get_exits() and player.travel(direction) useful.

# To solve this path, you'll want to construct your own traversal graph. You start in room 0, which contains exits ['n', 's', 'w', 'e'].
#  Your starting graph should look something like this:
# {
#   0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
# }
# Try moving south and you will find yourself in room 5 which contains exits ['n', 's', 'e']. You can now fill in some entries in your graph:
# {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# }
# You know you are done when you have exactly 500 entries (0-499) in your graph and no '?' in the adjacency dictionaries. 
# To do this, you will need to write a traversal algorithm that logs the path into traversal_path as it walks.


from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

## Create a stack class
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Get the reverse direction of the direction just traveled
reverse_dir = {"n": "s", "s": "n", "e": "w", "w": "e"}
# Add the reverse direction to reverse course
reverse_path = []

# Dictionary of exits
rooms = {}

# Add the id of the room as an exit
rooms[0] = player.current_room.get_exits()

# While the rooms visited is less than the total number rooms
while len(rooms) < len(room_graph) - 1:
    # If the room hasn't been visited
    if player.current_room.id not in rooms:
        # Add the exits for current room to rooms
        rooms[player.current_room.id] = player.current_room.get_exits()
        # Store last direction traveled in reverse path
        last_dir = reverse_path[-1]
        # Remove last exit from exits dictionary
        rooms[player.current_room.id].remove(last_dir)

    # While there are no rooms to explore.
    while len(rooms[player.current_room.id]) < 1:
        # Remove the last direction from reverse_path
        reverse = reverse_path.pop()
        # Add the reverse direction to traversal_path
        traversal_path.append(reverse)
        # Next travel in that direction
        player.travel(reverse)

    # Travel to first available exit in the current room
    exit_dir = rooms[player.current_room.id].pop(0)
    # Next add to the traversal path
    traversal_path.append(exit_dir)
    # Add the reverse direction to reverse path
    reverse_path.append(reverse_dir[exit_dir])
    # Next travel to the next room
    player.travel(exit_dir)

# print(rooms)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")