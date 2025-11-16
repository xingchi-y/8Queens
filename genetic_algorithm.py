import random

from utils import count_attacking_pairs, generate_population

N_QUEENS = 8
MUTATION_RATE = 0.2

# calculate how many pairs attacking each other
def fitness_function(individual):
    total_attacks = count_attacking_pairs(individual)
    max_attacking_pairs = N_QUEENS * (N_QUEENS - 1) / 2
    return max_attacking_pairs - total_attacks

def get_fitness_values(population):
    fitness_values = []
    for individual in population:
        fitness_values.append(fitness_function(individual))
    return fitness_values

def get_probabilities(fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return probabilities

# Randomly select pairs of parents to breed
def select_parent(population, probabilities):
    # roulette wheel selection
    r = random.random()
    cumulative = 0

    for individual, p in zip(population, probabilities):
        cumulative += p
        if r <= cumulative:
            return individual

    # fallback: return last individual (never None)
    return population[-1]

# Crossover (Single-point crossover)
def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n-2)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2

def mutate(individual):
    if random.random() < MUTATION_RATE:
        # start to mutate
        col = random.randint(0, N_QUEENS-1)
        individual[col] = random.randint(0, N_QUEENS-1)
    return individual

def ga(population_size, generations):
    # step 1: creating random members of the population
    population = generate_population(population_size, N_QUEENS)

    best_solution = None
    best_fitness = 0
    average_fitness = 0

    # for 8-queens is 28
    max_fitness = N_QUEENS * (N_QUEENS - 1) / 2

    for gen in range(generations):
        # compute the fitness
        fitness_values = [fitness_function(ind) for ind in population]

        gen_best = max(fitness_values)
        # update global best
        if gen_best > best_fitness:
            best_fitness = gen_best
            best_solution = population[fitness_values.index(gen_best)]

        average_fitness = sum(fitness_values) / len(fitness_values)

        if best_fitness == max_fitness:
            print(f"Solution found at generation {gen}")
            break

        probabilities = get_probabilities(fitness_values)

        new_population = []
        while len(new_population) < population_size:
            # select parents
            p1 = select_parent(population, probabilities)
            p2 = select_parent(population, probabilities)

            # crossover
            c1, c2 = crossover(p1, p2)

            # mutation
            c1 = mutate(c1)
            c2 = mutate(c2)

            new_population.append(c1)
            if len(new_population) < population_size:
                new_population.append(c2)

        # full replacement
        population = new_population

    return best_solution, best_fitness, average_fitness


