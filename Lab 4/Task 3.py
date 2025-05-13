from typing import List, Tuple
import heapq

grid = [
  ["S", ".", ".", "D1", "#"],
  [".", "#", ".", ".", "."],
  [".", ".", ".", "#", "D2"],
  ["D3", ".", "#", ".", "."],
  [".", "D4", ".", ".", "."],
]

nodes = {
  "D1": (0, 3, 5, 15),
  "D2": (2, 4, 8, 12),
  "D3": (3, 0, 10, 20),
  "D4": (4, 1, 7, 14),
}

start = (0, 0)

def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def greedy_best_first_search(grid: List[List[str]], start: Tuple[int, int], nodes: dict):
  rows, cols = len(grid), len(grid[0])
  visited = set()
  pq = []
  route = []
  curr_time = 0
  heapq.heappush(pq, (0, start, curr_time))

  while pq:
    _, current, curr_time = heapq.heappop(pq)
    if current in visited:
      continue
    visited.add(current)
    route.append(current)

    for name, (x, y, t_start, t_end) in list(nodes.items()):
      if (x, y) == current and t_start <= curr_time <= t_end:
        nodes.pop(name)
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = current[0] + dx, current[1] + dy
      if not (0 <= nx < rows and 0 <= ny < cols) or (nx, ny) in visited or grid[nx][ny] == "#":
        continue

      heuristic = float("inf")
      for name, (tx, ty, t_start, t_end) in nodes.items():
        travel_time = curr_time + 1 + distance((nx, ny), (tx, ty))
        if travel_time <= t_end:
          time_priority = 1 / (t_end - travel_time + 1)
          dist_priority = distance((nx, ny), (tx, ty))
          heuristic = min(heuristic, 0.7 * time_priority + 0.3 * dist_priority)
      heapq.heappush(pq, (heuristic, (nx, ny), curr_time + 1))

  return route

greedy_best_first_search(grid, start, nodes)
