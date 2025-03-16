graph = {
0: [1, 3],
1: [0, 3],
2: [4,5],
3: [0, 1, 6, 4],
4: [3, 2, 5],
5: [4, 2, 6],
6: [3, 5]
}

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
            print(f"Visiting: {node}")

            if node == goal:
                print("Goal Achieved")
                break

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulateGoal(self, percept):
        if percept ==  self.goal:
            return (f"Goal Achieved")
        else:
            return ("Goal Not achieved yet")

    def act(self, percept, environment):
        goalstatus = self.formulateGoal(percept)

        if goalstatus == "Goal Achieved":
            return f"Goal {self.goal} Found"
        else:
            environment.bfs(percept, self.goal)

    
def run_agent(self, environment, agent, start):
    percept = environment.get_percept(start)
    action = agent.act(percept, environment)

    print(action)

start = 0
goal = 5

environment = Environment(graph)
agent = GoalBasedAgent(goal)

run_agent(environment, agent, start)
