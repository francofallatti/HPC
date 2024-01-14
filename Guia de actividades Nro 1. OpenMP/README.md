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
3. Crear un programa en OpenMP que informe

   - La cantidad de hilos que se pidió al ejecutar el programa (lo solicitamos desde la línea de comandos).
   - La cantidad de procesadores disponibles y que muestre el modelo fork/join mostrando en pantalla que está ejecutando un solo hilo.
   - A continuación, que se ingresa a la región paralela mostrando que se abre la ejecución de n hilos.
   - Y por último se cierra la región paralela y sigue con 1 hilo de ejecución para finalizar.
     - `void omp_set_num_threads ( int num_threads );` Afecta el número de hilos usados por las regiones paralelas subsecuentes que no especifican una clausula num_threads.
     - `int omp get_num_threads(void);` Regresa el número de hilos de equipo actual.
     - `int omp get_max_threads(void);` Regresa el número máximo de hilos que pueden ser usados por un nuevo equipo que use la construcción parallel sin la cláusula num_threads.
     - `int omp get_thread_num(void);` Regresa la identidad del hilo en que se encuentra donde la identidad tiene un rango de 0 al tamaño del equipo de hilos menos 1.
     - `int omp get_num_procs(void);` Regresa el número de procesadores disponibles para el programa

4. En esta programación puede presentarse la llamada condición de carrera o _race condition_ que ocurre cuando Varios hilos tienen acceso a recursos compartidos **sin control**. El caso más común se da cuando en un programa varios hilos tienen acceso concurrente a una misma dirección de memoria (variable) y todos o algunos en algún momento intentan escribir en la misma localidad al mismo tiempo. Esto es un conflicto que genera salidas incorrectas o impredecibles del programa.
   En OpenMP al trabajar con hilos se sabe que hay partes de la memoria que comparten entre ellos y otras no. Por lo que habrá variables que serán compartidas entre los hilos, a las cuales todos los hilos tienen acceso y las pueden modificar, y habrá otras que serán propias o privadas de cada uno.
   Dentro del código se dirá que cualquier variable que esté declarada fuera de la región paralela será compartida y cualquier variable declarada dentro de la región paralela será privada.
   Continuar con el código de la actividad 2. Sacar de la región paralela la declaración de la variable entera i. Compilar y ejecutar el programa varias veces.

   ```c
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
   ```

   - ¿Qué sucedió? ¿Por qué sucede esto? De una explicación
