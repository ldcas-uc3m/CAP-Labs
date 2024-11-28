#include <stdio.h>
#include <omp.h>
int main (int argc, char **argv){
  int tid, global_acum=0;
  #pragma omp parallel private(tid)
  {
    int i, acum = 0;
    tid = omp_get_thread_num();  /* Get thread number */      
    #pragma omp for  /* split into threads */
    for (i=0; i<10; i++) {
	  printf("Iter * thread (%d * %d) = %d\n", i, tid, i*tid);
	  acum = acum + (i*tid);
    }
    #pragma omp critical
    global_acum = global_acum + acum;
  } /* All threads join master thread and terminate */
  printf("Accumulated value = %d\n", global_acum);
}

