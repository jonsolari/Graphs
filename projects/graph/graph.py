"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
     
        # create an empty queue

        queue = Queue()

        # add starting vertex id to queue

        queue.enqueue(starting_vertex)

        # create an empty set to store visited nodes
        visited = set()
    
        # while the queue is not empty,
            # dequeue the first vertex
            # check if it's been visited. if not,
            # mark it as visited
            # add all neighbors to the back of the queue
        while queue.size() > 0:

            v = queue.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    queue.enqueue(neighbor)

        # while the queue is not empty,
            # dequeue the first vertex
            # check if it's been visited. if not,
            # mark it as visited
            # add all neighbors to the back of the queue

        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack

        stack = Stack()

        # push starting vertex id to stack

        stack.push(starting_vertex)

        # create an empty set to store visited nodes
        visited = set()
    
        # while the stack is not empty,
            # pop the first vertex
            # check if it's been visited. if not,
            # mark it as visited
            # add all neighbors to the top of the stack
        while stack.size() > 0:

            v = stack.pop()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if the node is visited
        # if not
            # mark as visited
            # print
            # call dft_recursive on each child
        if visited is None:
            visited = set()
        
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # create an empty queue
        # add A PATH TO the starting vertex_id to the queue
        # create an empty set to store visited nodes
        # while the queue is not empty:
            # dequeue the first PATH
            # grab the last vertex from the path
            # check if it's the target
                # if so, return path
            # check if it's been visited
            # if it hasn't:
                # mark it as visited
                # add A PATH TO all neighbors to the back of queue
                    # make a copy of the path before adding
        
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
    
        while queue.size() > 0:
            v = queue.dequeue()
            if v[-1] == destination_vertex:
                return v
            if v[-1] not in visited:
                visited.add(v[-1])
                path = []
                for item in v:
                    path.append(item)
                for neighbor in self.get_neighbors(v[-1]):
                    queue.enqueue(path + [neighbor])


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
    
        while stack.size() > 0:
            v = stack.pop()
            if v[-1] == destination_vertex:
                return v
            if v[-1] not in visited:
                visited.add(v[-1])
                path = []
                for item in v:
                    path.append(item)
                for neighbor in self.get_neighbors(v[-1]):
                    stack.push(path + [neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
 
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                path2 = self.dfs_recursive(neighbor, destination_vertex, path, visited)
                if path2 is not None:
                    return path2

       

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
