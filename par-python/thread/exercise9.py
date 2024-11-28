#thread creation test and attributes

import threading
from time import time

start = time()

def countdown(val):
     x = val 
     while x > 0:
         x -= 1
     print('thread id:', threading.current_thread().getName(), 'val:', val)

# Implementation withMulti-threading
NUM_THREADS = 30

th = []

for num_thread in range(NUM_THREADS):
    th.append(threading.Thread(name='th%s' %num_thread, target = countdown, args=(10*num_thread,))   ) 
#    th.start()

for i in range(NUM_THREADS):
    th[i].start()
print ("Threads arrancados")


for i in range(NUM_THREADS):
    th[i].join()
print ("Threads terminados")
end = time()
print ("Time ", end-start)
