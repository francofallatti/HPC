import tensorflow as tf
import os

# Quitar los mensajes de aviso
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Constantes
const1 = tf.constant(1.0, dtype=tf.float32, name="const1")
const2 = tf.constant(2.5, dtype=tf.float32, name="const2")

# Operaciones
sum = tf.add(const1, const2, name="sum")

# Información de constantes
print("Información: {}, valor {}".format(repr(const1), const1.numpy()))
print("Información: {}, valor {}".format(repr(const2), const2.numpy()))

# Ejecución de operaciones
for i in range(10):
    result = sum.numpy()
    print("Suma: {} de constantes {} + {} = {}".format(i, const1.numpy(), const2.numpy(), result))