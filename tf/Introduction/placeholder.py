import tensorflow as tf
import os

# Quitar los mensajes de aviso
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Variables
v1 = tf.Variable([3.5], dtype=tf.float32, name="v1")

# Operaciones
@tf.function
def update_variable(var):
    var.assign(var - 0.5)
    return var

# Información de variables
print("Información: {}, valor {}".format(repr(v1), v1.numpy()))

# Ejecución de operaciones
for i in range(10):
    updated_value = update_variable(v1)
    print("Información {}: {}, valor {}".format(i, repr(v1), updated_value.numpy()))
