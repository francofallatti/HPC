#include <stdio.h>
#include <omp.h>
#include <math.h>
#define n 120000

void printArray(int a[n]) {
    printf("[ ");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("]\n");
}

void fillArrayA(int a[n]) {
    for (int i = 0; i < n; i++) {
        a[i] = i + 1;
    }
}

void fillArrayB(int a[n]) {
    for (int i = 0; i < n; i++) {
        a[i] = i + 11;
    }
}

void sumArray(int a[n], int b[n], int c[n]) {
    for (int i = 0; i < n; i++) {
        c[i] = a[i] + b[i];
    }

    printf("c: ");
    printArray(c);
}

int main() {
    double start_time = omp_get_wtime();

    int a[n], b[n], c[n];

    fillArrayA(a);
    printf("a: ");
    printArray(a);

    fillArrayB(b);
    printf("b: ");
    printArray(b);

    sumArray(a, b, c);



    for (int i = 0; i < n; i++) {
        c[i] = a[i] + b[i];
    }

    double end_time = omp_get_wtime();
    printf("Serial Execution Time: %f seconds\n", end_time - start_time);

    return 0;
}
