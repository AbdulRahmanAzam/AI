# THERE IS THE COMMENTED CODE BELOW, TO LEARN ABOUT IT
# THE CODE WITHOUT COMMENT IS ALSO WRITTEN BELOW THIS CODE
# ========================= Job Scheduling =========================


# ========================= Job Scheduling =========================
# This code implements a genetic algorithm to solve a staff scheduling problem

import random
import math

# Problem parameters
num_staff = 5                # Number of staff members available
num_shift = 21               # Total number of shifts to be covered
max_shift_per_staff = 7      # Maximum number of shifts any staff member can work
required_staff = 2           # Minimum number of staff required for each shift

# Genetic algorithm parameters
population_size = 10         # Number of schedules in each generation
mutation_rate = 0.1          # Probability of mutation (10%)
max_generations = 10         # Maximum number of generations to evolve

# 1: Initialize Population
# Creates a random valid schedule where each staff works between 3 and max_shift_per_staff shifts
def create_random_schedule():
    # Create a schedule with all zeros (no shifts assigned)
    # Format: schedule[staff_member][shift_number] = 1 if staff works that shift, 0 otherwise
    schedule = [[0] * num_shift for _ in range(num_staff)]
    
    # For each staff member, randomly assign between 3 and max_shift_per_staff shifts
    for staff in range(num_staff):
        # Randomly select shifts without replacement
        assigned_shifts = random.sample(range(num_shift), random.randint(3, max_shift_per_staff))
        # Mark the assigned shifts with 1
        for shift in assigned_shifts:
            schedule[staff][shift] = 1

    return schedule

# 2: Fitness Function
# Evaluates how good a schedule is by calculating penalties for constraint violations
# Lower fitness value = better schedule (fewer violations)
def fitness(schedule):
    penalty = 0

    # Check for under-staffed shifts (each shift needs at least required_staff members)
    for shift in range(num_shift):
        # Count staff assigned to this shift
        assigned_count = sum(schedule[staff][shift] for staff in range(num_staff))
        # Penalize if fewer than required staff are assigned
        if assigned_count < required_staff:
            penalty += (required_staff - assigned_count) * 10  # Weight: 10 per missing staff

    # Check constraints for each staff member
    for staff in range(num_staff):
        # Penalize consecutive shifts (staff shouldn't work back-to-back shifts)
        for shift in range(num_shift - 1):
            if schedule[staff][shift] == 1 and schedule[staff][shift + 1] == 1:
                penalty += 5  # Weight: 5 per consecutive shift
        
        # Penalize exceeding max shifts per staff
        staff_shifts = sum(schedule[staff])  # Count total shifts for this staff
        if staff_shifts > max_shift_per_staff:
            penalty += (staff_shifts - max_shift_per_staff) * 15  # Weight: 15 per excess shift
            
    return penalty

# 3: Selection
# Selects the best half of the population to become parents for the next generation
def select_parents(population, fitness_scores):
    # Sort population by fitness scores (lower is better)
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
    # Return the best half of the population
    return sorted_population[:len(population) // 2]

# 4: Crossover
# Creates a new schedule by combining parts of two parent schedules
def crossover(parent1, parent2):
    # Select a random crossover point along the shift dimension
    point = random.randint(0, num_shift - 1)
    # For each staff, take shifts before crossover point from parent1 and after from parent2
    child = [parent1[i][:point] + parent2[i][point:] for i in range(num_staff)]
    return child

# 5: Mutation
# Randomly alters a schedule by swapping two shifts for a random staff member
def mutate(schedule):
    # Select a random staff member
    staff = random.randint(0, num_staff - 1)
    # Select two random shifts to swap
    shift1, shift2 = random.sample(range(num_shift), 2)
    # Swap the values (0→1 or 1→0) for these shifts
    schedule[staff][shift1], schedule[staff][shift2] = schedule[staff][shift2], schedule[staff][shift1]
    return schedule

# Main genetic algorithm loop
# Generate initial population
population = [create_random_schedule() for _ in range(population_size)]
best_fitness = float('inf')  # Initialize best fitness to infinity

# Evolution process - repeat for max_generations
for generation in range(max_generations):
    # Calculate fitness for each schedule in the population
    fitness_scores = [fitness(schedule) for schedule in population]
    print(f"Generation {generation + 1}: Best Fitness = {min(fitness_scores)}")

    # Select the best individuals as parents
    parents = select_parents(population, fitness_scores)
    
    # Create a new population through crossover and mutation
    new_population = []
    while len(new_population) < population_size:
        # Select two random parents for each child
        parent1, parent2 = random.sample(parents, 2)
        # Create child through crossover
        child = crossover(parent1, parent2)
        # Apply mutation with probability mutation_rate
        if random.random() < mutation_rate:
            child = mutate(child)
        # Add child to new population
        new_population.append(child)

    # Replace old population with new population
    population = new_population

# Calculate fitness for final population
final_fitness_scores = [fitness(schedule) for schedule in population]
# Find the best schedule in the final population
best_schedule = population[final_fitness_scores.index(min(final_fitness_scores))]

# Display the best schedule found
print("\nBest Schedule (staff (x) shifts):")
for staff in range(num_staff):
    print(f"Staff {staff + 1}: {best_schedule[staff]}")






















# ======================================== WITHOUT COMMENT ============================
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

