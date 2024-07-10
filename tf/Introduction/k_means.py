import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

# Quitar los mensajes de aviso
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Configuración de parámetros
num_puntos = 800
num_clusters = 3
num_iteraciones = 500

# Generar los datos y seleccionar los centroides de manera aleatoria
puntos = tf.constant(np.random.uniform(0, 10, (num_puntos, 2)))
centroides = tf.Variable(tf.slice(tf.random.shuffle(puntos), [0, 0], [num_clusters, -1]))

# Aumentar una dimensión para poder restar
puntos_expand = tf.expand_dims(puntos, 0)
centroides_expand = tf.expand_dims(centroides, 1)

# Calcular la diferencia euclidiana y obtener la asignación de cada punto con el número de clusters más cercanos
distancias = tf.sqrt(tf.reduce_sum(tf.square(tf.subtract(puntos_expand, centroides_expand)), 2))
vector_dist_minimas = tf.argmin(distancias, 0)

# Se calculan los nuevos centroides 
lista = tf.dynamic_partition(puntos, tf.cast(vector_dist_minimas, dtype=tf.int32), num_clusters)
nuevos_centroides = [tf.reduce_mean(punto, 0) for punto in lista]

# Se asignan los centroides calculados a la variable centroides
centroides_actualizados = centroides.assign(nuevos_centroides)

# Se inicia una sesión y se ejecuta el algoritmo
init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sesion:
    sesion.run(init)
    for i in range(num_iteraciones):
        [_, valores_centroides, valores_puntos, valores_distancias] = sesion.run([centroides_actualizados, centroides, puntos, vector_dist_minimas])
    print("Centroides finales:\n", valores_centroides)

# Mostrar el resultado gráficamente
plt.scatter(valores_puntos[:, 0], valores_puntos[:, 1], c=valores_distancias, s=40, alpha=1, cmap=plt.cm.rainbow)
plt.plot(valores_centroides[:, 0], valores_centroides[:, 1], 'kx', markersize=15, mew=2)
plt.show()
