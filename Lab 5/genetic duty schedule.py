import random

num_staff = 5
num_shifts = 21
max_shifts_per_staff = 7
required_staff_per_shift = 2
population_size = 10
mutation_rate = 0.1
max_generations = 1000


# fitness functoin (lower is better)
def evaluate_fitness(schedule):
    penalty = 0

    for shift in range(num_shifts):
        assigned_count = sum(schedule[staff][shift] for staff in range(num_staff))
        if assigned_count < required_staff_per_shift:
            penalty += (required_staff_per_shift - assigned_count) * 10 # Understaffed penalty
        # Check consecutive shifts for each staff
        for staff in range(num_staff):
            for shift in range(num_shifts - 1):
                if schedule[staff][shift] == 1 and schedule[staff][shift + 1] ==1:
                    penalty += 5 # Penalty for consecutive shifts

        return penalty

# initialize populationn
def create_random_schedule():
    schedule = [[0] * num_shifts for _ in range(num_staff)]
    for staff in range(num_staff):
        assigned_shifts = random.sample(range(num_shifts), random.randint(3,max_shifts_per_staff))
        for shift in assigned_shifts:
            schedule[staff][shift] = 1

    return schedule

# selection
def select_parents(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores,population))]
    return sorted_population[:len(population) // 2]

# crossover
def crossover(parent1, parent2):
    point = random.randint(0, num_shifts - 1)
    child = [parent1[i][:point] + parent2[i][point:] for i in range(num_staff)]
    return child

# mutatoin
def mutate(schedule):
    staff = random.randint(0, num_staff - 1)
    shift1, shift2 = random.sample(range(num_shifts), 2)
    schedule[staff][shift1], schedule[staff][shift2] = schedule[staff][shift2], schedule[staff][shift1]
    return schedule


# convergence crieteria & GA Loop
population = [create_random_schedule() for _ in range(population_size)]

# Genetic Algorithm loop
for generation in range(max_generations):
    fitness_scores = [evaluate_fitness(schedule) for schedule in population]
    best_fitness = min(fitness_scores)
    print(f"quot;Generation {generation + 1}, Best Fitness: {best_fitness}")

    parents = select_parents(population, fitness_scores)
    new_population = []

    while len(new_population) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)

        if random.random() < mutation_rate:
            child = mutate(child)

        new_population.append(child)

    population = new_population
# Best schedule
best_schedule = population[fitness_scores.index(min(fitness_scores))]
print("\nBest Schedule (Staff x Shifts)")

for staff in range(num_staff):
    print("Staff {staff + 1}: {best_schedule[staff]}")
