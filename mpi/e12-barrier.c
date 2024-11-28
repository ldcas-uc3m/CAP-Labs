#include <mpi.h>
#include <stdio.h>
int main(int argc, char** argv) {

    int w_size, w_rank, name_len;
    char p_name[MPI_MAX_PROCESSOR_NAME];
    int num;

    MPI_Init(NULL, NULL);
    MPI_Comm_size(MPI_COMM_WORLD, &w_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &w_rank);
    MPI_Get_processor_name(p_name, &name_len);
    printf("Hi! from Process %d (%s)\n", w_rank, p_name);
    fflush(stdout);
    MPI_Barrier(MPI_COMM_WORLD);
    printf("Process %d (%s) finish\n", w_rank, p_name);
    MPI_Finalize();
}
