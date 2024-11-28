
# Collectives MPI:  alltoall

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

'''
data0 = [0,'rank',rank]
data1 = [1,'rank',rank]
data2 = [2,'rank',rank]
'''

data0 = [0]
data1 = [1]
data2 = [2]

senddata=(data0,data1,data2)

print ('on task',rank,'  all to all  recvdata = ',senddata)

comm.barrier()

if (rank == 0):
   print ('AlltoAll \n')


recvdata = comm.alltoall(senddata)
print ('on task',rank,'  all to all  recvdata = ',recvdata)



