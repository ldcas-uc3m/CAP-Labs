# Solution With Parallelization using Pool.map

import numpy as np 
from time import time 

# Step 1: Init multiprocessing.Pool() 
import multiprocessing as mp


# Function to look for in range
def howmany_within_range2(i, row, minimum, maximum):
    """Returns how many numbers lie within maximum and minimum in a given row"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count) 

# Step2: callback function to collect the ouput in results
def collect_result (result):
    global results
    results.append(result)

if __name__ == "__main__":

    # Prepare data 
    np.random.RandomState(100) 
    arr = np.random.randint(0, 10, size=[2000, 5]) 
    data = arr.tolist() 
    data[:5]

    print("CPUs:",mp.cpu_count()) 
    #pool = mp.Pool(4)
    results = []

    pool = mp.Pool(mp.cpu_count())

    # Step 3: Use loop to parallelize
    for i, row in enumerate(data):
        pool.apply_async(howmany_within_range2, args=(i, row, 4, 8), callback=collect_result) 

    # postpones the execution of next line of code until all processes in the queue are done.
    pool.close()

    # Step 4: Close loop and let the processes run
    pool.join()

    # Step 5: Sort results [OPTIONAL] 
    results.sort(key=lambda x: x[0]) 
    results_final = [r for i, r in results]

    print(results_final[:10])


