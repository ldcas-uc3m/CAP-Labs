#include <stdio.h>
#include <omp.h>

int main()
{

    int iam=0;
    int x=0;
  #pragma omp parallel private(iam)
  {
    omp_set_nested(1);

    #pragma omp parallel private(iam)
    {
	iam = omp_get_thread_num();
	x++;
        printf("Soy el thread %d, actualizando x=%d dentro \n\n",iam,x);
     }//parallel

  }//parallel

}
