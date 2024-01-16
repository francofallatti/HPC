#include <stdio.h>
#include <omp.h>
#include <math.h>
#define n 10

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
    int a[n], b[n], c[n];

    fillArrayA(a);
    printf("a: ");
    printArray(a);

    fillArrayB(b);
    printf("b: ");
    printArray(b);

    sumArray(a, b, c);

    return 0;
}
