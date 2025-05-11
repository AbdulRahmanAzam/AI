import random
import numpy as np

jobs = [5, 8, 4, 7, 6, 3, 9]  
mach_cap = [24, 30, 28]  
costs = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

pop = 6
xover = 0.8
mut = 0.2
gens = 50

def make_pop():
    return [[random.randint(1, 3) for _ in range(len(jobs))] for _ in range(pop)]

def eval_sol(s):
    cost = 0
    loads = [0, 0, 0]
    
    for i, m in enumerate(s):
        m_idx = m - 1
        loads[m_idx] += jobs[i]
        cost += jobs[i] * costs[i][m_idx]
    
    for i, load in enumerate(loads):
        if load > mach_cap[i]:
            cost += (load - mach_cap[i]) * 100
    
    return -cost

def select_sol(sols):
    fits = [eval_sol(s) for s in sols]
    min_fit = min(fits)
    adj = [f - min_fit + 1 for f in fits]
    total = sum(adj)
    probs = [f/total for f in adj]
    return sols[np.random.choice(len(sols), p=probs)]

def crossover(p1, p2):
    if random.random() < xover:
        cut = random.randint(1, len(jobs) - 1)
        return p1[:cut] + p2[cut:], p2[:cut] + p1[cut:]
    return p1.copy(), p2.copy()

def mutate(s):
    if random.random() < mut:
        i, j = random.sample(range(len(jobs)), 2)
        s[i], s[j] = s[j], s[i]
    return s

def run_ga():
    sols = make_pop()
    
    for _ in range(gens):
        new_sols = []
        while len(new_sols) < pop:
            p1 = select_sol(sols)
            p2 = select_sol(sols)
            kid1, kid2 = crossover(p1, p2)
            new_sols.append(mutate(kid1))
            if len(new_sols) < pop:
                new_sols.append(mutate(kid2))
        sols = new_sols
    
    best = max(sols, key=eval_sol)
    return best, -eval_sol(best)

result, cost = run_ga()
print("Assignment:", result)
print("Cost:", cost)
