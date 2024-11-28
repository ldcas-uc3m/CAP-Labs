#thread creation test

import threading, random

def countdown():
     y = 1000000
     x = ( random.random() * y ) % y
     print ("Thread: bucle ", x)
     while x > 0:
         x -= 1
     return x

if __name__ == "__main__":

    # Implementation withMulti-threading
    thread_1 = threading.Thread(target=countdown)
    thread_2 = threading.Thread(target=countdown)

    print ("Threads creados")

    thread_1.start()
    thread_2.start()

    print ("Threads arrancados")

    thread_1.join()
    thread_2.join()

    print ("Threads terminados")
