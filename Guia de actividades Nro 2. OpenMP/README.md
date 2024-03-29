# Actividades

1. Dada una función que encuentra el máximo valor entero entre los elementos de un arreglo unidimensional de n elementos enteros, realizar una versión paralela.

   ```c
   int buscaMaximo(int *a, int desde, int hasta) {
        int max, i;
        max = a[ 0 ];
        for (i = desde; i < hasta; i++) {
            if (a[i] > max){
                max=a[i];
            }            
        }
        return max;
   }
   ```
    Analizar el problema. Ver que se puede realizar una descomposición de dominio o datos. En otras palabras, si se tienen varios hilos, cada uno puede buscar el máximo en un sub-arreglo del arreglo original, que le es asignado, y utilizar el mismo algoritmo de búsqueda sobre cada sub-arreglo.
    Utilizando la función del ejemplo que realiza la búsqueda, para dividir el arreglo entre los hilos cada uno debe empezar y terminar su índice del arreglo en diferente valor. Para conseguir esto con OpenMP, como vimos en los ejemplos de la Guía de Actividades 1, se utiliza el constructor for que divide el computo entre los hilos.
    ```C
    # pragma omp parallel
    {
      #pragma omp for
    //Se puede reunir en
    # pragma omp parallel for
    ```
    Importante: Cuando cada hilo trabaje con una parte del arreglo puede ser que al revisar si `a[i] > max` y dos de ellos actualizan max pueda ocurrir que se dé una race condition. Esto es posible, aunque las ejecuciones parezcan que están bien.

      La clausula `reduction(max:max_local)` especifica que cada hilo tendrá su propia copia de `max_local` que se inicializa con el valor del primer elemento de su sub-arreglo. Después de que todos los hilos hayan terminado, OpenMP combinará estos valores locales en uno global usando la operación máxima, lo que dará el máximo global del arreglo. Esto elimina la necesidad de una sección crítica y hace que el código sea más eficiente.

    ### Cláusula reduction
    Para conocer cómo opera esta cláusula pensemos un ejemplo: 
    Realizar el producto escalar entre dos vectores de n elementos cada uno, el cual se grafica a continuación:\
    ![Image p1](../img/p1.png)

    Para tener una solución paralela con hilos que cooperen en el cómputo se analizará dividir el cálculo entre los n hilos. Otra vez hay que repartir el arreglo en sub-arreglos y encontrar los índices en función del Id del hilo.
    La siguiente es una primera manera de paralelizarlo usando la cláusula for:\
    ![Image p1b](../img/p1b.png)

    - Implementar este código.
    - ¿Los resultados obtenidos son correctos?
    - ¿Cuál es la función de la variable RES?
    - Explique el comportamiento del algoritmo

    Se inicia una región paralela con dos hilos utilizando `#pragma omp parallel reduction(+:res) num_threads(2)`. Cada hilo obtiene su número de identificación (tid) utilizando `omp_get_thread_num()`. La variable `res` se utiliza para acumular el resultado del producto escalar de dos vectores. La directiva `reduction(+:res)` indica que cada hilo debe tener su propia copia de `res`, y al final de la región paralela, se combinarán todos los valores de `res` de los diferentes hilos mediante una operación de suma de reduction. El bucle for es paralelizado con `#pragma omp for`. Cada hilo ejecuta una porción del bucle, sumando el producto de los elementos correspondientes de los vectores a y b a su variable local `res`. Al final de la región paralela, se devuelve el valor acumulado de `res`, que representa el producto escalar de los dos vectores. Esto significa que cada hilo realiza su propio cálculo parcial del producto escalar y al final, estos resultados parciales se suman para obtener el resultado final del producto escalar.
     

2. Escribir una solución posible para el problema anterior usando un arreglo de resultados RES. Reescribir la solución anterior usando la cláusula reduction

La cláusula reduction toma el valor de una variable aportada por cada hilo y aplica la operación indicada sobre esos datos para obtener un resultado correcto libre de race conditions. Esta cláusula suma todos los res parciales de cada hilo y deja la suma acumulada de todos en la
misma variable res. Algunos operadores válidos para utilizar en la cláusula reduction:

![reduction](../img/reduction.png)

## Constructor Sections
Sections es un constructor que permite la programación paralela funcional (descomposición funcional) debido a que permite construir secciones de código independiente a hilos diferentes que trabajarán en modo concurrente o paralelo. Como se ve en el siguiente esquema:

![sections](../img/sections.png)

3. Probar el ejemplo b. del constructor Barrier visto anteriormente y responder las siguientes preguntas
    - ¿Qué sucede si se quita la barrera?
    - Si en lugar del constructor Master se utiliza Single, ¿qué otros cambios se tienen que hacer en el código? Realice los cambios

    Sí, al quitar la barrera `#pragma omp barrier`, ocurre una race condition al momento de ejecutar el código. Ya quemúltiples hilos acceden y modifican `a[i]` de forma concurrente, y el resultado final depende del orden de ejecución de los hilos. Sin la barrera, los hilos continúan ejecutando la sección de código que modifica los valores de `a[i]` en `a[i] += i;`. Debido a que esta sección que imprime no tiene la barrera, los hilos pueden modificar `a` mientras otro hilo aún están imprimiendo sus valores originales. Como resultado, los valores impresos no son los originales y son incorrectos. Por consola podriamos recibir resultados, como los que se muestran a continuación

    | Con #pragma omp barrier        | Sin #pragma omp barrier       |
    |--------------------|-------------------|
    | a[0] = 0           | a[0] = 0          |
    | a[1] = 1           | a[1] = 2          |
    | a[2] = 4           | a[2] = 6          |
    | a[3] = 9           | a[3] = 12         |
    | a[4] = 16          | a[4] = 20         |

    
    Al reemplazar `#pragma omp master` con `#pragma omp single` el bloque de código solo será ejecutado por un único hilo en el equipo, pero esto no garantiza que el hilo que ejecutará el bloque sea siempre el hilo maestro. Puede ser cualquier hilo que llegue primero al punto de ejecución.

4. Una forma de obtener la aproximación del número irracional PI es utilizar la regla del trapecio para dar solución aproximada a la integral definida

    ![pi](../img/pi.png)
    
    Se da a continuación el código serial para que se comprenda el método numérico que se utiliza y se pide escribir una versión para OpenMP.
