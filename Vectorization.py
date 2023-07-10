import numpy as np 
import time

a = np.array([1,2,43,6,8])
print(a)

a = np.random.rand(10000000)
b = np.random.rand(10000000)


tic = time.time() #vectorized version
vectorized = np.dot(a,b)
toc = time.time()

print(vectorized)
print("vectorized version: " + str(1000*(toc-tic))+ " ms")

c = 0
tic = time.time() #for loop time
for i in range(1000000):
    c += a[i]*b[i] 
toc = time.time()

print(c)
print("for loop: " + str(1000*(toc-tic))+ " ms")




U = np.zeros((1)) #create new array filled woth 0's (floating point)