#include <stdio.h>
#include <omp.h>

int main(){
    
    // Ingresar cantidad de hilos a ejecutar
    int cant_hilos;
    printf("Ingrese cantidad de hilos: ");
    scanf("%d", &cant_hilos);

    // Setea la cantidad de hilos
    omp_set_num_threads(cant_hilos);

    // Informa la cantidad de hilos que se pidió al ejecutar el programa
    printf("Cantidad de hilos a ejecutar: %d\n", omp_get_max_threads());

    // Informa la cantidad de procesadores disponibles
    printf("Cantidad de procesadores disponibles: %d\n", omp_get_num_procs());

    #pragma omp parallel 
    {
        // Informa la cantidad de hilos en la región paralela
        printf("Se están ejecutando %d hilos\n", omp_get_num_threads());

        // Saluda cada hilo e informa su id
        printf("Hello World desde el hilo con el id: %d\n", omp_get_thread_num());

    }

    printf("Fin de la region paralela\n");
    printf("Se ejecuta el hilo %d para finalizar \n", omp_get_thread_num());
    printf("Fin del programa!");

    return 0;
}