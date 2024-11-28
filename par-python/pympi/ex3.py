# Asynchronous Communication example.  Master - slave model
# execute with:   mpiexec -n nprocs python  exercise3.py

from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    for i in range(1, size):
       data = i * 3
       comm.isend(data, dest=i, tag=11)
       #print("Sending to: ", i)
    else:
        print("Sending finished!")
else:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print('rank ', rank, 'val =', data, 'sqr = ', math.sqrt(data))
    

