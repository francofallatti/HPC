#include<stdio.h>
#include<omp.h>

int main(){

	omp_set_num_threads(2); // Cantidad de threads a utilizar

	#pragma omp parallel
	{
		printf("Hello World!\n");
		for(int i=0; i<10; i++){
			printf("Iteration: %d\n", i);
		}
	}
	printf("Bye \n");
	return 0;
}
