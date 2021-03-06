# Module 4: Simple TF Model
# Simple TF model on MINST dataset

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Parameters
learning_rate = 0.008
batch_size = 100

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("mnist", one_hot=True,reshape=True,validation_size=0)

# Step 1: Initial Setup
X = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Step 2: Setup Model
yhat = tf.nn.softmax(tf.matmul(X,W)+b)
y = tf.placeholder(tf.float32, [None, 10]) # placeholder for correct answers

# Step 3: Cross Entropy Loss Functions
loss = -tf.reduce_sum(y*tf.log(yhat))

# Step 4: Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

# % of correct answer found in batches
is_correct = tf.equal(tf.argmax(y,1),tf.argmax(yhat,1))
accuracy = tf.reduce_mean(tf.cast(is_correct,tf.float32))

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# Step 5: Training Loop
for i in range(1000):
    batch_X, batch_y = mnist.train.next_batch(batch_size)
    train_data = {X: batch_X, y: batch_y}
    sess.run(train, feed_dict=train_data)
    print("Training Accuracy = ",sess.run(accuracy,feed_dict = train_data))

# Step 6: Evaluation
test_data = {X:mnist.test.images,y:mnist.test.labels}
print("Testing Accuracy = ", sess.run(accuracy, feed_dict = test_data))