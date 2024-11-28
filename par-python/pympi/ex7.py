# Scatter Gather with Numpy

from mpi4py import MPI
import numpy as np
# importing functools for reduce() 
import functools
import operator 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Scatter
sendbuf = None

if rank == 0:
    sendbuf = np.empty([size, 10], dtype='i')
    sendbuf.T[:,:] = range(size)

recvbuf = np.empty(10, dtype='i')

comm.Scatter(sendbuf, recvbuf, root=0)
assert np.allclose(recvbuf, rank)
print ("Data in rank ", rank, recvbuf)

# Gather

sendbuf = np.zeros(10, dtype='i') + rank
recvbuf = None
if rank == 0:
    recvbuf = np.empty([size, 10], dtype='i')

comm.Gather(sendbuf, recvbuf, root=0)

if rank == 0:
    print ("rank 0 ")
    for i in range(size):
        assert np.allclose(recvbuf[i,:], i)
        print (recvbuf[i,:])

    # using reduce to compute product 
    print ("The sum of gathered list of elements is : ") 
    print (functools.reduce(operator.add,recvbuf))


