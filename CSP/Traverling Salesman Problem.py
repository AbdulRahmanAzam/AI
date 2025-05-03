

# =============================== Example 1: Traveling Salesman Problem
import random
import math
# 1: Problem and Fitness Function
locations = [(0, 0), (1, 5), (2, 3), (5, 2), (6, 6)]

def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        x1, y1 = locations[route[i]]
        x2, y2 = locations[route[i+1]]

        total_distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Euclidean distance

    return total_distance

# 2: Inititalize Population

def create_random_route():
    route = list(range(len(locations)))
    random.shuffle(route)
    return route

population_size = 10
population = [create_random_route() for _ in range(population_size)]
print("Initialize Population: ", population)

# 3: Fitness
fitness_scores = [calculate_distance(route) for route in population]
print("Fitness Scores: ", fitness_scores)

# 4: Selection
def select_parents(population, fitness_scores):
    sorted_population = [route for _, route in sorted(zip(fitness_scores, population), key=lambda x: x[0])]

    return sorted_population[:len(population)//2]

parents = select_parents(population, fitness_scores)
print("Parents: ", parents)

# 5: Crossover
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end]
    for gene in parent2:
        if gene not in child:
            child.append(gene)
    return child

def new_population(population_size):
    new_population = []
    for _ in range(population_size):
        parent1, parent2 = random.sample(parents, 2)
        new_population.append(crossover(parent1, parent2)) # child crossover
    return new_population
        
print("New Population: ", new_population(population_size))

# 6: Mutation
def mutate(route):
    idx1, idx2 = sorted(random.sample(range(len(route)), 2))
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

def mutate_population(new_population):
    mutation_rate = 0.1
    for i in range(len(new_population)):
        if random.random() < mutation_rate:
            new_population[i] = mutate(new_population[i])
    return new_population

print("Mutated Population: ", mutate_population(new_population(population_size)))

# 7: Evolution
best_fitness = min(fitness_scores)
no_improvement_count = 0
max_generations = 100
generation = 0

while generation < max_generations and no_improvement_count < 10:
    parents = select_parents(population, fitness_scores)
    population = new_population(population_size)
    population = mutate_population(population)
    fitness_scores = [calculate_distance(route) for route in population]


    if min(fitness_scores) < best_fitness:
        best_fitness = min(fitness_scores)
        best_route = population[fitness_scores.index(best_fitness)]
        no_improvement_count = 0
    else:
        no_improvement_count += 1
        
    generation += 1

print("Best Fitness: ", best_fitness)
print("Best Route: ", population[fitness_scores.index(best_fitness)])


