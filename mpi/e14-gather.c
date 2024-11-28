#include <mpi.h>
#include <stdio.h>
int main(int argc, char** argv) {

    int w_size, w_rank, name_len;
    char p_name[MPI_MAX_PROCESSOR_NAME];
    int send_vec[3], recv_vec[20], i, acum=0;

    MPI_Init(NULL, NULL);
    MPI_Comm_size(MPI_COMM_WORLD, &w_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &w_rank);
    MPI_Get_processor_name(p_name, &name_len);

    if (w_rank == 0) {
       for (i=0; i<3; i++) send_vec[i]=w_rank*i;    
    }

    MPI_Gather(send_vec, 3, MPI_INT, recv_vec, 3, MPI_INT, 0, MPI_COMM_WORLD);

    if (w_rank ==0)
      for (i=0; i < w_size*3; i++) {        
         printf("(%s): Proc num: %d; acum = %d \n", p_name, w_rank, acum);
      }
 
    MPI_Finalize();
}
