from time import perf_counter
from matplotlib import pyplot as plt
from scipy import matmul, rand, float32, zeros,float16
import numpy as np
import sys
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
    500,600,700,750,800,900,1000,1500,1700]

corridas = 1

for corrida in range(corridas):
    corrida=corrida+1
    texto = open(f"corrida {corrida}.txt","w")
    #texto.write(f"corrida {corrida} \n")

    for tamaño in Ns:
        N=tamaño
        A = matriz_laplaciana(N,np.double)
        
        t1 = perf_counter()
        C = np.linalg.inv(A)       
        t2 = perf_counter()
        
        dt = t2 - t1
        mem=sys.getsizeof(C) 
        texto.write(f"{N} {dt} {mem} \n")
        #print(mem)
        #print (N)
        #print(f"Tiempo transcurrido = {dt} s")

    texto.close()


#Lector de Arcivos de Texto
plt.subplot(2,1,1) #para graficar tiempo
for corrida in range(corridas):
    corrida=corrida+1
    
    lista_T=[]
    texto=open(f"corrida {corrida}.txt")
    for linea in texto:
        lista_T.append(float(linea.split()[1]))
        
    
    texto.close()
    
    #grafica la matriz vs tiempo 
    
    
    plt.loglog(Ns,lista_T,"-o")
    
    
x=[10,20,50,100,200,500,1000,2000,5000,10000] 
y1=[0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10]    
yl=["0.1 ms","1 ms", "10 ms" , "0.1 s" , "1 s", "10 s", "1 min"] 
   

plt.xticks(x,[])
plt.yticks(y1,yl)
plt.grid(True)



plt.ylabel('Tiempo transcurrido')
plt.title('Rendimiento INV caso 1 double')    


plt.subplot(2,1,2)#para graficar memoria
for corrida in range(corridas):
    corrida=corrida+1
    lista_m=[]
    
    texto=open(f"corrida {corrida}.txt")
    for linea in texto:
        
        lista_m.append(float(linea.split()[2]))
    
    texto.close()    
    plt.loglog(Ns,lista_m,"-o")
plt.axhline(8000000000,linestyle="--",color="r")
    
y2=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
yl2=["1 kb","10 kb","100 kb", "1 mb", "10 mb", "100 mb", "1 gb", "10 gb", "100 gb"]    
   
plt.xticks(x,x,rotation=60)
plt.yticks(y2,yl2)
plt.grid(True)


plt.xlabel('Tamaño matriz N')
plt.ylabel('Uso de memoria')
   
    
plt.show



























