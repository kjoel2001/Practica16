# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:54:45 2022

@author: Kevin Linares
"""

import numpy as np
from matplotlib import pyplot as plt

#Resultado Python
yp = [11.6,
641.6,
2327,
5144.6,
9272,
14185.4,
20423.4,
27759.4,
35948.6,
46738.8,
56727.6,
231739,
521820,
968394.6,
1505606.6
] #Colocar los resultados obtenido del txt
xp = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado Goland
yg = [10.4,
1128.2,
4464.8,
8950.2,
38805,
28182.2,
45195.4,
54200,
108515.8,
137618.2,
144222.8,
689240.4,
1312794,
2204782.2,
3223559.8
] #Colocar los resultados obtenido del txt
xg = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado C++
yc = [8,
386,
1459.6,
2583.2,
4068.8,
6086.8,
9592.2,
14713.2,
17671.2,
19037.2,
24898.2,
104767.6,
109508,
85513.6,
702579.6


] #Colocar los resultados obtenido del txt
xc =[100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


plt.plot(xp, yp, '-', label = 'python')
plt.plot(xg, yg, '-', label = 'Goland')
plt.plot(xc, yc, '-', label = "C++")
#plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6) #Para colorear debajo de las graficas

plt.legend()


plt.title("Gráfica de los Promedios Obtenidos: SelectionSort")
plt.xlabel('cantidad de numeros')
plt.ylabel('tiempo')
plt.show()