# Counting finished works

import random, time, multiprocessing
 
def func(arg):
    print ('%s says %s',multiprocessing.current_process(), arg)
    time.sleep( random.uniform(0, 0.5) )
    return arg

if __name__ == "__main__":
    start = time.time()

    p = multiprocessing.Pool(multiprocessing.cpu_count())


    result1 = p.map_async( func, range(10,190) )
    result2 = p.map_async( func, range(200,290) )
    result3 = p.map_async( func, range(300,390) )
 
    print ("Waiting for results")
 
    p.close()
    p.join()

    end = time.time()

    print (result1.get())
    print (result2.get())
    print (result3.get())

    print ("Time = ", end-start)
