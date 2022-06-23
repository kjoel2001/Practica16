# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:54:45 2022

@author: Kevin Linares
"""

import numpy as np
from matplotlib import pyplot as plt

#Resultado Python
yp = [1.140175425,
13.01153335,
138.9863303,
46.80064102,
22.41205033,
125.0167989,
57.46912214,
308.7801807,
456.7643813,
187.2605137,
375.2401897,
287.1224477,
763.6835077,
501.6540641,
457.2540869

] #Colocar los resultados obtenido del txt
xp = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado Goland
yg = [0.547722558,
4.979959839,
13.24009063,
16.88786547,
30.41710045,
21.56849554,
45.83448483,
58.12314513,
76.49052229,
68.42879511,
162.3135854,
534.9124227,
256.8291261,
1324.914714,
540.2712282

] #Colocar los resultados obtenido del txt
xg = [100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


#Resultado C++
yc = [0.836660027,
12.95376393,
5.594640292,
7.602631123,
7.949842766,
11.23832728,
22.68920448,
29.52456604,
32.01093563,
66.6610831,
47.09033871,
95.41331144,
163.660319,
237.0259479,
130.607427
] #Colocar los resultados obtenido del txt
xc =[100,1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 , 50000]


plt.plot(xp, yp, '-', label = 'python')
plt.plot(xg, yg, '-', label = 'Goland')
plt.plot(xc, yc, '-', label = "C++")
#plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6) #Para colorear debajo de las graficas

plt.legend()


plt.title("Gráfica de los Desviacion: QuickSort")
plt.xlabel('cantidad de numeros')
plt.ylabel('tiempo')
plt.show()