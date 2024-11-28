## Count how many numbers exist between a given range in each row 
# Serial version

import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]

# Solution Without Parallelization
def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within maximum and minimum in a given row""" 
    count = 0
    for n in row:
        if minimum <= n <= maximum:
             count = count + 1
    return count

results = []
for row in data:
    results.append(howmany_within_range(row, minimum=4, maximum=8))

print(results[:10])

