from collections import deque
import time
import copy
from constraint import Problem, AllDifferentConstraint

def load_grid(fname):
    with open(fname, 'r') as f:
        return [l.strip() for l in f if l.strip()]

def grid_from_str(s):
    return [[int(s[i * 9 + j]) for j in range(9)] for i in range(9)]

def grid_to_str(g):
    return ''.join(str(g[i][j]) for i in range(9) for j in range(9))

def find_opts(grid):
    opts = {}
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                vals = set(range(1, 10))
                
                for i in range(9):
                    vals.discard(grid[r][i])
                    vals.discard(grid[i][c])
                
                box_r, box_c = 3 * (r // 3), 3 * (c // 3)
                for i in range(3):
                    for j in range(3):
                        vals.discard(grid[box_r+i][box_c+j])
                
                opts[(r, c)] = vals
    return opts

def find_adj(cell):
    r, c = cell
    adj = set()
    
    for i in range(9):
        if i != c: 
            adj.add((r, i))
        if i != r: 
            adj.add((i, c))
    
    box_r, box_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(3):
        for j in range(3):
            nr, nc = box_r + i, box_c + j
            if (nr, nc) != cell:
                adj.add((nr, nc))
    
    return adj

def trim_opts(opts, a, b):
    changed = False
    to_del = set()
    
    for x in opts[a]:
        if all(x == y for y in opts[b]):
            to_del.add(x)
            
    if to_del:
        opts[a] -= to_del
        changed = True
        
    return changed

def prop_constraints(opts):
    q = deque([(a, b) for a in opts for b in find_adj(a) if b in opts])
    
    while q:
        a, b = q.popleft()
        
        if a not in opts or b not in opts:
            continue
            
        if trim_opts(opts, a, b):
            if not opts[a]:
                return False
                
            for c in find_adj(a):
                if c in opts and c != b:
                    q.append((c, a))
                    
    return True

def pick_cell(opts):
    return min(opts, key=lambda v: len(opts[v]))

def solve_csp(grid, opts):
    if not opts:
        return True

    cell = pick_cell(opts)
    
    for val in sorted(opts[cell]):
        new_grid = copy.deepcopy(grid)
        new_opts = copy.deepcopy(opts)
        
        new_grid[cell[0]][cell[1]] = val
        new_opts.pop(cell)
        
        for adj in find_adj(cell):
            if adj in new_opts:
                new_opts[adj].discard(val)
                
        if prop_constraints(new_opts):
            if solve_csp(new_grid, new_opts):
                grid[:] = new_grid
                return True
                
    return False

def solve_grid(grid):
    opts = find_opts(grid)
    
    if not prop_constraints(opts):
        return None
        
    if solve_csp(grid, opts):
        return grid
        
    return None

def process_file(in_file, out_file):
    grids = load_grid(in_file)
    results = []

    for grid_str in grids:
        grid = grid_from_str(grid_str)
        solved = solve_grid(grid)
        
        if solved:
            results.append(grid_to_str(solved))
        else:
            results.append("No solution")

    with open(out_file, 'w') as f:
        for res in results:
            f.write(res + "\n")

def check_valid(grid, r, c, num):
    for i in range(9):
        if grid[r][i] == num or grid[i][c] == num:
            return False
            
    box_r, box_c = r - r % 3, c - c % 3
    for i in range(3):
        for j in range(3):
            if grid[box_r + i][box_c + j] == num:
                return False
                
    return True

def simple_solver(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for num in range(1, 10):
                    if check_valid(grid, r, c, num):
                        grid[r][c] = num
                        
                        if simple_solver(grid):
                            return True
                            
                        grid[r][c] = 0
                        
                return False
                
    return True

def lib_solver(grid):
    prob = Problem()
    cells = [(i, j) for i in range(9) for j in range(9)]

    for cell in cells:
        r, c = cell
        val = grid[r][c]
        
        if val == 0:
            prob.addVariable(cell, range(1, 10))
        else:
            prob.addVariable(cell, [val])

    for i in range(9):
        prob.addConstraint(AllDifferentConstraint(), [(i, j) for j in range(9)])
        prob.addConstraint(AllDifferentConstraint(), [(j, i) for j in range(9)])

    for box_r in range(3):
        for box_c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append((3 * box_r + i, 3 * box_c + j))
            prob.addConstraint(AllDifferentConstraint(), block)

    sol = prob.getSolution()
    
    if not sol:
        return None

    solved = [[0] * 9 for _ in range(9)]
    for (r, c), val in sol.items():
        solved[r][c] = val
        
    return solved

def bench_solvers(grids):
    csp_res = []
    lib_res = []
    bf_res = []
    
    t1 = time.time()
    for grid_str in grids:
        grid = grid_from_str(grid_str)
        csp_grid = copy.deepcopy(grid)
        csp_res.append(solve_grid(csp_grid))
    csp_time = time.time() - t1
    
    t1 = time.time()
    for grid_str in grids:
        grid = grid_from_str(grid_str)
        simple_solver(grid)
    bf_time = time.time() - t1

    t1 = time.time()
    for grid_str in grids:
        grid = grid_from_str(grid_str)
        lib_solver(grid)
    lib_time = time.time() - t1

    print("=== Performance Results ===")
    print("\nCSP Solver:")
    print("Time: {:.6f}s".format(csp_time))

    print("\nSimple Backtracking:")
    print("Time: {:.6f}s".format(bf_time))

    print("\nLibrary Solver:")
    print("Time: {:.6f}s".format(lib_time))

in_file = "sudoku_puzzle.txt"
out_file = "sudoku_output.txt"
process_file(in_file, out_file)

grids = load_grid("sudoku_puzzle.txt")
bench_solvers(grids)
