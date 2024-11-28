#include <stdio.h>
#include <omp.h>

int main()
{

    int iam=0;

   omp_set_dynamic(0);     // Explicitly disable dynamic teams
   omp_set_num_threads(4); // Use 4 threads for all consecutive parallel regions


  #pragma omp parallel private(iam)
  {
    #pragma omp sections
    {
      #pragma omp section 
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 1ª \n",iam);
      }
      #pragma omp section
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 2ª \n",iam);
      }
      #pragma omp section
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 3ª \n",iam);
      }
      #pragma omp section
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 4ª \n",iam);
      }
      #pragma omp section
      {
         iam=omp_get_thread_num ();
         printf("Soy el thread %d, en solitario en la seccion 5ª \n",iam);
      }
    }//sections
  }//parallel

}
