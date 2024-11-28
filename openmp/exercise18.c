
// add all elements in an array in parallel  
#include <stdio.h>
#include <omp.h>
#include <time.h>


int main() {

  int N=100000; 
  int i;
  int a[N], b[N], c[N]; 
  int sum=0; 

   clock_t start, end;
     double cpu_time_used;

     
  start = clock();
  
  //initialize 
 #pragma omp simd simdlen(32)
  for (i=0; i < N; i++){
    a[i] = i; 
    b[i] = i; 
  }

    
 #pragma omp simd simdlen(32)
   for (i=0; i< N; i++) 
      c[i] = a[i] + b[i]; 

 #pragma omp simd simdlen(32)
   for (i=0; i< N; i++) 
	   sum += c[i];

  end = clock();
  cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

  printf("suma = %d time = %f  \n", sum, cpu_time_used );

}
