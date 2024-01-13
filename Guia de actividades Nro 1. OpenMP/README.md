# Actividades

1. Realizar un Hello World y un contador de iteraciones en C, compilarlo y ejercutar
   ```bash
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

  ```bash
  gcc (o g++) –o HelloWorldParallel HelloWorldParallel.c -fopenmp
  ./HelloWorldParallel
  ```

- ¿Qué diferencia hay en la salida? Explique en función del hardware sobre el que está ejecutando el programa.
  La directiva `#pragma omp parallel` indica que el bloque de código siguiente debe ejecutarse en paralelo. La diferencia en la salida radica en que, debido a la directiva OpenMP, el bloque de código dentro del `pragma #pragma omp` parallel se ejecutará en varios hilos simultáneamente. Entonces, las multiples lineas "Hello World" y las iteraciones del bucle se imprimen en un orden no secuencial, ya que varios hilos se ejecutan de manera concurrente y pueden imprimir su salida en un orden intercalado. El orden y la cantidad de lineas pueden variar dependiendo de cómo se maneje la ejecución en el hardware (según el Scheduler) en el que se está ejecutando el programa. Tambien toma relevancia la catidad de núcleos disponibles en el hardware. En sistemas con un solo núcleo, el programa se ejecutará secuencialmente y dará una salida igual a la del primer programa.
