# Actividades

1. Realizar un Hello World y un contador de iteraciones en C, compilarlo y ejercutar
   ```console
   gcc (o g++) –o HelloWorld HelloWorld.c
   ./HelloWorld
   ```

- Agregar constructor paralelo, compilarlo y ejercutar
  ```C
  #pragma omp parallel
  {
  	...
  }
  ```
  ```console
  gcc (o g++) –o HelloWorldParallel HelloWorldParallel.c -fopenmp
  ./HelloWorldParallel
  ```
