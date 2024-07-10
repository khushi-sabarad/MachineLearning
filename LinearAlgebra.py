# Quantitative Lab
# Linear Algebra

import numpy as np
from numpy import linalg

# 7 tuple 1d array
a = np.array((1,2,3,4,5,6,7))
print(a)

# 2,4,7th array element
print(a[1])
print(a[3])
print(a[6])

# array shape
print(a.shape)

# 6D vector
v = np.array([[1,2,3,4,5,6]])

# array transpose 
t = v.T
print(t)
print(t.shape)

# 2D array transpose
x = np.array([[1,2,3],[3,2,1]])
y = x.T
print(x)
print(y)

# 7D array with 0s, 3d array with 1s
print(np.zeros(7))
print(np.ones(3)) 
print(np.array([[0,0,0,0,0,0,0]]*7))

# 4x5 matrix
m = np.array([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]])
print(m)

# matrix shape
print(np.shape(m))

# matrix transpose 
mt = m.T
print(mt)

# matrix first col
print(m[:,0])
# matrix first row
print(m[0,:])

# 2 non-square matrix that can be multiplied
m1 = np.array([[1,0,2],[0,1,3]])
m2 = np.array([[1,2],[2,1],[3,4]])
print(m1.shape)
print(m2.shape)

# matrix product
print(np.matmul(m1,m2))
#z=np.array([np.zeros(2)]*2)
#for i in range(len(m1)):
#    for j in range(len(m2[1])):
#        for k in range(len(m2)):
#            z[i][j] += m1[i][j] * m2[i][j]
#print(z)

# sum: two non square matrices of same order
x = np.array([[1,2,1],[2,1,2]])
y = np.array([[1,1,1],[2,2,3]])
print(x+y)

# Define a square matrix A.
a = np.matrix([[1,2],[3,4]])
a1 = np.array([[4,5],[6,7]])

# Print the identity matrix of the above order I.
i = np.array([[1,0],[0,1]])
print(i)

# Verify A.I = I.A for matrix multiplication.
print("A.I= ",a@i)
print("I.A= ",i@a)
print("A.I = I.A")

# Print the product of the matrices as matrix multiplication
print(a@a1)

# Print the product of the matrices by element wise multiplication
print(np.multiply(a,a1))

# Calculate and print the inverse of A. (Use linalg)Check if determinant is 0 Use if else statement to calculate inverse only when determinant is non zero
d = np.linalg.det(a)
print("Determinant: ",d)
if d != 0:
    print("Inverse: ", np.linalg.inv(a))
else:
    print("Inverse does not exist")
