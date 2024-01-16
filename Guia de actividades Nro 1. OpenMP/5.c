#include<stdio.h>
#include<omp.h>

int main() {

    int i=0;  // Declarar i fuera de la región paralela

    #pragma omp parallel private(i)
    {
        printf("Hello World desde el hilo con el id: %d\n", omp_get_thread_num());

        while(i < 10) {
            printf("Iteration: %d from thread %d\n", i, omp_get_thread_num());
            i++;
        }
    }

    printf("Bye\n");
    return 0;
}