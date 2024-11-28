#!/usr/bin/env python3

import threading as th
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

    threads = []
    prime_numbers = []
    start = 1
    stop = 20000
    for i in range(10):
        thread = th.Thread(
            target=prime,
            args=(i*2000, i*2000+2000, prime_numbers,)
        )
        threads.append(thread)

    for thread  in threads:
        thread.start()
    for thread  in threads:
        thread.join()

    print(len(prime_numbers))
    print("Total Time: {}".format(time.time()-start_time))

