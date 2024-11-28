# Write a multithreaded implementation for a code that sequentially adds 
# numbers to lists

import random
import threading
import time 

def list_append(count, id, out_list):
    """
    Creates an empty list and then appends a
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    for i in range(count):
        out_list.append(random.random())

if __name__ == "__main__":
    st = time.time()
    size = 1000000
    # Number of random numbers to add
    threads = 16
    # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list
    out_list = list()
    jobs = []
    for i in range(0, threads):
        thread = threading.Thread(target=list_append(size//threads, i, out_list))
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

        et = time.time()
        tt = et - st
    print ("List processing complete. time = ", tt, "sec for elements = ", len(out_list))


