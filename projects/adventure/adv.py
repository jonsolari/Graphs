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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

traversal_path = []

def traverse():
    
    visited = {
      0: {'w': '?', 's': '?', 'n': '?', 'e': '?' }
    }

    stax = Stack()

    prev_room = 0

    direction_traveled = ''
    
    stax.push(0)

    while stax.size() > 0:
        curr_room = stax.pop()
        mark_visiting(player.current_room.id, prev_room, visited, direction_traveled)
        
        if '?' in visited[curr_room].values():
        
            for key, value in visited[curr_room].items():
                if value == '?':
                    player.travel(key)
                    stax.push(player.current_room.id)
                    direction_traveled = key
                    traversal_path.append(direction_traveled)
                    prev_room = curr_room
                    break
        else:
            if bfs(curr_room, visited) is None:
                break
            
            path = bfs(curr_room, visited)
            new_traverse = []
            
            for index, room in enumerate(path):
                if index < len(path) - 1 and path[index + 1] in visited[room].values():
                    for key, value in visited[room].items():
                        if value == path[index + 1]:
                            new_traverse.append(key)
            
            for move in new_traverse:
                prev_room = player.current_room.id
                player.travel(move)
                direction_traveled = move
                traversal_path.append(move)
            if '?' in visited[player.current_room.id].values():
                stax.push(player.current_room.id)



def mark_visiting(current_room, prev_room, visited, direction_traveled):
    
    if current_room not in visited:
        
        exits_array = player.current_room.get_exits()
        exits = {}

        for direction in exits_array:
            exits[direction] = '?'
        if direction_traveled == 's':
            exits['n'] = prev_room
        elif direction_traveled == 'n':
            exits['s'] = prev_room
        elif direction_traveled == 'e':
            exits['w'] = prev_room
        elif direction_traveled == 'w':
            exits['e'] = prev_room
        
        visited[current_room] = exits
        visited[prev_room][direction_traveled] = current_room
        

    else:
        if direction_traveled == 's':
            visited[current_room]['n'] = prev_room
        elif direction_traveled == 'n':
            visited[current_room]['s'] = prev_room
        elif direction_traveled == 'e':
            visited[current_room]['w'] = prev_room
        elif direction_traveled == 'w':
            visited[current_room]['e'] = prev_room

def bfs(starting_vertex, visited):
    
    queue = Queue()
    queue.enqueue([starting_vertex])
    
    visited_rooms = set()
    
    while queue.size() > 0:
        
        path = queue.dequeue()
        
        v = path[-1]
        if v not in visited_rooms:
            if '?' in visited[v].values():
                return path
            visited_rooms.add(v)
            
            for key, value in visited[v].items():
                path_copy = path.copy()
                path_copy.append(value)
                queue.enqueue(path_copy)

traverse()



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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
