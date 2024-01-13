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

2. En cada región paralela hay un número de hilos generados por defecto y ese número es igual al de unidades de procesamiento que se tengan en la computadora paralela que se esté utilizando, en este caso el número de núcleos que tenga el procesador.
   En el mismo código, cambiar el número de hilos que habrá en la región paralela a un número diferente n (entero), probar cada una de las formas indicadas a continuación. Primero modificar, después compilar y ejecutar nuevamente el programa en cada cambio.
   1. Modificar la variable de ambiente desde la consola de la siguiente forma:
      `export OMP_NUM_THREADS = 4` en Unix y `set OMP_NUM_THREADS=4` en Windows
   ```bash
   Salida por consola (set OMP_NUM_THREADS=4 && .\1_HelloWorldParallel.exe):
   Hello World!
   Iteration: 0
   Iteration: 1
   Iteration: 2
   Iteration: 3
   Iteration: 4
   Iteration: 5
   Iteration: 6
   Iteration: 7
   Iteration: 8
   Iteration: 9
   Hello World!
   Iteration: 0
   Iteration: 1
   Iteration: 2
   Iteration: 3
   Iteration: 4
   Iteration: 5
   Iteration: 6
   Iteration: 7
   Iteration: 8
   Iteration: 9
   Hello World!
   Iteration: 0
   Iteration: 1
   Iteration: 2
   Iteration: 3
   Iteration: 4
   Iteration: 5
   Iteration: 6
   Iteration: 7
   Iteration: 8
   Iteration: 9
   Hello World!
   Iteration: 0
   Iteration: 1
   Iteration: 2
   Iteration: 3
   Iteration: 4
   Iteration: 5
   Iteration: 6
   Iteration: 7
   Iteration: 8
   Iteration: 9
   Bye
   ```
   2. Cambiar el número de hilos a `n` un entero llamando a la función `omp_set_num_threads(n)` que se encuentra en la biblioteca omp.h
   ```bash
   Salida por consola (2_HelloWorldParallel_omp_set_num_threads.exe):
   Hello World!
   Iteration: 0
   Iteration: 1
   Iteration: 2
   Iteration: 3
   Iteration: 4
   Iteration: 5
   Iteration: 6
   Iteration: 7
   Iteration: 8
   Iteration: 9
   Hello World!
   Iteration: 0
   Iteration: 1
   Iteration: 2
   Iteration: 3
   Iteration: 4
   Iteration: 5
   Iteration: 6
   Iteration: 7
   Iteration: 8
   Iteration: 9
   Bye
   ```
   3. Agregar la clúsula `num_threads(n)` seguida después del constructor parallel, esto es: `#pragma omp parallel num_threads(n)`
   ```bash
    Salida por consola (2_HelloWorldParallel_num_threads.exe):
    Hello World!
    Iteration: 0
    Iteration: 1
    Iteration: 2
    Iteration: 3
    Iteration: 4
    Iteration: 5
    Iteration: 6
    Iteration: 7
    Iteration: 8
    Iteration: 9
    Hello World!
    Iteration: 0
    Iteration: 1
    Iteration: 2
    Iteration: 3
    Iteration: 4
    Iteration: 5
    Iteration: 6
    Iteration: 7
    Iteration: 8
    Iteration: 9
    Hello World!
    Iteration: 0
    Iteration: 1
    Iteration: 2
    Iteration: 3
    Iteration: 4
    Iteration: 5
    Iteration: 6
    Iteration: 7
    Iteration: 8
    Iteration: 9
    Bye
   ```
