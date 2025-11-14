import numpy as np

A = np.array([[1,2,3],[4,5,6], [7,8,9]])
A.shape

"""Slicing"""
A[0] # 0th row
A[-1] # last row

A[0,:] # 0th row
A[0,0:2] # 0th-1st column 0th row

A[:,0] # 0th column
A[1:3,0] #1st and 2nd row 0th column


A[0,0] = 5 # Assignment

""" Looping """
for row in A: print(row)
A.T # Transpose of A (swaps rows with columns)
for col in A.T: print(col)

""" Creating Arrays """
Z = np.zeros([2,5]) # Array filled with zeros
W = np.ones([3,3])  # Array filled with ones

# Use the arange function to create integer arrays np.arrange(start, stop, step)
M = np.arange(0,12) # The Array Range method

M.shape
M = M.reshape([3,4])    # Reshape array 
# M.reshape(3,4)        ##WRONG
M.shape

""" Array arithmatic """
A
W

A+3 # Scalar addition
A+W # Array addition
A*W # Elementwise multiplication

# Sum functions
M
np.sum(M,0) # Sum of rows
np.sum(M,1) # Sum of columns

np.argmin(M,0)
np.argmax(M,1)


""" Linspace and Meshgrid """
# Use the linspace method to create linearly spaced values np.linspace(start, stop, number)
x = np.linspace(0,1,11)
y = np.arange(2,4,0.25)

# Use meshgrid
(X, Y) = np.meshgrid(x,y)
Z = X**2 + Y**2
