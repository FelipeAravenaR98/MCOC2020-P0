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






