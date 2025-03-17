import random

# fitness function
n  = 10 # -------------------- CHANGE N ACCORDINGLY
def calculate_fitness(individual):
    non_attacking_pairs = 0
    total_pairs = (n * (n-1) // 2)

    # check for conflicts
    for i in range(n):
        for j in range(i+1, n):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i-j):
                non_attacking_pairs +=1

    return non_attacking_pairs / total_pairs

## population
def create_random_individual():
    return random.sample(range(n), n)

population_size = 10
population = [create_random_individual() for _ in range(population_size)]

## evaluate fitness
fitness_scores = [calculate_fitness(individual) for individual in population]
print("Fitness Score: ", fitness_scores)

## Selection
def select_parents(population, fitness_scores):
    sorted_population = [board for _, board in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population)//2]

parents = select_parents(population, fitness_scores)
print("Selected Parents: ", parents)

## CrossOver
def crossover(parent1, parent2):
    point = random.randint(1, n-2)
    child = parent1[:point] + parent2[point:]

    missing = set(range(n)) - set(child)
    duplicates = [col for col in child if child.count(col) > 1]

    for i in range(len(child)):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()
    
    return child

# create new population using crossover
new_population = []
for i in range(population_size):
    parent1, parent2 = random.sample(parents, 2)
    child = crossover(parent1, parent2)
    new_population.append(child)

print("New population after crossover: ", new_population)

## Mutation
def mutate(individual):
    idx1, idx2 = random.sample(range(n), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

mutation_rate = 0.1
for i in range(len(new_population)):
    if random.random() < mutation_rate:
        new_population[i] = mutate(new_population[i])
print("Population after mutation: ", new_population)


# Check Convergence Criteria
# Genetic Algo main function
def genetic_algorithm():
    population = [create_random_individual() for _ in range(population_size)]
    generation = 0
    best_fitness = 0

    while best_fitness < 1.0 and generation < 100:
        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)
        print(f"Generation {generation} Best Fitness: {best_fitness}")

        if best_fitness == 1.0:
            break
            
        # Crossover
        new_population = [crossover(random.choice(parents), random.choice(parents)) for _ in range(population_size)]

        # Mutation
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])
            
        population = new_population
        generation += 1
    
    best_individual = max(population, key=calculate_fitness)
    return best_individual, calculate_fitness(best_individual)

solution, fitness = genetic_algorithm()
print("Best solutoin: ", solution)
print("Best Fitness: ", fitness)



