import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0,],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])


cal = A.sum(axis=0) #axis 0 = vertically, axis 1 = horizontally

percentage = 100* A/cal.reshape(1,4) #gives percentage of each value by column
 

######################## tips and tricks to avoid bugs ############################################

#constructing vectors

a = np.random.randn(5) #we don't want to do this !!!!!!!
#rank 1 array

a = np.random.randn(5,1) #do this instead. is more explicit

#print("This is a: ", a)
#print("This is the transpose: ", a.T)
#print("The product is: ", np.dot(a,a.T))


ex = np.array([[2,1],[1,3]])
ans = np.dot(ex,ex)



a = np.random.randn(3,3)
b = np.random.randn(3,1)
c = a+b



a = np.array([[1,1],[1,-1]])
b = np.array([[2],[3]])
n = a + b
print(n)


A = np.random.rand(4,3)
B = np.sum(A, axis = 1, keepdims=True)

print("The shape is: ", np.shape(B))