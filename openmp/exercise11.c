/*
  Purpose:

    MAIN is the main program for MXM_OPENMP.

  Licensing:

    This code is distributed under the GNU LGPL license. 


  Author:

    John Burkardt
*/

// Compile with:  gcc -fopenmp  exercise11.c -lm

# include <stdlib.h>
# include <stdio.h>
# include <math.h>
# include <time.h>
# include <omp.h>

int main ( void );
void timestamp ( void );

/******************************************************************************/

int main ( void )

/******************************************************************************/

{
  double a[500][500];
  double b[500][500];
  double c[500][500];
  int n = 500;
  int i;
  double angle;
  int j;
  int k;
  double pi = 3.141592653589793;
  double s;
  int thread_num;
  double wtime;

  timestamp ( );

  printf ( "\n" );
  printf ( "MXM_OPENMP:\n" );
  printf ( "  C/OpenMP version\n" );
  printf ( "  Compute matrix product C = A * B.\n" );

  thread_num = omp_get_max_threads ( );

  printf ( "\n" );
  printf ( "  The number of processors available = %d\n", omp_get_num_procs ( ) );
  printf ( "  The number of threads available    = %d\n", thread_num );

  printf ( "  The matrix order N                 = %d\n", n );
/*
  Loop 1: Evaluate A.
*/
  s = 1.0 / sqrt ( ( double ) ( n ) );

  wtime = omp_get_wtime ( );

# pragma omp parallel shared ( a, b, c, n, pi, s ) private ( angle, i, j, k )
{
  # pragma omp for
  for ( i = 0; i < n; i++ )
  {
    for ( j = 0; j < n; j++ )
    {
      angle = 2.0 * pi * i * j / ( double ) n;
      a[i][j] = s * ( sin( angle ) + cos( angle ) );
    }
  }
/*
  Loop 2: Copy A into B.
*/
  # pragma omp for
  for ( i = 0; i < n; i++ )
  {
    for ( j = 0; j < n; j++ )
    {
      b[i][j] = a[i][j];
    }
  }
/*
  Loop 3: Compute C = A * B.
*/
  # pragma omp for
  for ( i = 0; i < n; i++ )
  {
    for ( j = 0; j < n; j++ )
    {
      c[i][j] = 0.0;
      for ( k = 0; k < n; k++ )
      {
        c[i][j] = c[i][j] + a[i][k] * b[k][j];
      }
    }
  }

}
  wtime = omp_get_wtime ( ) - wtime;
  printf ( "  Elapsed seconds = %g\n", wtime );
  printf ( "  C(500,500)  = %g\n", c[499][499] );
/*
  Terminate.
*/
  printf ( "\n" );
  printf ( "MXM_OPENMP:\n" );
  printf ( "  Normal end of execution.\n" );

  printf ( "\n" );
  timestamp ( );

  return 0;
}
/******************************************************************************/

void timestamp ( void )

/******************************************************************************/
{
# define TIME_SIZE 40

  static char time_buffer[TIME_SIZE];
  const struct tm *tm;
  time_t now;

  now = time ( NULL );
  tm = localtime ( &now );

  strftime ( time_buffer, TIME_SIZE, "%d %B %Y %I:%M:%S %p", tm );

  printf ( "%s\n", time_buffer );

  return;
# undef TIME_SIZE
}


