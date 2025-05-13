import heapq
import random
import time
from typing import Dict, List, Tuple, Optional

Node = Tuple[int, int]
Edge = Tuple[Node, int]
Graph = Dict[Node, List[Edge]]
Key = Tuple[float, float]

class IncrementalAStar:
  def __init__(self):
    self.g_scores: Dict[Node, float] = {}
    self.rhs: Dict[Node, float] = {}
    self.open_list: List[Tuple[Key, Node]] = []
    self.graph: Graph = {}
    self.start: Optional[Node] = None
    self.goal: Optional[Node] = None

  def initialize(self, graph: Graph, start: Node, goal: Node):
    self.graph = graph
    self.start = start
    self.goal = goal
    self.g_scores = {node: float('inf') for node in graph}
    self.rhs = {node: float('inf') for node in graph}
    self.rhs[goal] = 0
    self.open_list = []
    heapq.heappush(self.open_list, (self.calculate_key(goal), goal))

  def calculate_key(self, node: Node) -> Key:
    g_rhs = min(self.g_scores[node], self.rhs[node])
    return (g_rhs + self.heuristic(node, self.start), g_rhs)

  def heuristic(self, node: Node, target: Node) -> int:
    return abs(node[0] - target[0]) + abs(node[1] - target[1])

  def update_vertex(self, node: Node):
    if self.g_scores[node] != self.rhs[node]:
      heapq.heappush(self.open_list, (self.calculate_key(node), node))
    else:
      self.open_list = [entry for entry in self.open_list if entry[1] != node]
      heapq.heapify(self.open_list)

  def compute_shortest_path(self):
    while self.open_list and (self.open_list[0][0] < self.calculate_key(self.start) or self.rhs[self.start] != self.g_scores[self.start]):
      _, current = heapq.heappop(self.open_list)

      self.g_scores[current] = self.rhs[current] if self.g_scores[current] > self.rhs[current] else float('inf')
      for neighbor, cost in self.graph.get(current, []):
        self.rhs[neighbor] = min(self.rhs[neighbor], self.g_scores[current] + cost)
        self.update_vertex(neighbor)
      self.update_vertex(current)

  def find_path(self) -> Optional[List[Node]]:
    path = []
    current = self.start
    while current != self.goal:
      path.append(current)
      if current not in self.graph or self.g_scores[current] == float('inf'):
        return None
      current = min(self.graph[current], key=lambda x: self.g_scores[x[0]])[0]
    path.append(self.goal)
    return path

  def modify_graph(self):
    for node in random.sample(list(self.graph.keys()), k=random.randint(1, len(self.graph))):
      if not self.graph[node]:
        continue

      neighbor, _ = random.choice(self.graph[node])
      new_cost = random.randint(1, 10)
      print(f"Updating edge {node} -> {neighbor} cost to {new_cost}")
      self.graph[node] = [
        (n, new_cost if n == neighbor else c)
        for n, c in self.graph[node]
      ]
      self.update_vertex(node)

graph = {
  (0, 0): [((1, 0), 1), ((0, 1), 1)],
  (1, 0): [((0, 0), 1), ((1, 1), 1)],
  (0, 1): [((0, 0), 1), ((1, 1), 1)],
  (1, 1): [((1, 0), 1), ((0, 1), 1)],
}

start = (0, 0)
goal = (1, 1)
algo = IncrementalAStar()
algo.initialize(graph, start, goal)

for i in range(2):
  print(f"\nIteration {i+1}:")
  algo.compute_shortest_path()
  path = algo.find_path()
  print("Shortest Path:", path)
  time.sleep(1)
  algo.modify_graph()
