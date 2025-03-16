from collections import deque


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

# -------------------------------------------------------------- DFS
```
    def dfs(self, start, goal):
        visited = []
        stack = [(start, [start])] # storing path as well

        while stack:
            node, path = stack.pop()
            print(f"Visiting: {node}")

            if node == goal:
                print("Goal achieved")
                return path
            
            if node not in visited:
                visited.append(node)
                for neighbour in reversed(self.graph[node]):
                    if neighbour not in visited:
                        stack.append((neighbour, path + [neighbour]))

        print("Goal not found")
        return None
```
# -------------------------------------------------------------- BFS
```
    def bfs(self, start, goal):
        visited = []
        queue = [(start, [start])]

        while queue:
            node, path = queue.pop(0)
            print(f"Visiting: {node}")

            if node == goal:
                print("Goal achieved")
                return path
            
            if node not in visited:
                visited.append(node)
                for neighbour in self.graph[node]:
                    if neighbour not in visited:
                        queue.append((neighbour, path + [neighbour]))
```
# -------------------------------------------------------------- DLS
```
    def dls(self, start, goal, depth_limit):
        visited = []

        def dfs(node, depth):
            if depth > depth_limit:
                return None
            
            visited.append(node)
            if node == goal:
                print(f"Goal Achieved, Path: {visited}")
                return visited[:]
            
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    path = dfs(neighbour, depth + 1)
                    if path:
                        return path
                    
            visited.pop() # this must not be written, said by gpt
            return None

        return dfs(start, 0)        
```
# -------------------------------------------------------------- UCS
```
    def ucs(self, start, goal):
        frontier = [(0, start)] # (cost, node)
        visited = []
        cost_sofar = {start: 0}
        parent = {}

        while frontier:
            frontier.sort()
            current_cost, node = frontier.pop(0)

            if node in visited:
                continue

            visited.add(node)

            if node == goal:
                path = [] 

                while node:
                    path.append(node)
                    node = parent.get(node)
                
                path.reverse()
                print(f"Goal Achieved, Path: {path}, Total Cost: {current_cost}")
                return path, current_cost
            
            for neighbour, cost in self.graph.get(node, {}).items():
                new_cost = current_cost + cost
                if neighbour not in cost_sofar or new_cost < cost_sofar[neighbour]:
                    cost_sofar[neighbour] = new_cost
                    parent[neighbour] = node
                    frontier.append((new_cost, neighbour))

        print("Goal Not Found")
        return None, float('inf')
    
```
     # -------------------------------------------------------------- IDDFS
```
    def dls_for_iddfs(self, node, goal, depth_limit, path):
        if depth_limit == 0:
            return [node] if node == goal else None
        
        path.append(node)

        if node == goal:
            return path[:]
        
        if node not in self.graph:
            path.pop()
            return None
        
        for neighbour in self.graph[node]:
            if neighbour not in path:
                result = self.dls_for_iddfs(neighbour, goal, depth_limit - 1, path)
                if result:
                    return result

        path.pop()
        return None                
        
    def iddfs(self, start, goal, max_depth):
        for depth in range(max_depth):
            print(f"Trying depth limit: {depth}")
            path = []

            result = self.dls_for_iddfs(start, goal, depth, path)

            if result:
                print(f"Goal found at depth: {depth}, Path: {result}")
                return result
        
        print("Goal not found within dpeth limit")
        return None
```
    # -------------------------------------------------------------- BIDIRECTIONAL SEARCH
```
    def bidirectional_search(self, start, goal):
        if start == goal:
            return [start]
        
        fqueue = deque([start])
        bqueue = deque([goal])

        fvisited = {start:None}
        bvisited = {goal:None}

        while fqueue and bqueue:

            if fqueue:
                node = fqueue.popleft()
                
                for neighbour in self.graph[node]:
                    if neighbour not in fvisited:
                        fvisited[neighbour] = node
                        fqueue.append(neighbour)

                        if neighbour in bvisited:
                            return self.reconstruct_path(fvisited, bvisited,neighbour)

            if bqueue:
                node = bqueue.popleft()

                for neighbour in self.graph[node]:
                    if neighbour not in bvisited:
                        bvisited[neighbour] = node
                        bqueue.append(neighbour)
```
