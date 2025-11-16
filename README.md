## Using Genetic Algorithm (GA) to solve the 8-Queens problem

### Requirements
Python 3.13 (recommended)

No external dependencies except: matplotlib (for plotting fitness curves)

```pip install matplotlib```

### Running the Project
```python main.py```

### GA Parameters
(1)N_QUEENS = 8: 8-Queens problem.

(2)MUTATION_RATE = 0.2: If the random probability is greater than MUTATION_RATE, then a mutation operation is performed.

(3)Pop_size_arr = [10, 100, 500, 1000]: Initial population size.

(4)Generation_arr = [200, 400, 600, 800, 1000]: Number of iterations to generate offspring

### GA Functions
(1)Generate Population Function
Randomly generate a population of a specified quantity. Each individual in the population is encoded as a list of length 8, each row value ranges from 0 to 7, like this: 
		
```[1, 6, 4, 7, 5, 0, 3, 6]```
    
(2)Fitness Function
There are C(8, 2) = 28 possible pairs of queens. We can calculate the actual attacking pairs.
  
```fitness = 28 – actual_attacking_pairs```

(3)Selection of Parents
		I implemented roulette wheel selection using normalized fitness:
			
		This ensures fitter individuals are more likely to be chosen as parents.
    
(4)Crossover
		I used single-point crossover, select a random crossover point k, swap genetic material to create two children
    
(5)Mutation

```MutationPct = 0.2```
