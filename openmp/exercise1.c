#include <stdio.h>
#include <omp.h>
int main (int argc, char **argv){
  int tid;

  int cores = omp_get_num_procs();
  printf("We have %d cores\n", cores);
  omp_set_num_threads(cores - 1);

  /* Create several threads (OMP_NUM_THREADS) */
  /* Each thread has a private variable (tid)*/
  #pragma omp parallel private(tid)
  {
    tid = omp_get_thread_num();  /* Get thread number */   
    printf("Hello World from thread = %d\n", tid);

  } /* All threads join master thread and terminate */
}

