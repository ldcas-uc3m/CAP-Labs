# threads and locks usage example
import sys
from _thread import start_new_thread, allocate_lock

num_threads = 0

thread_started = False

lock = allocate_lock()

def testglobal(val):
    global num_threads, thread_started
    lock.acquire()
    num_threads += 1
    thread_started = True
    lock.release()
    print ("\n Num threads= ", num_threads)
    lock.acquire()
    num_threads -= 1
    lock.release()

if __name__ == "__main__":

    MAX_THREADS = int(sys.argv[1])

    for i in range(MAX_THREADS):
        start_new_thread(testglobal,(i,))

    while not thread_started:
        pass
    while num_threads > 0:
        pass

