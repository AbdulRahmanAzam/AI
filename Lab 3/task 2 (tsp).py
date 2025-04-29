graph = { 
    'A': {'B':10, 'C':15, 'D':20},
    'B': {'A':10, 'C':35, 'D':25},
    'C': {'A':15, 'B':35, 'D':30},
    'D': {'A':20, 'B':25, 'C':30}
}

def generate_permutations(elements):
    if len(elements) == 0:
        return [[]]
    
    result = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i+1:]

        for perm in generate_permutations(rest):
            result.append([elements[i]] + perm)
        
    return result

def calculate_tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    permutations = generate_permutations(nodes)

    min_path = None
    min_cost = float('inf')
    
    print("\nAll possible paths from", start, ":")

    for perm in permutations: 
        curr_path = start
        curr_cost = 0
        path = [start]

        for node in perm:
            curr_cost += graph[curr_path][node]
            curr_path = node
            path.append(node)

        curr_cost += graph[curr_path][start]
        path.append(start)
        
        # Print this path and its cost
        path_str = ' -> '.join(path)
        print(f"Path: {path_str}, Cost: {curr_cost}")

        if curr_cost < min_cost:
            min_cost = curr_cost
            min_path = path

    return min_path, min_cost


def main():
    start_node = 'A'
    path, cost = calculate_tsp(graph, start_node)
    print(f"\nMinimum Path: {' -> '.join(path)}, Minimum Cost: {cost}")


if __name__ == "__main__":
    main()
