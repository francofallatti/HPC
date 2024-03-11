#include <stdio.h>

int buscaMaximo( int *a, int desde, int hasta) {
    int max, i;
    max = a[0];
    for (i = desde; i < hasta; i++) {
        if (a[i] > max){
            max=a[i];
        }
    }
    return max;
}

int main() {
    int arreglo[] = {1, 5, 9, 3, 7, 2, 8, 6, 4};
    int desde = 0; 
    int hasta = sizeof(arreglo) / sizeof(arreglo[0]);

    int maximo = buscaMaximo(arreglo, desde, hasta);
    printf("The maximum is: %d\n", maximo);

    return 0;
}