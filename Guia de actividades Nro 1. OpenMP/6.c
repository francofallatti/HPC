#include <stdio.h>
#include <omp.h>

int main () {

    int tid, nth;

    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();  // Returns the thread id
        nth = omp_get_max_threads(); // Returns the maximum number of threads
        printf("Hello World from thread %d out of a total of %d\n", tid, nth);
    }

    printf("Bye");
    return 0;
}