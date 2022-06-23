# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:54:45 2022

@author: Kevin Linares
"""

import numpy as np
from matplotlib import pyplot as plt

#Resultado Python
yp = [4.159326869,
51.15955434,
31.65438358,
51.14000391,
97.49102523,
222.1594022,
113.7949911,
278.144387,
149.1100265,
798.6805995,
498.0796121,
1031.575736,
5725.780951,
2155.831812,
7948.415742

] #Colocar los resultados obtenido del txt
xp = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado Goland
yg = [2.50998008,
341.7787296,
2257.861754,
2983.30751,
34490.72102,
29988.1491,
31987.69164,
33805.23364,
32012.51531,
44099.19128,
37732.82274,
106484.651,
151179.4078,
352216.367,
384072.5601

] #Colocar los resultados obtenido del txt
xg = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado C++
yc = [0.707106781,
70.72835358,
237.7526025,
333.1961885,
631.8806849,
707.3996042,
2099.758486,
2446.426925,
3402.368249,
2624.356816,
2449.988306,
27199.95901,
31136.32812,
10903.85188,
83483.06285,
] #Colocar los resultados obtenido del txt
xc =[100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


plt.plot(xp, yp, '-', label = 'python')
plt.plot(xg, yg, '-', label = 'Goland')
plt.plot(xc, yc, '-', label = "C++")
#plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6) #Para colorear debajo de las graficas

plt.legend()


plt.title("Gráfica de los Desviacion: SelectionSort")
plt.xlabel('cantidad de numeros')
plt.ylabel('tiempo')
plt.show()
