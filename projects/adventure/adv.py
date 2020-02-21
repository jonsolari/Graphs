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


# THIS PART, AT LEAST, WORKS     
#  VVVVVVVVVVVVVVVVVVVVVVVV

graphq = Queue()
graphq.enqueue([world.starting_room])
traversal_graph = {}

while graphq.size() > 0:
    v = graphq.dequeue()
    curr_room = v[-1]

    # fill out traversal graph with '?'s
    if curr_room.id not in traversal_graph.keys():
        traversal_graph[curr_room.id] = {}
        path = []
        
        if 'n' in curr_room.get_exits():
            traversal_graph[curr_room.id]['n']= '?'
            graphq.enqueue(path + [curr_room.n_to])
        
        if 's' in curr_room.get_exits():
            traversal_graph[curr_room.id]['s']= '?'
            graphq.enqueue(path + [curr_room.s_to])

        if 'w' in curr_room.get_exits():
            traversal_graph[curr_room.id]['w']= '?'
            graphq.enqueue(path + [curr_room.w_to])
            
        if 'e' in curr_room.get_exits():
            traversal_graph[curr_room.id]['e']= '?'
            graphq.enqueue(path + [curr_room.e_to])

#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# THIS PART UP HERE WORKS AS INTENDED




# INITIAL TRAVERSAL, WORKS
#  VVVVVVVVVVVVVVVVVVVVVV

def initial(start):
    queue = Queue()
    queue.enqueue([start])
    visited = set()

    while queue.size() > 0:
        v = queue.dequeue()
        roomba = v[-1]
        if roomba not in visited:
            visited.add(roomba)
            path = []
            for item in v:
                path.append(item)
            for i in roomba.get_exits():
                if i is 'n':
                    queue.enqueue(path + [roomba.n_to])
                if i is 's':
                    queue.enqueue(path + [roomba.s_to])
                if i is 'w':
                    queue.enqueue(path + [roomba.w_to])
                if i is 'e':
                    queue.enqueue(path + [roomba.e_to])
        else:
            final = []
            roomz = []
            room_idz = []
            for i in path:
                room_idz.append(i.id)
                roomz.append(i)
            for i in range(0, len(path)):
                j = i - 1
                if path[j].n_to == path[i]:
                    final.append('n')
                    traversal_graph[path[j].id]['n'] = path[i].id
                    traversal_graph[path[i].id]['s'] = path[j].id
                elif path[j].s_to == path[i]:
                    final.append('s')
                    traversal_graph[path[j].id]['s'] = path[i].id
                    traversal_graph[path[i].id]['n'] = path[j].id
                elif path[j].w_to == path[i]:
                    final.append('w')
                    traversal_graph[path[j].id]['w'] = path[i].id
                    traversal_graph[path[i].id]['e'] = path[j].id
                elif path[j].e_to == path[i]:
                    final.append('e')
                    traversal_graph[path[j].id]['e'] = path[i].id
                    traversal_graph[path[i].id]['w'] = path[j].id
    return [final, roomz[-1]]

result = initial(world.starting_room)
traversal_path = traversal_path + result[0]

new_room = result[1]

#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# THIS BIT HERE WORKS (25 rooms down)




# V   REVERSAL WORKS   V

def reverse(dir):
    if dir == 'n':
        return 's'
    elif dir == 's':
        return 'n'
    elif dir == 'w':
        return 'e'
    elif dir == 'e':
        return 'w'
    else:
        return

# ^   REVERSAL WORKS  ^




# print(traversal_path)
# print(reversal_path)


