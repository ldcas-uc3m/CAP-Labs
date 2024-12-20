# Solution With Parallelization using Pool.apply

import numpy as np 
from time import time 
import multiprocessing as mp


# Function to look for in range 
def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within maximum and minimum in a given row"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
             count = count + 1
    return count


if __name__ == "__main__":

    # Prepare data 
    np.random.RandomState(100) 
    arr = np.random.randint(0, 10, size=[20000, 5]) 
    data = arr.tolist() 
    data[:5]

    # Step 1: Init multiprocessing.Pool() 
    #pool = mp.Pool(mp.cpu_count())

    print("CPUs:",mp.cpu_count()) 
    pool = mp.Pool(mp.cpu_count())

    results = []
    # Step 2: `pool.apply` the `howmany_within_range()`
    results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data] 

    # Step 3: Don't forget to close 
    pool.close() 

    print(results[:10])


