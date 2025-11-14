import numpy as np

A = np.array([[1,2],[3,4]])
B = np.ones((2,2)) # Array of 1s
Z = np.zeros((2,2)) # Array of zeros


I = np.eye(2) # Identity 
# result:
# [1 0]
# [0 1]


# additional options let you create a non-square matrix (nxm)
# and also let you shift the location of the diagonal that has the 1s
# creating a shift matrix: https://en.wikipedia.org/wiki/Shift_matrix
# you can multiply a matrix by one of these to shift its elements
I2 = np.eye(3, M=4, k=1)


D = np.diag((1,5,7,9)) # Diagonal Array
# result
# [1 0 0 0]
# [0 5 0 0]
# [0 0 7 0]
# [0 0 0 9]

""" Array Multiplication """
A*B      # Elementwise multiplication
A@B      # Matrix multiplication

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

r = v1.dot(v2)

A.dot(B) # Matrix multiplication in another way

""" Matrix Operatins """
# Using Linear Algebra submodule
np.linalg.det(A)  # Determinant of A
np.linalg.inv(A)  # Inverse of A
[evals, evecs] = np.linalg.eig(A) # Eigenvectors returned as columns


