
// average for  all elements in an array in parallel
#include <stdio.h>
#include <omp.h>
#include <sys/time.h>


long current_timestamp() {
    struct timeval te;
    gettimeofday(&te, NULL); // get current time
    long milliseconds = te.tv_sec*1000 + te.tv_usec/1000; // calculate milliseconds
    // printf("milliseconds: %lld\n", milliseconds);
    return milliseconds;
}




int main() {

  const int N=1000;
  int a[N];
  int num_threads = 1;
  long tinit, tend;

  tinit = current_timestamp();
  //initialize
  for (int i=0; i < N; i++)
    a[i] = 2;

  //compute sum
  int local_sum, local_num, local_avg, avg;
#pragma omp parallel private(local_sum, local_num, local_avg) shared(avg)
  {
    omp_set_num_threads(4);
    num_threads = omp_get_num_threads();
    local_sum =0;
    local_num =0;

//the array is distributde statically between threads
#pragma omp for schedule(static,1)
    for (int i=0; i< N; i++) {
      local_sum += a[i];
      local_num ++;
    }
    local_avg = local_sum / local_num;

    //each thread calculated its local_sum. ALl threads have to add to
    //the global sum. It is critical that this operation is atomic.

#pragma omp critical
    avg += local_avg;

  }

    avg = avg / num_threads;

  tend = current_timestamp();

  printf("avg = %d exec time  %ld \n", avg, tend-tinit);
}
