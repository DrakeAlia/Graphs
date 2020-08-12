# You have been assigned the task of building a new friend-based social network. In this network, users are able to view their own friends, friends of their friends, friends of their friends' friends, and so on. People connected to you through any number of friendship connections are considered a part of your extended social network.
# The functionality behind creating users and friendships has been completed already. Your job is to implement a function that shows all the friends in a user's extended social network and chain of friendships that link them. The number of connections between one user and another are called the degrees of separation.
# Your client is also interested in how the performance will scale as more users join so she has asked you to implement a feature that creates large numbers of users to the network and assigns them a random distribution of friends.



from random import shuffle
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # empty array for non mutual friends
        self.non_mutual = []

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
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # For loop that calls the create user the right amount of times
        for i in range(num_users):
            self.add_user(f"{i + 1}")
        # Shuffle the list, then grab the first N elements from the list
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id +1, self.last_id +1):
                possible_friendships.append((user_id,friend_id))
        
        shuffle(possible_friendships)

        # Create friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0],friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        direct_friends = self.friendships[user_id]
        print(f"\nImmediate Friends {direct_friends}")

        if len(direct_friends) == 0:
            print(f"User {user_id} has no friends :(")
            return {}

        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            # Grab the first path
            path = q.dequeue()
            # Get the last node in the path
            v = path[-1]
            if v not in visited:
                # Add the path to the id
                visited[v] = path
                
                for friend in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        for user in self.users:
            if user not in visited:
                self.non_mutual.append(user)

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    #  Print out for users who have no mutual friends 
    print(f"These users have no mutual friend {sg.non_mutual}")


# Other Method, but was getting a large array of nums:
# import random

# class User:
#     def __init__(self, name):
#         self.name = name

# class SocialGraph:
#     def __init__(self):
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}

#     def add_friendship(self, user_id, friend_id):
#         """
#         Creates a bi-directional friendship
#         """
#         if user_id == friend_id:
#             print("WARNING: You cannot be friends with yourself")
#         elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
#             print("WARNING: Friendship already exists")
#         else:
#             self.friendships[user_id].add(friend_id)
#             self.friendships[friend_id].add(user_id)

#     def add_user(self, name):
#         """
#         Create a new user with a sequential integer ID
#         """
#         self.last_id += 1  # automatically increment the ID to assign the new user
#         self.users[self.last_id] = User(name)
#         self.friendships[self.last_id] = set()

#     def fisher_yates_shuffle(self, l):
#         for i in range(0, len(l)):
#             random_index = random.randint(i, len(l) - 1)
#             l[random_index], l[i] = l[i], l[random_index]

#     def populate_graph(self, num_users, avg_friendships):
#         """
#         Takes a number of users and an average number of friendships
#         as arguments

#         Creates that number of users and a randomly distributed friendships
#         between those users.

#         The number of users must be greater than the average number of friendships.
#         """
#         # Reset graph
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}
#         # !!!! IMPLEMENT ME

#         # Add users
#         # Use num_users
#         for user in range(num_users):
#             self.add_user(user)

#         # Create friendships
#         # Make a list with all POSSIBLE friendships
#         # Example:
#         # 5 users
#         # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
#         friendships = []
#         for user in range(1, self.last_id + 1):
#             for friend in range(user + 1, num_users + 1):
#                 friendship = (user, friend)
#                 friendships.append(friendship)

#         # Shuffle the list
#         self.fisher_yates_shuffle(friendships)

#         # Take as many as we need
#         total_friendships = num_users * avg_friendships

#         random_friendships = friendships[:total_friendships//2]
#         # Add to self.friendships
#         for friendship in random_friendships:
#             self.add_friendship(friendship[0], friendship[1])


#     def get_all_social_paths(self, user_id):
#         """
#         Takes a user's user_id as an argument

#         Returns a dictionary containing every user in that user's
#         extended network with the shortest friendship path between them.

#         The key is the friend's ID and the value is the path.
#         """
#         visited = {}  # Note that this is a dictionary, not a set
#         # !!!! IMPLEMENT ME
#         user_list = []

#         # Store the given user in a visited dict() & user_list_queue
#         visited[user_id] = [user_id]
#         user_list.append(user_id)

#         # While user_list_queue isn't empty
#         while len(user_list) > 0:
#         # Visit the friends of a given user
#             user_id = user_list.pop(0)
#             friend_path = visited[user_id]


#             # For each friend    
#             for user in sg.friendships[user_id]:
#                 # Add friend/user : path to visited dict() and to user_list_queue
#                 # If not in visited dict()
#                 if user not in visited:
#                     # For each user in user_list_queue
#                     user_path = friend_path.copy()
#                     user_path.append(user)
#                     print("path:", user_path)
#                     visited[user] = user_path
#                     # Add friends of user to the user queue
#                     user_list.append(user)

#         return visited

# if __name__ == '__main__':
#     sg = SocialGraph()
#     sg.populate_graph(1000, 20)
#     print(sg.friendships)
#     connections = sg.get_all_social_paths(1)
#     print(connections)