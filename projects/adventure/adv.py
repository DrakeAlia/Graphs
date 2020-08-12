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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
