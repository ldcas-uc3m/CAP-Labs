#include <stdio.h>
#include <omp.h>
int main (int argc, char **argv){
  int tid;

  printf("Parallel. Static (chunk size 3)\n");
  #pragma omp parallel private(tid)
  {
    tid = omp_get_thread_num();  /* Get thread number */   
    int i;
    #pragma omp for schedule (static, 3) /* split into threads */
      for (i=0; i<13; i++) {
          printf("Iteration %d on thread %d\n", i, tid);
      }
  } /* All threads join master thread and terminate */

  printf("Parallel. Dynamic (chunk size 3)\n");
  #pragma omp parallel private(tid)
  {
    tid = omp_get_thread_num();  /* Get thread number */   
    int i;
    #pragma omp for schedule (dynamic, 3) /* split into threads */
      for (i=0; i<13; i++) {
          printf("Iteration %d on thread %d\n", i, tid);
      }
  }

  printf("Parallel. Guided\n");
  #pragma omp parallel private(tid)
  {
    tid = omp_get_thread_num();  /* Get thread number */   
    int i;
    #pragma omp for schedule (guided) /* split into threads */
      for (i=0; i<13; i++) {
          printf("Iteration %d on thread %d\n", i, tid);
      }
  }
}