def bread(room):
    queue = Queue()
    queue.enqueue([room])
    visited = set()
    reversal_path = []
    for i in reversed(traversal_path):
        reversal_path.append(reverse(i))

    while queue.size() > 0:
        v = queue.dequeue()
        thisroom = v[-1]
        final = []
        if thisroom is not None and thisroom not in visited:
            visited.add(thisroom)
            path = []
            for item in v:
                path.append(item)
        
                if '?' not in traversal_graph[thisroom.id].values():
                    if reversal_path[0] == 'n':
                        queue.enqueue(path + [thisroom.n_to])
                        reversal_path.pop(0)
                        final.append('n')

                    elif reversal_path[0] == 's':
                        queue.enqueue(path + [thisroom.s_to])
                        reversal_path.pop(0)
                        final.append('s')

                    elif reversal_path[0] == 'w':
                        queue.enqueue(path + [thisroom.w_to])
                        reversal_path.pop(0)
                        final.append('w')

                    elif reversal_path[0] == 'e':
                        queue.enqueue(path + [thisroom.e_to])
                        reversal_path.pop(0)
                        final.append('e')

                if thisroom is not None:
                    for i in thisroom.get_exits():
                        if i is 'n' and traversal_graph[thisroom.id]['n'] is '?':
                            queue.enqueue(path + [thisroom.n_to])
                        elif i is 's' and traversal_graph[thisroom.id]['s'] is '?':
                            queue.enqueue(path + [thisroom.s_to])
                        elif i is 'w' and traversal_graph[thisroom.id]['w'] is '?':
                            queue.enqueue(path + [thisroom.w_to])
                        elif i is 'e' and traversal_graph[thisroom.id]['e'] is '?':
                            queue.enqueue(path + [thisroom.e_to])
        else:
            
            for i in range(0, len(v)-1):
                j = i - 1
                if path[j].n_to == path[i]:
                    traversal_path.append('n')
                    traversal_graph[path[j].id]['n'] = path[i].id
                    traversal_graph[path[i].id]['s'] = path[j].id
                elif path[j].s_to == path[i]:
                    traversal_path.append('s')
                    traversal_graph[path[j].id]['s'] = path[i].id
                    traversal_graph[path[i].id]['n'] = path[j].id
                elif path[j].w_to == path[i]:
                    traversal_path.append('w')
                    traversal_graph[path[j].id]['w'] = path[i].id
                    traversal_graph[path[i].id]['e'] = path[j].id
                elif path[j].e_to == path[i]:
                    traversal_path.append('e')
                    traversal_graph[path[j].id]['e'] = path[i].id
                    traversal_graph[path[i].id]['w'] = path[j].id
            idid = []
            for i in v:
                if i is not None:
                    idid.append(i.id)

    return path[-1]

# ^^^^^  THIS WORKS, BACKTRACKS TO A NEARBY ROOM WITH NO '?'s   ^^^^^



res2 = bread(new_room)
res3 = bread(res2)























# def initial(start):
#     stack = Stack()
#     stack.push([start])
#     visited = set()

#     last_direction = 'x'

#     while stack.size() > 0:
#             v = stack.pop()
#             room = v[-1]
            
#             if room not in visited:
#                 visited.add(room)
#                 path = []
#                 if last_direction is 'n':
#                     if room.n_to is None and room.e_to is None and room.w_to is None: 
#                         return v
#                 if last_direction is 's':
#                     if room.s_to is None and room.e_to is None and room.w_to is None: 
#                         return v
#                 if last_direction is 'w':
#                     if room.n_to is None and room.e_to is None and room.s_to is None: 
#                         return v
#                 if last_direction is 'e':
#                     if room.n_to is None and room.e_to is None and room.s_to is None: 
#                         return v

#                 for item in v:
#                     path.append(item)
#                 if 'n' in room.get_exits():
#                     stack.push(path + [room.n_to])
#                     last_direction = 'n'
#                 elif 's' in room.get_exits():
#                     stack.push(path + [room.s_to])
#                     last_direction = 's'
#                 elif 'w' in room.get_exits():
#                     stack.push(path + [room.w_to])
#                     last_direction = 'w'
#                 elif 'e' in room.get_exits():
#                     stack.push(path + [room.e_to])
#                     last_direction = 'e'

# list1 = initial(world.starting_room)
# list2 = []

# for i in list1:
#     list2.append(i.id)

# print("LIST2",list2)







# print("GRAPH", traversal_graph)
# print("PATH", traversal_path)


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
