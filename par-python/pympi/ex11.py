# NOn COntiguous (Interleaved) Collective I/O wth NumPy arrays



from mpi4py import MPI
import numpy as np

amode = MPI.MODE_WRONLY|MPI.MODE_CREATE
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


fh = MPI.File.Open(comm, "./datafile.noncontig", amode)

item_count = 10

buffer = np.empty(item_count, dtype='i')
buffer[:] = rank+65 #A, B, C, D, ..

filetype = MPI.INT.Create_vector(item_count, 1, size)
filetype.Commit()

displacement = MPI.INT.Get_size()*rank

fh.Set_view(displacement, filetype=filetype)

fh.Write_all(buffer)
filetype.Free()

fh.Close()

print(" Rank ", rank, "Buffer ", buffer)



