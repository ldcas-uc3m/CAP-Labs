import os                                                                       
import multiprocessing as mp

processes = ('ex2/script1.py', 'ex2/script2.py', 'ex2/script3.py', 'exercise1.py')                      

def run_python(process):                                                             
    os.system('python {}'.format(process))                                      

if __name__ == "__main__":
    pool = mp.Pool(processes=4)     
                                                   
    pool.map(run_python, processes) 
