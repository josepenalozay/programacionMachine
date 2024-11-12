from timeit import default_timer as timer
import numpy as np

a = [i for i in range(1000)]
b = [i for i in range(1000)]

start = timer()
dot = 0.0
for i in range(len(a)):
    dot += a[i] * b[i]
end = timer()

print("dot_product = "+ str(dot));
print("Computation time = " + str(1000*(end - start)) + "ms")

n_start = timer()
n_dot_product = np.array(a).dot(np.array(b))
n_end = timer()

print("\nn_dot_product = "+str(n_dot_product))
print("Computation time = " + str(1000*(n_end - n_start)) + "ms")