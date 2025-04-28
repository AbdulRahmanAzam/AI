# run agent => percept and action

class Algorithms:
    def __init__(self):
        pass

    def bfs(self, tree, start, goal):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)

            print(node, end=" ")

            if node == goal:
                print("BFS. Goal Found. PATH: ", visited)
                break

            for neighbour in tree[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)



    def dfs(self, graph, start, goal):
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()   # LIFO: Pop from top

            print(node, end=" ")

            if node == goal:
                print("DFS. Goal Found. PATH: ", visited)
                break

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)


    def dls(self, graph, start, goal, limit):
        # Use a list to track the path during search
        path = []

        def dfs(node, depth):
            # Add the current node to our path
            path.append(node)
            
            if node == goal:
                print(f"DLS. Goal Found. PATH: {path}")
                return path.copy()  # Return a copy of the current path
            
            if depth == limit:
                path.pop()  # Remove this node from path on backtracking
                return None
            
            for neighbour in graph[node]:
                if neighbour not in path:  # Avoid cycles
                    result = dfs(neighbour, depth + 1)
                    if result:
                        return result
            
            # Backtrack - remove this node from path when going back up
            path.pop()
            return None
        
        return dfs(start, 0)


    def ucs(self, graph, start, goal):
        frontier = [(start, 0)]
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}

        while frontier:
            frontier.sort(key=lambda x: x[1])

            node, curr_cost = frontier.pop(0)   # pop the lowest cost node

            if node in visited:
                continue

            visited.add(node)

            if node == goal:
                path = []
                while node:
                    path.append(node)
                    node = came_from[node]

                path.reverse()
                print(f"UCS. Goal Found. Path: {path}, Total cost: {curr_cost}")
                return path
            
            for neighbour, edge_cost in graph[node].items():
                new_cost = curr_cost + edge_cost
                if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                    cost_so_far[neighbour] = new_cost
                    came_from[neighbour] = node
                    frontier.append((neighbour, new_cost))

        return None
    

    def iterative_deepening_search(self, graph, start, goal, max_depth):
        for depth in range(max_depth+1):
            print(f"Trying depth limit: {depth}")
            result = self.dls(graph, start, goal, depth)

            if result:
                print(f"IDDFS. Goal Found at depth {depth}. PATH: {result}")
                return result
            
        print(f"IDDFS. Goal NOT found within depth limit {max_depth}")
        return None
    
    def bidirectional_search(self, graph, start, goal):
        # Forward search from start
        forward_queue = [start]
        forward_visited = {start: None}  # Maps node to its parent
        
        # Backward search from goal
        backward_queue = [goal]
        backward_visited = {goal: None}  # Maps node to its parent
        
        # Track the meeting point
        intersection = None
        
        while forward_queue and backward_queue and intersection is None:
            # Forward BFS step
            current = forward_queue.pop(0)
            
            # Check neighbors in forward direction
            for neighbor in graph[current]:
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = current
                    forward_queue.append(neighbor)
                    
                    # Check if we found intersection with backward search
                    if neighbor in backward_visited:
                        intersection = neighbor
                        break
            
            if intersection:
                break
                
            # Backward BFS step
            current = backward_queue.pop(0)
            
            # Check neighbors in backward direction
            for neighbor in graph[current]:
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = current
                    backward_queue.append(neighbor)
                    
                    # Check if we found intersection with forward search
                    if neighbor in forward_visited:
                        intersection = neighbor
                        break
        
        if intersection is None:
            print("No path found between start and goal")
            return None
        
        # Reconstruct the path
        # First, build path from start to intersection
        path_from_start = []
        current = intersection
        while current is not None:
            path_from_start.append(current)
            current = forward_visited[current]
        path_from_start.reverse()
        
        # Then, build path from intersection to goal
        path_to_goal = []
        current = backward_visited[intersection]
        while current is not None:
            path_to_goal.append(current)
            current = backward_visited[current]
        
        # Combine paths (removing duplicate intersection node)
        full_path = path_from_start + path_to_goal
        
        print(f"Bidirectional search. Goal found. PATH: {full_path}")
        return full_path


# Main function to test all algorithms
def main():
    # Initialize the algorithms class
    algs = Algorithms()
    
    # Create a sample graph for unweighted search algorithms (BFS, DFS, DLS, IDDFS, Bidirectional)
    # This represents connections between nodes, where each node is connected to its neighbors
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'H'],
        'E': ['B', 'I'],
        'F': ['C', 'J'],
        'G': ['C'],
        'H': ['D'],
        'I': ['E'],
        'J': ['F']
    }
    
    # Create a weighted graph for UCS
    # This represents connections between nodes with associated costs
    weighted_graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'D': 3, 'E': 1},
        'C': {'A': 3, 'F': 2, 'G': 4},
        'D': {'B': 3, 'H': 1},
        'E': {'B': 1, 'I': 5},
        'F': {'C': 2, 'J': 1},
        'G': {'C': 4},
        'H': {'D': 1},
        'I': {'E': 5},
        'J': {'F': 1}
    }
    
    print("\n" + "="*50)
    print("TESTING BREADTH-FIRST SEARCH (BFS)")
    print("="*50)
    algs.bfs(graph, 'A', 'J')
    
    print("\n" + "="*50)
    print("TESTING DEPTH-FIRST SEARCH (DFS)")
    print("="*50)
    algs.dfs(graph, 'A', 'J')
    
    print("\n" + "="*50)
    print("TESTING DEPTH-LIMITED SEARCH (DLS)")
    print("="*50)
    algs.dls(graph, 'A', 'J', 3)  # Limit depth to 3
    
    print("\n" + "="*50)
    print("TESTING ITERATIVE DEEPENING SEARCH (IDDFS)")
    print("="*50)
    algs.iterative_deepening_search(graph, 'A', 'J', 5)  # Max depth 5
    
    print("\n" + "="*50)
    print("TESTING UNIFORM COST SEARCH (UCS)")
    print("="*50)
    algs.ucs(weighted_graph, 'A', 'J')
    
    print("\n" + "="*50)
    print("TESTING BIDIRECTIONAL SEARCH")
    print("="*50)
    algs.bidirectional_search(graph, 'A', 'J')


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()









