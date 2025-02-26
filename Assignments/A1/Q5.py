# Code is written by me
# Comments are written by GPT
from queue import PriorityQueue, Queue

# Graph representation with cities as nodes and distances as edges
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Heuristic values for Greedy Best First Search
heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

def bfs(start, goal):
    """Breadth-First Search algorithm"""
    queue = Queue()
    queue.put((start, [start]))
    explored = set()
    while not queue.empty():
        node, path = queue.get()
        if node == goal:
            return path, len(path)-1
        if node not in explored:
            explored.add(node)
            for neighbor in graph[node]:
                queue.put((neighbor, path + [neighbor]))
    return None, float('inf')

def ucs(start, goal):
    """Uniform Cost Search algorithm"""
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    explored = set()
    while not queue.empty():
        cost, node, path = queue.get()
        if node == goal:
            return path, cost
        if node not in explored:
            explored.add(node)
            for neighbor, weight in graph[node].items():
                queue.put((cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

def greedy_best_first(start, goal):
    """Greedy Best-First Search algorithm using heuristic values"""
    queue = PriorityQueue()
    queue.put((heuristics[start], start, [start]))
    explored = set()
    while not queue.empty():
        _, node, path = queue.get()
        if node == goal:
            return path, sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
        if node not in explored:
            explored.add(node)
            for neighbor in graph[node]:
                queue.put((heuristics[neighbor], neighbor, path + [neighbor]))
    return None, float('inf')

def iddfs(start, goal, max_depth=20):
    """Iterative Deepening Depth-First Search algorithm"""
    def dls(node, path, depth):
        if depth == 0:
            return None, float('inf')
        if node == goal:
            return path, len(path)-1
        for neighbor in graph[node]:
            if neighbor not in path:
                result, cost = dls(neighbor, path + [neighbor], depth - 1)
                if result:
                    return result, cost
        return None, float('inf')
    
    for depth in range(1, max_depth + 1):
        result, cost = dls(start, [start], depth)
        if result:
            return result, cost
    return None, float('inf')

if __name__ == "__main__":
    # Take input from the user
    start = input("Enter the source city: ")
    goal = input("Enter the destination city: ")
    
    # Execute search algorithms and display results
    print("\nResults:")
    for algo, func in zip(["BFS", "UCS", "Greedy Best First", "IDDFS"], [bfs, ucs, greedy_best_first, iddfs]):
        path, cost = func(start, goal)
        print(f"{algo}: Path = {path}, Cost = {cost}")
