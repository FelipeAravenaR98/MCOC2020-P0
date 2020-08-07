from scipy import matmul, rand
from time import perf_counter
from matplotlib import pyplot as plt

#Generador de Archivos de Texto

Ns=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,
    500,600,800,1000,2000,5000]

corridas = 10

for corrida in range(corridas):
    corrida=corrida+1
    texto = open(f"corrida {corrida}.txt","w")
    #texto.write(f"corrida {corrida} \n")

    for tamaño in Ns:
        N=tamaño
    
        A = rand(N,N)
        B = rand(N,N)
        
        t1 = perf_counter()
        C = A@B        #Python 3.5 o mas define el operador `@` como multiplicacion de matrices. 
        			   # Si no le funciona, usar la funcion `matmul`
        			   #
        			   # Se recomienda no usar la clase 'matrix'.
        			   #
        #C = matmul(A,B)
        t2 = perf_counter()
        
        dt = t2 - t1
        mem=3*(N**2)*8
        texto.write(f"{N} {dt} {mem} \n")
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
plt.title('Rendimiento A@B')    


plt.subplot(2,1,2)#para graficar memoria
for corrida in range(corridas):
    corrida=corrida+1
    lista_m=[]
    
    texto=open(f"corrida {corrida}.txt")
    for linea in texto:
        
        lista_m.append(float(linea.split()[2]))
    
    texto.close()    
    plt.loglog(Ns,lista_m,"-o")
plt.axhline(8000000000,linestyle="--",color="k")
    
y2=[10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
yl2=["1 kb","10 kb","100 kb", "1 mb", "10 mb", "100 mb", "1 gb", "10 gb", "100 gb"]    
   
plt.xticks(x,x,rotation=60)
plt.yticks(y2,yl2)
plt.grid(True)


plt.xlabel('Tamaño matriz N')
plt.ylabel('Uso de memoria')
   
    
plt.show
























