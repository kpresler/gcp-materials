import numpy as np

print("""
Part A
""")
a = np.arange(1,49).reshape(3,4,4)
print("a =\n", a)

print("\na.")
print(a[1,0,3])

print("\nb.")
print(a[0,2,:])


print("\nc.")
print(a[2,:,:])

print("\nd.")
print(a[:,1,0:2])

print("\ne.")
print(a[2,:,3:1:-1])

print("\nf.")
print(a[:,::-1,0])

print("\ng.")
print(a[[0,2],[0,3],::3])


print("""
Part B
""")

L = 1
xValues = np.linspace(0,1,101)
nValues = np.linspace(1,5,5)

n, x = np.meshgrid(nValues,xValues)

lamda_n = 2*L / n


f = x * (L- x)* np.sin(2*np.pi*x / lamda_n)

min_i = f.argmin(axis=0)
max_i = f.argmax(axis=0)
print(min_i, max_i)




    
    

