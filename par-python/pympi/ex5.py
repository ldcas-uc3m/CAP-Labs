# Example of collectives.  Broadcast. 

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'key1' : [7, 2.72, 2+3j],
            'key2' : ( 'abc', 'xyz8888888'),
            'key3' : ( 'ab1', 'uip'),
            'key4' : ( '32', 'xyz'),
            'key5' : ( 'ead', '567'),
            'key6' : ( 'edf', '345')}
else:
    data = None

data = comm.bcast(data, root=0)

print ('rank', rank, 'data', data )

