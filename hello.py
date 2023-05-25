#save this file as hello.py
import tensorflow as tf

# Simple hello world using TensorFlow
hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))