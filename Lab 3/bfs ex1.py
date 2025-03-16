
class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def bfs(self, start, goal):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)
            print(f'Visiting: {node}')

            if node == goal:
                print("\nGoal {node} Found")
                break

            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal Achieved"
        
        return "Searching"
    
    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)

        if goal_status == "Goal Achieved":
            return f"Goal {self.goal} found"
        else:
            return environment.bfs(percept, self.goal)
        
def run_agent(agent, environment, start):
    percept = environment.get_percept(start)
    action = agent.act(percept, environment)

    print(action)

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

start = 'A'
goal = 'I'

agent = GoalBasedAgent(goal)
environment = Environment(tree)

run_agent(agent, environment, start)

