#include<stdio.h>
#include<omp.h>

int main(){
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
