maze: List[List[int]] = [
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 1],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0]
]

def heuristic(source: Tuple[int, int], goal: Tuple[int, int]) -> int:
  return abs(source[0] - goal[0]) + abs(source[1] - goal[1])

goals: Set[Tuple[int, int]] = set([(4, 4), (2, 3), (0, 4)])

type DistanceDict = Dict[Tuple[int, int], Tuple[int, Optional[Tuple[int, int]]]]
def best_first_search(maze: List[List[int]], source: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
  dists: DistanceDict = {source: (0, None)}
  pq = [source]
  n, m = len(maze), len(maze[-1])

  def construct_path() -> List[Tuple[int, int]]:
    path = [goal]
    curr: Optional[Tuple[int, int]] = goal
    while curr:
      parent = dists[curr][1]
      path.append(parent)
      curr = parent
    return path[::-1][1:]

  while pq:
    r, c = heapq.heappop(pq)

    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
      nr, nc = r + dr, c + dc
      if not (0 <= nr < n and 0 <= nc < m) or maze[nr][nc] == 1:
        continue

      f = heuristic((nr, nc), goal)
      if f < dists.get((nr, nc), (float('inf'), None))[0]:
        dists[(nr, nc)] = (f, (r, c))
        heapq.heappush(pq, (nr, nc))

  return construct_path()

def display_path(maze: List[List[int]], path: List[Tuple[int, int]]):
  for r, c in path:
    maze[r][c] = 2
  print(*map(lambda row: ' '.join(map(str, row)), maze), sep="\n", end="\n\n")

for goal in goals:
  path = best_first_search(maze, (0, 0), goal)
  display_path([row[:] for row in maze], path)
