from mpi4py import MPI
import random
import numpy as np
    
#MPI Parallelization
comm = MPI.COMM_WORLD # gets communication pool 
rank = comm.Get_rank()  # gets rank of current process 
num_ranks = comm.Get_size() # total number of processes
 
r = np.random.randint(0, 100, 10)
rmin = np.empty(10, dtype=int)
rmax = np.empty(10, dtype=int)
    
print("Rank " + str(rank) + ": " + str(r))
  
comm.Barrier()

comm.Allreduce([r, MPI.INT], [rmin, MPI.INT], op=MPI.MIN)
comm.Allreduce([r, MPI.INT], [rmax, MPI.INT], op=MPI.MAX)

#comm.Barrier()
   
if rank == 0:
    print("Allreduce MIN: " + str(rmin))
    print("Allreduce MAX: " + str(rmax))

if rank == 1:
    print("Allreduce MIN: " + str(rmin))
    print("Allreduce MAX: " + str(rmax))
