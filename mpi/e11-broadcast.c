#include <mpi.h>
#include <stdio.h>

int main (int argc, char** argv) {

    int w_size, w_rank, name_len;
    char p_name[MPI_MAX_PROCESSOR_NAME];
    int num = 0;

    MPI_Init(NULL, NULL);
    MPI_Comm_size(MPI_COMM_WORLD, &w_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &w_rank);
    MPI_Get_processor_name(p_name, &name_len);

    if (w_rank == 0) num = 12345;
    printf("Process %d (%s): number %d\n",w_rank, p_name, num);

   MPI_Bcast(&num, 1, MPI_INT, 0, MPI_COMM_WORLD);

   printf("Process %d (%s) new  number %d\n",w_rank, p_name, num);
    MPI_Finalize();
}
