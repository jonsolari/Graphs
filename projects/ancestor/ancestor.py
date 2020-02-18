from util import Stack, Queue  

def earliest_ancestor(ancestors, starting_node, visited=None):

    if visited is None:
        visited = set()
    
    for i in ancestors:
        if i[1] == starting_node:
            print(i[0])
            visited.add(i[1])
            earliest_ancestor(ancestors, i[0], visited)
            

    
            
           

earliest_ancestor([(1, 3), 
                   (2, 3), 
                   (3, 6), 
                   (5, 6), 
                   (5, 7), 
                   (4, 5),
                   (4, 8), 
                   (8, 9), 
                   (11, 8), 
                   (10, 1)], 6)