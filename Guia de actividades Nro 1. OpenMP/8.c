#include<stdio.h>
#include<omp.h>

int main() {
    int i; 

    #pragma omp parallel
    {
        printf("Hello World!\n");
        
        #pragma omp for
        for(i = 0; i < 10; i++) {
            printf("Iteration: %d, desde el hilo con el id: %d\n", i, omp_get_thread_num());
        }
    }

    printf("Bye \n");
    return 0;
}
