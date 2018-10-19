
#import tensorflow
import tensorflow as tf

#here e are using import os for removing warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 2-D tensor `a`
# [[1, 2],
#  [3, 4]]
a = tf.constant([1, 2, 3, 4,], shape=[2, 2])

#A Session object encapsulates the environment in which Operation objects are executed, and Tensor objects are evaluated.
sess = tf.Session()
print("matrix A:")


#evaluate the tensor
print(sess.run(a))

# 2-D tensor `b`
# [[ 5,  6],
#  [ 7, 8]]
b = tf.constant([5, 6, 7, 8], shape=[2, 2])

print("matrix B:")
print(sess.run(b))

# 2-D tensor `c`
# [[ 9,  10],
#  [ 11, 12]]
c = tf.constant([9, 10, 11, 12], shape=[2, 2])

print("matrix C:")
print(sess.run(c))

# `a` * `a`
# [[ 7, 10 ],
#  [15, 22]]
a2 = tf.matmul(a, a)
print("matrix A X A:")
print(sess.run(a2))

# 'a^2' + 'b'
#[[12 ,16],
#[22, 30]]
s = tf.add(a2,b)
print("matrix A^2 + B:")
print(sess.run(s))

# '(a^2+b)*c
#[[284 , 312 ],
#[528 , 580]]
t =tf.matmul(s,c)
print("matrix (A^2 +B) X C:")
print(sess.run(t))