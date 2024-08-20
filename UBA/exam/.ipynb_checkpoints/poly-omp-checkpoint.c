#include <stdio.h>
#include <float.h>
#include <omp.h>

int main(int argc, char* argv[]) {
  double coeff[4], xmin, xmax, nsteps;
  FILE* in;
  double starttime, endtime;
    
  if ( (in = fopen("poly.dat", "r")) == NULL ) {
    perror("poly.dat");
    return 1;
  }
  fscanf(in, "%lg %lg %lg %lg", &coeff[0], &coeff[1], &coeff[2], &coeff[3]);
  fscanf(in, "%lg %lg %lg", &xmin, &xmax, &nsteps);

  double step = (xmax - xmin) / (nsteps - 1);
  double ymax = -DBL_MAX;

  starttime = omp_get_wtime();
    
  #pragma omp parallel for reduction(max:ymax)
  for (int i=0; i<(int)nsteps; ++i) {
    double x = xmin + i * step;
    double y = coeff[3]*x*x*x + coeff[2]*x*x + coeff[1]*x + coeff[0];
    if ( y > ymax) ymax = y;
  }

  endtime = omp_get_wtime();
    
  printf("Maximum is %lg\n", ymax);
  printf("OMP %d threads used %.6f seconds\n", omp_get_max_threads(), endtime - starttime);

  return 0;
}
