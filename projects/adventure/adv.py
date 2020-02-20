from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

traversal_graph = {}

queue = Queue()
queue.enqueue([world.starting_room])

while queue.size() > 0:
    v = queue.dequeue()
    curr_room = v[-1]
    
    if curr_room.id not in traversal_graph.keys():
        traversal_graph[curr_room.id] = {}
        path = []
        for item in v:
            path.append(item)

        if 'n' in curr_room.get_exits():
            traversal_graph[curr_room.id]['n']= '?'
            queue.enqueue(path + [curr_room.n_to])
        if 's' in curr_room.get_exits():
            traversal_graph[curr_room.id]['s']= '?'
            queue.enqueue(path + [curr_room.s_to])
        if 'w' in curr_room.get_exits():
            traversal_graph[curr_room.id]['w']= '?'
            queue.enqueue(path + [curr_room.w_to])
        if 'e' in curr_room.get_exits():
            traversal_graph[curr_room.id]['e']= '?'
            queue.enqueue(path + [curr_room.e_to])
    
print(traversal_graph)
            
# print("HEY NOW", traversal_graph)
# print("PATH", path)

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
