import random
from collections import defaultdict
from matplotlib import pyplot as plt

pop_size_arr = [10, 100, 500, 1000]
generation_arr = [200, 400, 600, 800, 1000]

def generate_population(pop_size, n_queens):
    population = []
    for _ in range(pop_size):
        # generate random chromosome
        chromosome = [random.randint(0, n_queens-1) for _ in range(n_queens)]
        population.append(chromosome)
    return population

def count_attacking_pairs(individual):
    n = len(individual)

    row_count = defaultdict(int)
    major_diag = defaultdict(int)  # row - col
    minor_diag = defaultdict(int)  # row + col

    # Count queens on same row or same diagonals
    for col in range(n):
        row = individual[col]
        row_count[row] += 1
        major_diag[row - col] += 1
        minor_diag[row + col] += 1

    total_attacks = 0
    for d in (row_count, major_diag, minor_diag):
        for k in d.values():
            if k > 1:
                total_attacks += combinations(k)

    return total_attacks

def combinations(k):
    return k * (k - 1) // 2

def plot_for_pop_size(pop_size, data_list):
    """
    pop_size: e.g., 100
    data_list: list of [generations, best_fitness, avg_fitness]
    """
    # Extract values
    generations = [item[0] for item in data_list]  # X axis
    best_fitness = [item[1] for item in data_list]  # red line
    avg_fitness = [item[2] for item in data_list]  # blue line

    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(generations, best_fitness, color='red', label='Best Fitness')
    plt.plot(generations, avg_fitness, color='blue', label='Average Fitness')

    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.title(f"GA Performance - Population Size = {pop_size}")
    plt.legend()
    plt.grid(True)

    plt.show()