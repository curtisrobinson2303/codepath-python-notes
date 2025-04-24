"""
Problem 7: Number of Flights
You are a travel planner and have an adjacency matrix flights with n airports labeled 0 to n-1 where flights[i][j] indicates CodePath Airlines offers a flight from airport i to airport j. You are planning a trip for a client and want to know the minimum number of flights (edges) it will take to travel from airport start to their final destination airport destination on CodePath Airlines.

Return the minimum number of flights needed to travel from airport i to airport j. If it is not possible to fly from airport i to airport j, return -1.

def counting_flights(flights, i, j):
    pass
Example Usage:


# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
Example Output:

1
Example 1 Explanation: Flight path: 0 -> 2
3
Example 2 Explanation: Flight path 0 -> 2 -> 3 -> 4
-1
Explanation: Cannot fly from Airport 4 to Airport 0
"""

from collections import deque


def counting_flights(flights, i, j):
    # get the length of adj matrix
    # keep track of the visited nodes
    # use queue to keep track of the current node and all edges off that node
    #
    # iterate through each of the nodes adding the previous node distances as the bfs algorithms touches the next set of neigbors

    # return -1 if no path is found

    n = len(flights)
    visited = [False] * n
    queue = deque()
    queue.append([i, 0])

    while queue:
        current, num_flights = queue.popleft()

        if current == j:
            return num_flights


# Example usage
flights = [
    [0, 1, 1, 0, 0],  # Airport 0
    [0, 0, 1, 0, 0],  # Airport 1
    [0, 0, 0, 1, 0],  # Airport 2
    [0, 0, 0, 0, 1],  # Airport 3
    [0, 0, 0, 0, 0],  # Airport 4
]

print(counting_flights(flights, 0, 2))
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))

from collections import deque


# def counting_flights(flights, start, destination):
#     n = len(flights)
#     visited = [False] * n
#     queue = deque([(start, 0)])  # (current_airport, num_flights)

#     while queue:
#         current, num_flights = queue.popleft()

#         if current == destination:
#             return num_flights

#         visited[current] = True

#         for neighbor in range(n):
#             if flights[current][neighbor] == 1 and not visited[neighbor]:
#                 queue.append((neighbor, num_flights + 1))

#     return -1  # No path found
