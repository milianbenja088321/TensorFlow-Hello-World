import tensorflow as tf
# Simple hello world using Tensorflow

# Create a cosntant op
# The op is added as a node to the default graph.

# The value returned by the constructor reperesents the output
# of the Constant op.
hello = tf.constant("Hello, World!")

# Start tf session
sess = tf.Session()

# Run the op
print (sess.run(hello))

