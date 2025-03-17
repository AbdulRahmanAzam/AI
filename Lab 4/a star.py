graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}


# Heuristic function (estimated cost to reach goal 'I')
heuristic = {
'A': 7,
'B': 6,
'C': 5,
'D': 4,
'E': 7,
'F': 3,
'G': 6,
'H': 2,
'I': 0 # Goal node
}


def aStar(graph, heuristic, start, goal):
    frontier = [(start, 0 + heuristic[start])]

    visited = set()
    g_cost = {start: 0}
    came_from = {start:None}

    while frontier:
        frontier.sort(key=lambda x:x[1])
        currNode, currF = frontier.pop(0)

        if currNode in visited:
            continue

        print(currNode, end=" ")
        visited.add(currNode)

        if currNode == goal:
            path = []

            while currNode is not None:
                path.append(currNode)
                currNode = came_from[currNode]
            
            path.reverse()
            print(f"\nGoal Found: Path: {path}")
            return
        
        for neighbour, cost in graph[currNode].items():
            new_g_cost = g_cost[currNode] + cost
            f_cost = new_g_cost + heuristic[neighbour]

            if neighbour not in g_cost or new_g_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_g_cost
                came_from[neighbour] = currNode
                frontier.append((neighbour, f_cost))

    print("Goal Not Found")

aStar(graph, heuristic, 'A', 'I')


