#include <stdio.h>
#include <omp.h>
#include <math.h>

int start, end;

void printArray(int a[], int size) {
    printf("[ ");
    for (int i = 0; i < size; i++) {
        printf("%d ", a[i]);
    }
    printf("]\n");
}

void fillArrayA(int a[], int size) {
    for (int i = 0; i < size; i++) {
        a[i] = i + 1;
    }
}

void fillArrayB(int a[], int size) {
    for (int i = 0; i < size; i++) {
        a[i] = i + 11;
    }
}

void sumArray(int a[], int b[], int c[], int size) {

    // Set num_threads() with set OMP_NUM_THREADS=4
    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        int num_threads = omp_get_num_threads();

        // Asegura que el número de threads sea divisor de n
        while (size % num_threads != 0) {
            num_threads--;
        }

        int chunk_size = size / num_threads;
        int start = tid * chunk_size;
        int end = start + chunk_size;

        for (int i = start; i < end; i++) {
            c[i] = a[i] + b[i];
            printf("Part of c with thread: %d, c[%d] = %d -> (%d + %d)\n", tid, i, c[i], a[i], b[i]);
        }
    }

    printf("c: ");
    printArray(c, size);
}

int main() {
    double start_time = omp_get_wtime();

    int size;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    int a[size], b[size], c[size];

    fillArrayA(a, size);
    printf("a: ");
    printArray(a, size);

    fillArrayB(b, size);
    printf("b: ");
    printArray(b, size);

    sumArray(a, b, c, size);

    double end_time = omp_get_wtime();
    printf("Parallel Execution Time: %f seconds\n", end_time - start_time);
    return 0;
}
