#include <stdio.h>
#include <omp.h>

int buscaMaximo(int *a, int desde, int hasta) {
    int max_local = a[desde]; // Inicializa max_local con el primer elemento del sub-arreglo
    int i;

    // OpenMP paraleliza solo el bucle for
    #pragma omp parallel for reduction(max:max_local) num_threads(2) 
        for (i = desde + 1; i < hasta; i++) {
            if (a[i] > max_local) {
                max_local = a[i];
            }
            printf("Maximun in theread %d is: %d\n", omp_get_thread_num(), max_local);
        } 
    return max_local;
}

int main() {
    int arreglo[] = {1, 5, 9, 3, 7, 2, 8, 6, 4};
    int desde = 0;
    int hasta = sizeof(arreglo) / sizeof(arreglo[0]);

    int maximo = buscaMaximo(arreglo, desde, hasta);
    printf("The maximum is: %d\n", maximo);

    return 0;
}
