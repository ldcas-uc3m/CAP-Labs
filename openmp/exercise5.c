#include <stdio.h>
#include <omp.h>
int main (int argc, char **argv){
  int tid, acum;
  #pragma omp parallel private(tid, acum)
  {
    tid = omp_get_thread_num();  /* Get thread number */ 
    int i;
    #pragma omp for  /* split into threads */
    for (i=0; i<10; i++) {
	  printf("Iter * thread (%d * %d) = %d\n", i, tid, i*tid);
	  acum = acum + (i*tid);
    }
    #pragma omp barrier
    printf("Thread %d, acum = %d\n", tid, acum);  
  } /* All threads join master thread and terminate */
}

