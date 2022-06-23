# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:54:45 2022

@author: Kevin Linares
"""

import numpy as np
from matplotlib import pyplot as plt

#Resultado Python
yp = [8.6,
125.4,
724.2,
997.4,
1054.6,
1882.2,
2051.8,
2544.2,
2947.2,
2960,
3634.2,
7478.4,
11170,
16771.6,
20620.4] #Colocar los resultados obtenido del txt
xp = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado Goland
yg = [3.6,
51.6,
112.4,
187.2,
253.8,
296.2,
382.4,
428.4,
504.4,
652,
728.8,
1724.6,
2254.8,
4022,
3536] #Colocar los resultados obtenido del txt
xg = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado C++
yc = [4.8,
50.6,
98.4,
161.6,
214.2,
340.6,
409.4,
468.2,
523.8,
655.8,
696,
1514.8,
2203.8,
3090.4,
3913.4
] #Colocar los resultados obtenido del txt
xc =[100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


plt.plot(xp, yp, '-', label = 'python')
plt.plot(xg, yg, '-', label = 'Goland')
plt.plot(xc, yc, '-', label = "C++")
#plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6) #Para colorear debajo de las graficas

plt.legend()


plt.title("Gráfica de los Promedios Obtenidos: QuickSort")
plt.xlabel('cantidad de numeros')
plt.ylabel('tiempo')
plt.show()