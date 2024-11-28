// add all elements in two arrays in parallel
#include <stdio.h>
#include <omp.h>


int main() {

  const int N=1000; 
  int a[N], b[N], c[N]; 

  //initialize 
  for (int i=0; i < N; i++){
    a[i] = i; 
    b[i] = i*2;
  } 

//the array is distributde statically between threads
#pragma omp for schedule(static,4) 
    for (int i=0; i< N; i++) {
      c[i] = a[i]+b[i]; 
      printf("%d , ", c[i]);
    }

//  for (int i=0; i < N; i++)
//      printf("%d , ", c[i]);
}