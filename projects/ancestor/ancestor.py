from util import Stack, Queue  

def earliest_ancestor(ancestors, starting_node):

    counter = 0
    
    for i in ancestors:
        if i[1] == starting_node:
            counter += 1
            earliest_ancestor(ancestors, i[0])
            
    print(counter)


            
           

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