import multiprocessing as mp
import random
import string
from time import time

random.seed(123)

start = time()

# Define an output queue
output = mp.Queue()

# define a example function
def rand_string(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.digits)
                   for i in range(length))
    output.put(rand_str)

if __name__ == "__main__":

    # Setup a list of processes that we want to run
    processes = [mp.Process(target=rand_string, args=(9, output)) for x in range(8)]

    #processes = [] 
    #for x in range(1000):
    #    processes.append(mp.Process(target=rand_string, args=(9, output))) 
    #    processes[x].start()

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()

    # Get process results from the output queue
    results = [output.get() for p in processes]

    # Get results ordered
    results.sort()
    results = [r[1] for r in results]

    end = time()
    print(results)
    print(end-start)
