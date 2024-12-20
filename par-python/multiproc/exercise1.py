#!/usr/bin/python3

import multiprocessing as mp
from time import time

t0 = time()

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

def get_commons(list_1, list_2):
    return list(set(list_1).intersection(list_2))

if __name__ == "__main__":

    pool = mp.Pool(mp.cpu_count())

    print("Num CPUS = ",  mp.cpu_count())

    results = []

    results = [pool.apply(get_commons, args=(l1, l2)) for l1, l2 in zip(list_a, list_b)]

    pool.close()

    print(results[:10])

    t1 = time()

    print("Tiempo: ", str(t1 - t0))
