
import multiprocessing as mp
import time

chunk = 20000

def prime(start):
    prime_numbers = []
    print("Range: {}-{}".format(start, start+chunk))
    for num in range(start, start+chunk+1):
        is_prime=True
        for div in range(2, num):
            if num%div == 0:
                is_prime=False
                break
        if is_prime:
            prime_numbers.append(num)
    #print(prime_numbers)
    return(prime_numbers)

if __name__ == '__main__':
    start_time = time.time()

    result = []
# Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(10)
    data = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000 ]

    result=[pool.map(prime, data)]

    pool.close()


    print(len(result))
    print("Total Time: {}".format(time.time()-start_time))

