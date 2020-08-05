
#Multiplicación de arreglos

import scipy as sp

N = 3

A = sp.matrix(sp.rand(N,N))
B = sp.matrix(sp.rand(N,N))

print(f"A = \n{A}")
print(f"B = \n{B}")

C = A*B     #multiplicacion de arreglos 




print("C= ")
print(C)




