import random
p_cnt = 10
c_cnt = 10
max_gen = 100
mut_rate = 0.2
# Generate Poplation

def generate():
    cities = list(range(c_cnt))
    population = [random.sample(cities, len(cities)) for _ in range(p_cnt)]
    return population

print(generate())

# fitness Function

dist_matrix = [
    [ 0, 29, 20, 21, 16, 31, 100, 12,  4, 31], 
    [29,  0, 15, 29, 28, 40, 72, 21, 29, 41], 
    [20, 15,  0, 15, 14, 25, 81,  9, 23, 27], 
    [21, 29, 15,  0,  4, 12, 92, 12, 25, 13], 
    [16, 28, 14,  4,  0, 16, 94,  9, 20, 16], 
    [31, 40, 25, 12, 16,  0, 95, 24, 36,  3], 
    [100,72, 81, 92, 94, 95,  0, 90, 101,99], 
    [12, 21,  9, 12,  9, 24, 90,  0, 15, 25], 
    [4,  29, 23, 25, 20, 36, 101, 15,  0, 35], 
    [31, 41, 27, 13, 16, 3,  99, 25, 35,  0]
]

def Fitness_Function(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += dist_matrix[route[i]][route[i + 1]]
    total_distance += dist_matrix[route[-1]][route[0]]  
    return 1/total_distance
#Select Parents

def select(population,fitnessvalues):
    sortedpop = [route for route,_ in sorted(zip(population,fitnessvalues))]
    return sortedpop[:len(sortedpop)//2]
# Order Crossover (OX)
def crossover(p1, p2):
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = p1[start:end]
    remaining = [gene for gene in p2 if gene not in child]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = remaining[idx]
            idx += 1
    return child
# Mutate

def mutate(route):
    i,j = random.sample(range(c_cnt),2)
    route[i],route[j] = route[j],route[i]
    return route
    
# Main Genetic Algorithm
population = generate()
gen = 0

while gen < max_gen:
    fitness_scores = [Fitness_Function(ind) for ind in population]
    best_distance = 1 / max(fitness_scores)  # Convert back to distance
    print(f"Generation {gen} Best Distance: {best_distance}")
    
    parents = select(population, fitness_scores)
    newpop = []

    for _ in range(p_cnt):
        p1, p2 = random.sample(parents, 2)
        child = crossover(p1, p2)
        if random.random() < mut_rate:
            child = mutate(child)
        newpop.append(child)
    
    population = newpop
    gen += 1

# Get Best Route After Last Generation
fitness_scores = [Fitness_Function(ind) for ind in population]
best_route = min(population, key=Fitness_Function)
best_distance = 1 / Fitness_Function(best_route)
print("Best Route:", best_route)
print("Best Distance:", best_distance)
