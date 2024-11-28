#include <stdio.h>
#include <omp.h>
int main (int argc, char **argv){
  int tid, acum=0;

  #pragma omp parallel private(tid)
  {
    tid = omp_get_thread_num();  /* Get thread number */   
    int i;
    #pragma omp for reduction(+:acum) /* split into threads */
    for (i=0; i<10; i++) {
	  printf("Iter * thread (%d * %d) = %d\n", i, tid, i*tid);
	  acum = acum + (i*tid);
    }
  } /* All threads join master thread and terminate */
  printf("Accumulated value = %d\n", acum);
}

