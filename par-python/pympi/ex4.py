
# example.  Collective barrier.   Transmission Numpy arraysi, faster than native types.. 
from mpi4py import MPI
import numpy
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print ('Num procs = ', size)

# passing MPI datatypes explicitly
ts = time.time( )
if rank == 0:
    data = numpy.arange(1000, dtype='i')
    for i in range(1, size):
        comm.Send([data, MPI.INT], dest=i)
    else:
        print ('Sending finished! ')
else:
    data = numpy.empty(1000, dtype='i')
    comm.Recv([data, MPI.INT], source=0)

comm.barrier()
#print (data)

if rank == 0:
    tt = time.time( )
    print ("end of integer array.  Elapsed time = ", tt-ts )
#    print data


# automatic MPI datatype discovery
ts = time.time( )
if rank == 0:
    data = numpy.arange(1000, dtype=numpy.float64)
    for i in range(1, size):
        comm.Send(data, dest=i )
    else:
        print ('Sending finished! ')
else:
    data = numpy.empty(1000, dtype=numpy.float64)
    comm.Recv([data, MPI.INT], source=0 )

comm.barrier()
#print (data)

if rank == 0:
    tt = time.time( )
    print ('end of float array.  Elapsed time = ', tt-ts, '\n') 
    #print (data)

