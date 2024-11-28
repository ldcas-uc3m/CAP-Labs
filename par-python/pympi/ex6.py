#Scatter gather example


from mpi4py import MPI

def factorial(n):
    # Base case: 1! = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# main part 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

## Scatter

if rank == 0:
     data = [factorial(i) for i in range(size)]
     print ("data in rank 0 ", data)
else:
    data = None
data1 = comm.scatter(data, root=0)

assert data1 == factorial(rank)
print ('Scatter in rank', rank, data1)

comm.barrier()
## gather

data = comm.gather(data1, root=0)
if rank == 0:
    print ('Gather in rank 0 ', data)
else:
    assert data is None



