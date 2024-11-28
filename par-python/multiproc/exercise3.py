import multiprocessing as mp

list_a = [[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]]

def normalize(mylist):
    mini = min(mylist)
    maxi = max(mylist)
    print(mp.current_process())
    return [(i - mini)/(maxi-mini) for i in mylist]

if __name__ == "__main__":
    #pool = mp.Pool(mp.cpu_count())
    pool = mp.Pool(4)

    results = [pool.apply(normalize, args=(l1, )) for l1 in list_a]

    pool.close()    

    print(results[:10])

