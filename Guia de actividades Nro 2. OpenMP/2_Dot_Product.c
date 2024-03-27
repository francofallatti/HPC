#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <time.h>
#define n 10

void printArray(double a[n]);

double dotProduct(double *a, double *b) {
    double res = 0, resArr[n];
    int i;

    #pragma omp parallel reduction(+:res) num_threads(2)
    {
        int tid = omp_get_thread_num();
        
        #pragma omp for
        for(i = 0; i < n; i++){
            res += a[i] * b[i];
            resArr[i] = a[i] * b[i];
            printf("Dot Product iteration with thread %d is: %lf \n", tid, res);
        }
    }
    printf("Array of results: ");
    printArray(resArr);

    return res;
}

void printArray(double a[n]) {
    printf("[ ");
    for (int i = 0; i < n; i++) {
        printf("%lf ", a[i]);
    }
    printf("]\n");
}

void fillArrayA(double a[n]) {
    for (int i = 0; i < n; i++) {
        a[i] = i + ((double)rand() / RAND_MAX) * 9.0 + 1.0;
    }
}

void fillArrayB(double a[n]) {
    for (int i = 0; i < n; i++) {
        a[i] = i + ((double)rand() / RAND_MAX) * 9.0 + 1.0;
    }
}

int main(){
     srand(time(NULL)); // Inicializar la semilla del generador de números aleatorios con el tiempo actual
    double a[n], b[n];

    fillArrayA(a);
    printf("a: ");
    printArray(a);

    fillArrayB(b);
    printf("b: ");
    printArray(b);

    double dotProductResult = dotProduct(a, b);
    printf("the dot product is: %lf", dotProductResult);
}