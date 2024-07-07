import tensorflow as tf
import os

# Quitar los mensajes de aviso
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Variables
x = tf.constant(5.0, dtype=tf.float32, name="x")
y = tf.Variable([3.5], dtype=tf.float32, name="y")
z = tf.Variable(0.0, dtype=tf.float32, name="z")

# Crear un escritor de archivo para TensorBoard
logdir = "logs/basicGraph"
writer = tf.summary.create_file_writer(logdir)

# Operaciones (x*y+z)
with writer.as_default():
    for i in range(10):
        z.assign(tf.cast(i, dtype=tf.float32))  # Actualizar z con el valor de i
        mult = tf.multiply(x, y, name="mult")  # Recalcular mult
        sum_op = tf.add(mult, z, name="sum")  # Recalcular sum_op
        pacial_result = mult.numpy()
        result = sum_op.numpy()

        # Registrar los valores de las variables y la operación sum_op en cada paso
        tf.summary.scalar("x", x.numpy(), step=i)
        tf.summary.scalar("y", y.numpy()[0], step=i)
        tf.summary.scalar("z", z.numpy(), step=i)
        tf.summary.scalar("sum", result[0], step=i)  # Extract scalar value from tensor

        print("{}*{}+{}={}+{}={}".format(x.numpy(), y.numpy(), i, pacial_result, i, result))

print(f"Se ha creado el archivo para TensorBoard en '{logdir}'")
writer.close()
