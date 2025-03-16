maze = [
[1, 1, 0],
[0, 1, 0],
[0, 1, 1]
]

#             Right    Down
directions = [(0,1), (1,0)]  # (row, col)


def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):

            if maze[i][j] == 1:
                neighbours = []

                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1:
                        neighbours.append((x,y))

                graph[(i, j)] = neighbours

    return graph

def bfs(graph, start, goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(f"Visiting: {node}")

        if node == goal:
            print(f"Goal {node} achieved")
            break
            
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = create_graph(maze)

start = (0,0)
goal = (2,2)

bfs(graph, start, goal)


