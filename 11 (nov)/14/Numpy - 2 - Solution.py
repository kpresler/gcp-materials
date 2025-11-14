import numpy as np

print("Part A: Matrix vs elementwise product")
M = np.array([[2,3,-15], [-5,7,22],[11,0,3]])
N = np.array([[1,7,5], [-2, 8, -6], [9, -4, 3]])
print("M+N = \n", M+N)
print("np.dot(M,N) =\n",np.dot(M,N) )
print("M@N =\n",M@N)
print("M*N =\n",M*N)



print("\nPart B: Calculate the inverse of M")
print("inv(M) =\n", np.linalg.inv(M))



print("""\nPart C: Solve system of equations
   3x + y - z = 25
      8x + 3z = 41
2x -  5y - 4z = 39
""")
A = np.array([[3, 1, -1],
              [8, 0, 3],
              [2, -5, -4]])
B = np.array([[25],
              [41],
              [39]])
X = np.linalg.inv(A)@B
print("x =",X[0,0])
print("y =",X[1,0])
print("z =",X[2,0])


print("\nPart D: Determinant of C")
C = np.arange(16).reshape((4,4))
print("C =\n",C)
print("|C| =",np.linalg.det(C))



print("\nPart E: Check if monotonically increasing")
D = np.arange(1,10)
print(" D = ",D)
print(" It is ",np.all(np.diff(D)>=0),"that D is monotonically increasing.")



print("\nPart F: Shoelace Algorithm")

def shoeLaceAlg(a):

    b = np.concatenate([a,a[0,:].reshape(1,2)])
    xcoords = b[:,0]
    ycoords = b[:,1]

    S1 = np.dot(xcoords[0:-1],ycoords[1:])
    S2 = np.dot(xcoords[1:],ycoords[0:-1])                   

    return 0.5*np.abs(S1-S2)


    
a = np.array([[0.,0.],[2.,5.],[5.,5.],[7.,0.],[5.,-5.],[2.,-5.]])
print(shoeLaceAlg(a) ) 

