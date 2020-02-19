import random
from util import Stack, Queue  

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
      
        self.last_id = 0
        self.users = {}
        self.friendships = {}
      
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        

        random.shuffle(possible_friendships)
        

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_neighbors(self, vertex_id):    
        return self.friendships[vertex_id]

    def bfs(self, starting_vertex, destination_vertex):
        
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


    def get_all_social_paths(self, user_id):
   
        visited = {} 
    
        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:
            pathway = queue.dequeue()
            vertex = pathway[-1]
            if vertex not in visited:
                visited[vertex] = pathway

                for i in self.friendships[vertex]:
                    copy = pathway.copy()
                    copy.append(i)
                    queue.enqueue(copy)
            
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
