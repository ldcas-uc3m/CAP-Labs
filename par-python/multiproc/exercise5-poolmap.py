# Solution With Parallelization using Pool.map

import numpy as np 
from time import time 
import multiprocessing as mp

# Function to look for in range 
def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    """Returns how many numbers lie within maximum and minimum in a given row"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
             count = count + 1
    return count

if __name__ == "__main__":
    # Step 1: Init multiprocessing.Pool() 
    # Prepare data 
    np.random.RandomState(100) 
    arr = np.random.randint(0, 10, size=[200000, 5]) 
    data = arr.tolist() 
    data[:5]

    print("CPUs:",mp.cpu_count()) 
    pool = mp.Pool(mp.cpu_count())

    results = []
    # Step 2: `pool.map' the `howmany_within_range()
    results = pool.map(howmany_within_range_rowonly, [row for row in data])

    # Step 3: Don't forget to close 
    pool.close() 

    print(results[:10])


