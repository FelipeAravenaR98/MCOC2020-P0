# MCOC2020-P0
Marca/modelo: Asus Vivobook pro N580GD

Tipo: Notebook

Año adquisición: 2018

###### Procesador:

Marca/Modelo: Intel Core i5-8300H

Velocidad Base: 2.30 GHz

Velocidad Máxima: 4.00 GHz

Numero de núcleos: 4

Humero de hilos: 8

Arquitectura: x86_64

Set de instrucciones: MMX,SSE,SSE3,SSSE3,SSE4.1,SSE4.2,EM64T,VT-x,AES,AVX,AVX2,FMA3.

Tamaño de las cachés del procesador

L1d: 32KB
L1i: 32KB
L2: 256KB
L3: 8192KB

###### Memoria

Total: 8 GB

Tipo memoria: DDR4

Velocidad 2400 MHz

Numero de (SO)DIMM: 2

###### Tarjeta Gráfica

Marca / Modelo: Nvidia GeForce GTX 1050

Memoria dedicada: 4096 MB

Resolución: 1920 x 1080

###### Disco 1:

Marca: Toshiba

Tipo: HDD

Tamaño: 1TB

Particiones: 4

Sistema de archivos: NTFS,FAT, FAT32, exFAT, ReFS

Dirección MAC de la tarjeta wifi: 0C-9D-92-32-B4-3F

Dirección IP (Interna, del router): 192.168.1.4

Dirección IP (Externa, del ISP): 2620:9b::1914:1625

Proveedor internet: GTD Manquehue

# Desempeño MATMUL

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P0/blob/master/Rendimiento%20A%40B.png?raw=true)

###### 1
El gráfico difiere solo en los tiempos transcurridos ya que en el de uso de memoria solo depende de los valores de N y utilizamos valores similares. En cuanto al tiempo, para los primeros valores de N en mi caso demora mucho más y la mayor densidad de puntos se dan bajo los 1ms a diferencia del gráfico del profesor.
###### 2
El peak inicial se puede deber a la velocidad del procesador y luego, para mayores valores de N, la velocidad de las frecuencas RAM pasan a ser más importantes. Esto debido a que la Ram funciona como un puente entre el disco duro y el procesador siendo una memoria volátil. Entonces debido a que yo tengo mayor frecuencia con respecto a la del profesor (2400 mhz y es gddr4), entonces entregará los datos para procesar a mayor velocidad. Sin embargo como tengo menor memoria, a valores de N más altos que sobrepasen mi ram no los podré procesar igual que el profesor.
###### 3
El gráfico de tiempo no es lineal y aumenta al aumentar el valor de N debido probablemente a que se forma una especie de cuello de botella en el procesador, donde la memoria quese usa es tanta que el procesador no alcanza a recibir todos los datos para procesarlos formando una cola y aumentando el tiempo de ejecución. En el caso de la memoria es lineal debidoa que solo depende del tamaño de las matrices al cuadrado.
###### 4
versión de python: 3.7
###### 5
version de numpy:1.16.4

###### 6
Sí se utiliza más de un procesador. La primera imagen muestra el uso de los núcleos del cpu sin correr el programa y la segunda corriendo el programa. Se utiliza el software cpuid hwmonitor donde la primera columna es el uso de cpu actual, la segunda el valor minimo desde q se inicio el software y la tercera el valor máximo desde que se inicio el software, por lo que debemos fijarnos en la primera.

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P0/blob/master/cpu%20sin%20programa.JPG?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P0/blob/master/cpu%20con%20programa.JPG?raw=true)

# Desempeño MIMATMUL

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P0/blob/master/Rendimiento%20A%40B%20mimatmul.png?raw=true)

###### 1
El gráfico difiere principalmente en los tiempos de demora ya que, utilizando la función mimatmul, el programa tarda mucho más debido a que no es el programa óptimo para este tipo de cálculos. Sin embargo se puede notar que al comienzo o con matrices pequeñas es más rápido que con la funciom matmul.
###### 2
Estas diferencias como ya se comentó, se deben a que el programa hecho por mi no es el óptimo. Por otro lado (y como se verá mas adelante) no se utilizan todos los procesadores como en la implementación anterior. Cabe destacar, que para saber a ciencia cierta las razones de las diferencias, se deberá observar que ocurre o como funciona matmul.
###### 3
En este caso ambos son practicamente lineales, aunque al comienzo para matrices pequeñas la demora es mínima por lo que se ve esa línea horizontal.
###### 4
versión de python: 3.7
###### 5
version de numpy:1.16.4

###### 6
Sí se utiliza más de un procesador. La primera imagen muestra el uso de los núcleos del cpu sin correr el programa y la segunda corriendo el programa. Se utiliza el software cpuid hwmonitor donde la primera columna es el uso de cpu actual, la segunda el valor minimo desde q se inicio el software y la tercera el valor máximo desde que se inicio el software, por lo que debemos fijarnos en la primera. Para este caso sería mejor hacer un benchmark en vídeo ya que se podrá ver que se activan y desactivan los procesadores, por lo que la cantidad de estos que estan en uso varía constantemente. Además, en general hay menor uso de procesador que en la entrega pasada.

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P0/blob/master/cpu%20sin%20programa%20mimatmul.JPG?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P0/blob/master/cpu%20con%20programa%20mimatmul.JPG?raw=true)


# Desempeño INV

Como era de esperar, en el caso de los datos half se utiliza menor memoria y en los longdouble mayor. Esto ocurre debido a que a mayor tamaño de bits en el tipo de dato, mayor memoria se utiliza. Con respecto a las funciones de inversión de matrices, se puede ver que utilizando numpy se esperan mayores tiempos de ejecución en comparación a scipy (no muy relevantes) Además, entre las funciones Scipy la mayor rapidez y menor uso de memoria se alcanza con el parametro de overwrite = True porque se descartan algunos datos d la matriz que es invertida.

###### 1
El método de numpy utiliza el método de diagonalizar (RREF) que es más lento que el que utiliza Scipy. Éste debe ser utilizando la adjunta y el determinante por lo que es más rápido que los métodos de mumpy.

###### 2

Como se comentó en la clase, las memorias del procesador son las más rápidas del sistema por lo que a mayor memoria caché (en especial si es del tipo L3) los tiempos de ejecución disminuyen. Sumado a esto, tener más nucleos en el procesador permite hacer cálculos en paralelo y aumentar la velocidad. Esto se ven en los gráficos de desempeño cuando se superan las memorias cache los tiempos de ejecucion tienen peaks o aumentan hasta llegar a sobrepasar la memoria Ram, en donde se siguen almacenando datos pero en el disco duro (hdd o ssd) lo cual es muy lento y se intenta evitar.


# Desempeño Ax = b (Parte 1)

Como era de esperar, los calculos invirtiendo la matriz tarda más que en el caso del solve probablemente debido a que el solve utiliza ciertos métodos numéricos o aproximaciónes numéricas para resolver el problema más rápidamente. Se puede ver que hay grandes peaks en el método de inversión de matriz probablemente provocados por los rendimientos en las últimas corridas que son más lentas por "arrastre de cálculos anteriores".

# Desempeño Ax = b (Parte 2)

A continuación se puede ver el gráfico pedido:

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P0/blob/master/Entrega%206/Desempe%C3%B1o%20invB.png?raw=true)

El resultado es el esperado, obteniendo uno muy similar al entregado en el encunciado donde el método más lento y menos optimizado o adecuado para el cálculo es el de la inversa, mientras que el más rápido para matrices grandes es solver de scipy con pos y overwrite activados y el más rápido en matrices pequeñas es el solver de numpy.

