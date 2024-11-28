#include <stdio.h>
#include <omp.h>

int main()
{

    int iam=0;
    int x=0;
  #pragma omp parallel private(iam)
  {
    #pragma omp master
    {
	iam = omp_get_thread_num();
	x = 1200;
        printf("Soy el thread %d, actualizando x=%d \n\n",iam,x);
    }

	iam = omp_get_thread_num();
    printf("Soy el thread %d, antes del flush, con x=%d \n",iam,x);

    #pragma omp flush(x)

	iam = omp_get_thread_num();
    printf("\t\t-----Soy el thread %d, despues del flush, con x=%d \n",iam,x);

  }//parallel

}
