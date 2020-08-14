from time import perf_counter
from matplotlib import pyplot as plt
from scipy import linalg, float32, zeros
import numpy as np

#Para obtener la matriz laplaciana segun el tipo de dato
def matriz_laplaciana(N,dtype):
    
    A = zeros((N,N),dtype= dtype)
    
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A

Ns=[3,4,5,10,20,30,40,45,50,55,60,75,100,125,160,200,250,350,
    500,600,700,750,800
    ,900,1000,1500,2000, 2500,3000,3500,
    4000,4500,5000,5500,6000,7000,8000,9000,10000]


corridas = 10

nombres = ["A_invB_inv.txt", "A_invB_npsolve.txt"]
archivos=[]
for nombre in nombres:
    archivo = open(nombre,"w")
    archivos.append(archivo)
    
for N in Ns:
    dts=np.zeros((corridas,len(archivos)))
    for i in range(corridas):
        
        #metodo inversa
        A = matriz_laplaciana(N,float32)
        B=np.ones(N)
        t1 = perf_counter()
        C = np.linalg.inv(A)
        A_invB=C@B
        t2 = perf_counter()
        dt=t2-t1
        dts[i][0]=dt
        
        #metodo numpy
        A = matriz_laplaciana(N,float32)
        B=np.ones(N)
        t1 = perf_counter()
        A_invB=np.linalg.solve(A,B)
        t2 = perf_counter()
        dt=t2-t1
        dts[i][1]=dt
    promedio=[np.mean(dts[:,j]) for j in range(len(archivos))]
    
    for j in range(len(archivos)):
        archivos[j].write(f"{N} {promedio[j]}\n")
        archivos[j].flush()
        
[archivo.close() for archivo in archivos]

#grafico

x=[10,20,50,100,200,500,1000,2000,5000,10000] 
y1=[0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]    
yl=["0.1 ms","1 ms", "10 ms" , "0.1 s" , "1 s", "10 s", "1 min","10 min"] 

for nombre in nombres:
    datos=np.loadtxt(nombre)
    Ns=datos[:,0]
    dts=datos[:,1]
    plt.loglog(Ns,dts.T,"-o", label = nombre)
    plt.ylabel("Tiempo transcurrido")
    plt.xlabel("Tamaño matriz N")
    plt.title('Rendimiento Ax=b') 
    

    plt.xticks(x,x,rotation=60)
    plt.yticks(y1,yl)
    plt.grid(True)
plt.show()










