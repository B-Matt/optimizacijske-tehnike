import time
import random
import numpy as np

import algorithms.optimal_knapsack
import algorithms.greedy_knapsack
import algorithms.optimized_dantzing

# Variables
random_values = [1, 100]
random_weights = [1, 100]

# Functions
def generate_random_items(rand_values, rand_weights, len=10):
    items = []
    for i in range(len):
        items.append(
            (random.randint(rand_values[0], rand_values[1]), random.randint(rand_weights[0], rand_weights[1]))
        )

    capacity = 25 #random.randint(5, 100)
    return items, capacity

def solve_given_knapsack(items, capacity, verbose=False):
    optimal_start = time.process_time_ns()
    total_value = algorithms.optimal_knapsack.solve_knapsack(items, capacity)
    optimal_end = time.process_time_ns()
    
    greedy_start = time.process_time_ns()
    greedy_knapsack, greedy_value, greedy_weight = algorithms.greedy_knapsack.solve_knapsack(items, capacity)
    greedy_end = time.process_time_ns()

    start_optimized = time.process_time_ns()
    optimized_knapsack, optimized_value, optimized_weight = algorithms.optimized_dantzing.solve_knapsack(items, capacity)
    end_optimized = time.process_time_ns()

    # Verbose Results
    if verbose:
        print('-----------------[INFO]-----------------')
        print(f'Items: {items}')
        print(f'Knapsack capacity: {capacity}')

        # print('\n-----------------[OPTIMAL]-----------------')
        # print(f'Total value: {total_value}')

        print('\n-----------------[DANTZING]-----------------')
        print(f'Knapsack contents: {greedy_knapsack}')
        print(f'Total value: {greedy_value}')
        print(f'Total weight: {greedy_weight}')

        print('\n-----------------[OPTIMIZED DANTZING]-----------------')
        print(f'Knapsack contents: {optimized_knapsack}')
        print(f'Total value: {optimized_value}')
        print(f'Total weight: {optimized_weight}')

    return greedy_value < optimized_value, (optimal_end - optimal_start), (greedy_end - greedy_start), (end_optimized - start_optimized)

# Setup
run_iterations = 10000
better_cnt = 0

optimal_timings = []
greedy_timings = []
optimized_timings = []

for i in range(run_iterations):
    items, capacity = generate_random_items(random_values, random_weights, 25)
    was_optimized_better, optimal_timing, greedy_timing, optimized_timing = solve_given_knapsack(items, capacity)

    optimal_timings.append(optimal_timing)
    greedy_timings.append(greedy_timing)
    optimized_timings.append(optimized_timing)

    if was_optimized_better:
        better_cnt += 1

print('-----------------[RUN STATS]-----------------')
print(f'Run iterations: {run_iterations}')
print(f'Iterations in which optimized algorithm was better: {(better_cnt / run_iterations) * 100}%')
print(f"Optimal time: {np.mean(optimal_timings)}ns")
print(f"Greedy time: {np.mean(greedy_timings)}ns")
print(f"Optimized time: {np.mean(optimized_timings)}ns")