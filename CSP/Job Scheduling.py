
# ========================= Job Scheduling =========================

import random
import math

num_staff = 5
num_shift = 21
max_shift_per_staff = 7
required_staff = 2
population_size = 10
mutation_rate = 0.1
max_generations = 10

# 1: Initialize Population
def create_random_schedule():
    schedule = [[0] * num_shift for _ in range(num_staff)]
    for staff in range(num_staff):
        assigned_shifts = random.sample(range(num_shift), random.randint(3, max_shift_per_staff))
        for shift in assigned_shifts:
            schedule[staff][shift] = 1

    return schedule

# 2: Fitness Function
def fitness(schedule):
    penalty = 0

    # Check for under-staffed shifts
    for shift in range(num_shift):
        assigned_count = sum(schedule[staff][shift] for staff in range(num_staff))
        if assigned_count < required_staff:
            penalty += (required_staff - assigned_count) * 10

    # Check consecutive shifts and max shifts per staff
    for staff in range(num_staff):
        # Penalize consecutive shifts
        for shift in range(num_shift - 1):
            if schedule[staff][shift] == 1 and schedule[staff][shift + 1] == 1:
                penalty += 5
        
        # Penalize exceeding max shifts per staff
        staff_shifts = sum(schedule[staff])
        if staff_shifts > max_shift_per_staff:
            penalty += (staff_shifts - max_shift_per_staff) * 15
            
    return penalty

# 3: Selection
def select_parents(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
    return sorted_population[:len(population) // 2]


# 4: Crossover
def crossover(parent1, parent2):
    point = random.randint(0, num_shift - 1)
    child = [parent1[i][:point] + parent2[i][point:] for i in range(num_staff)]
    return child

# 5: Mutation
def mutate(schedule):
    staff = random.randint(0, num_staff - 1)
    shift1, shift2 = random.sample(range(num_shift), 2)
    schedule[staff][shift1], schedule[staff][shift2] = schedule[staff][shift2], schedule[staff][shift1]
    return schedule

# Convergence Criteria
population = [create_random_schedule() for _ in range(population_size)]
best_fitness = float('inf')

for generation in range(max_generations):
    fitness_scores = [fitness(schedule) for schedule in population]
    print(f"Generation {generation + 1}: Best Fitness = {min(fitness_scores)}")

    parents = select_parents(population, fitness_scores)
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            child = mutate(child)
        new_population.append(child)

    population = new_population

# Calculate fitness for final population
final_fitness_scores = [fitness(schedule) for schedule in population]
best_schedule = population[final_fitness_scores.index(min(final_fitness_scores))]

print("\nBest Schedule (staff (x) shifts):")
for staff in range(num_staff):
    print(f"Staff {staff + 1}: {best_schedule[staff]}")

