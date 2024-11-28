#!/usr/bin/env python3

import multiprocessing
import time

def prime(start, stop, prime_numbers):
    print("Range: {}-{}".format(start, stop))
    for num in range(start, stop+1):
        is_prime=True
        for div in range(2, num):
            if num%div == 0:
                is_prime=False
                break
        if is_prime:
            prime_numbers.append(num)

if __name__ == '__main__':
    start_time = time.time()

    processes = []
    chunk = 20000
    manager = multiprocessing.Manager()
    prime_numbers = manager.list()

    for i in range(10):
        process = multiprocessing.Process(
            target=prime,
            args=(i*chunk, i*chunk+chunk, prime_numbers,)
        )
        processes.append(process)

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    print(len(prime_numbers))
    print("Total Time: {}".format(time.time()-start_time))

