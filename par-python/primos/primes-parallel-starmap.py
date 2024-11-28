import multiprocessing as mp
import time
 
def prime(prime_numbers, start, stop):
    print("Range: {}-{}".format(start, stop))
    for num in range(start, stop+1):
        is_prime=True
        for div in range(2, num):
            if num%div == 0:
                is_prime=False
                break
        if is_prime:
            prime_numbers.append(num)
    return(prime_numbers)
 
if __name__ == '__main__':
    start_time = time.time()
 
# Step 1: Init multiprocessing.Pool() 
    pool = mp.Pool(10) 
    chunk = 20000
    result = []
    prime_numbers = []
    data = [(prime_numbers,0, 20000), (prime_numbers,20000, 40000),
            (prime_numbers,40000, 60000), (prime_numbers,60000, 80000),
            (prime_numbers,80000, 100000), (prime_numbers,100000, 120000),
            (prime_numbers,1200000, 140000), (prime_numbers,140000, 160000),
            (prime_numbers,1600000, 180000), (prime_numbers,180000, 200000)]

    result=[pool.starmap(prime, data)]

    pool.close()
    
 
    print(len(result))
    print("Total Time: {}".format(time.time()-start_time))

