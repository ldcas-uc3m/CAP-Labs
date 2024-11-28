from mpi4py import MPI 
import time

comm = MPI.COMM_WORLD

assert comm.Get_size() > 1 
rank = comm.Get_rank() 

if rank == 0: 
    data = {'a': 7, 'b': 3.14}
    req = comm.isend(data, dest=1, tag=42) 
    req.wait()
elif rank == 1: 
    req = comm.irecv(source=0, tag=42)
    print("rank", rank, "to sleep")
    time.sleep(6)
    print("rank", rank, "to wait")
    data = req.wait()
    print (data)

