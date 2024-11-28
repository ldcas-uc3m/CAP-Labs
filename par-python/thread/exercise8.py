#thread creation test and attributes

import threading, random, decimal

# By default rounding setting in python is decimal.ROUND_HALF_EVEN
decimal.getcontext().rounding = decimal.ROUND_DOWN

def countdown():
     y = decimal.Decimal( random.random() * 1000 )
     y = round(y,0)
     x = y
     while x > 0:
         x -= 1
     print('thread id:', threading.current_thread().getName(),'with ident:', threading.current_thread().ident, 'y:', y)

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
