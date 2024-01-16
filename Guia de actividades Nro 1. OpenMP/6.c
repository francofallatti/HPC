#include <stdio.h>
#include <omp.h>

int main () {

    int tid, nth;

    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        nth = omp_get_max_threads();
        printf("Hello World desde el hilo %d de un total de %d\n", tid, nth);
    }

    printf("Bye");
    return 0;
}