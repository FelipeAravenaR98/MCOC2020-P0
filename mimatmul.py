from scipy import matmul, rand
from numpy import *

def mimatmul(A,B):
    C=[]

    for a in range(len(A)):
        C.append([0]*(len(A)))
    
    for a in range(len(A)):
        for b in range(len(B)):
            for c in range(len(B)):
                C[a][b]+=A[a][c]*B[c][b]
    return array(C)
"""
N=200
A=rand(N,N)
B=rand(N,N)

print(mimatmul(A,B))
"""
