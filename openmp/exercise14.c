#include <stdio.h>
#include <omp.h>

int main()
{

    int iam=0;
  #pragma omp parallel private(iam)
  {
      #pragma omp master 
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 1ª \n",iam);
      }
      #pragma omp master
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 2ª \n",iam);
      }
      #pragma omp master
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 3ª \n",iam);
      }
  }//parallel

}
