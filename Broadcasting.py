import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0,],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])


cal = A.sum(axis=0) #axis 0 = vertically, axis 1 = horizontally

percentage = 100* A/cal.reshape(1,4) #gives percentage of each value by column
 

########################tips and tricks to avoid bugs############################################

#constructing vectors

a = np.random.randn(5) #we don't want to do this !!!!!!!
#rank 1 array

a = np.random.randn(5,1) #do this instead

print("This is a: ", a)
print("This is the transpose: ", a.T)
print("The product is: ", np.dot(a,a.T))


