# COntiguous Collective I/O wth NumPy arrays

from mpi4py import MPI
import numpy as np

amode = MPI.MODE_WRONLY|MPI.MODE_CREATE
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

fh = MPI.File.Open(comm, "./datafile.contig", amode)

buffer = np.ones(20, dtype=np.int)

buffer[:] = rank + 65 # A, B, C, ....

#print(buffer)

offset = rank * buffer.nbytes
fh.Write_at_all(offset, buffer)

fh.Close()

print("Rank ", rank, "Buffer ", buffer)
