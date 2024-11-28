
# Communication example.  Master - slave model
# execute with:   mpiexec -n nprocs python  exercise2.py

from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    for i in range(1, size):
       comm.send(i*3, dest=i, tag=11)
       print("Sending to: ", i)
    else:
        print("Sending finished!")
else:
    val = comm.recv(source=0, tag=11)
    print('rank ', rank, 'val =', val, 'sqr = ', math.sqrt(val))

