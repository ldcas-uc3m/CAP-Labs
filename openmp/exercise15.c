#include <stdio.h>
#include <omp.h>

int main()
{

    int iam=0;
    int comp=0;
  #pragma omp parallel private(iam)
  {
      #pragma omp critical 
      {
         iam=omp_get_thread_num ();
	 comp++;
         printf("Soy el thread %d, en solitario en la seccion critica. Compartida = %d \n",iam,comp);
      }
  }//parallel
  printf("\n Fin de la seccion critica \n\n");

  #pragma omp parallel private(iam)
  {
         iam=omp_get_thread_num ();
	 comp++;
         printf("Soy el thread %d, en solitario en la seccion critica. Compartida = %d \n",iam,comp);
  }//parallel

}
