#  MPI collectives all gather and all reduce
#  run with 3 procs


from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 4
senddata = (rank+1)*numpy.arange(a_size,dtype=numpy.float64)
recvdata = numpy.arange(size*a_size,dtype=numpy.float64)

comm.Allgather(senddata,recvdata)
print ('in task',rank,'after Gather:    data = ',recvdata)

#  Gatherv is for variable lengh buffers
counts=(2,3,4)
dspls=(0,3,8)
recvdata = numpy.empty(12,dtype=numpy.float64)

comm.Allgatherv([senddata,counts[rank]],[recvdata,counts,dspls,MPI.DOUBLE])
print ('in task',rank,'after Gatherv:    data = ',recvdata)

comm.barrier()

# All reduce operations

global_sum = numpy.zeros(a_size * size, dtype='float64')
local_sum = numpy.sum(recvdata)

comm.Allreduce(recvdata, global_sum, op=MPI.SUM)
print ('in task',rank,'All reduce:    ',  global_sum)


comm.barrier()

a_size = 3
recvdata = numpy.zeros(a_size,dtype=numpy.int)
senddata = (rank+1)*numpy.arange(a_size,dtype=numpy.int)

comm.Reduce(senddata,recvdata,root=0,op=MPI.PROD)
print ('on task',rank,'after Reduce:    data = ',recvdata)

comm.Allreduce(senddata,recvdata)
print ('on task',rank,'after Allreduce:    data = ',recvdata)

 
comm.barrier()


