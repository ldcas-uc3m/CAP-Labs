// Work with atomic sections to avoid concurrency problems

#include <stdio.h>
#include <omp.h>

int main(void) {
  int count = 0;
  #pragma omp parallel shared(count)
  {
     #pragma omp atomic
     count++; // count is updated by only a single thread at a time
  }
  printf("Number of threads: %d\n", count);
}
