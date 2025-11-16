

from genetic_algorithm import ga
from utils import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    results = {}

    for pop_size in pop_size_arr:
        results[pop_size] = []
        for generations in generation_arr:
            # print("-------- pop_size = {}, generation = {} ----------".format(pop_size, generations))
            best_solution, best_fitness, average_fitness = ga(pop_size, generations)

            results[pop_size].append([generations, best_fitness, average_fitness])

            # print("Best solution:", best_solution)
            # print("Best fitness:", best_fitness)
            # print("\n")

    for pop_size, data_list in results.items():
        plot_for_pop_size(pop_size, data_list)


