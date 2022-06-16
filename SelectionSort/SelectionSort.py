from random import randint
from timeit import default_timer


def SelectionSort (array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j     
        array[i], array[min_idx] = array[min_idx], array[i]
    for i in range(len(array)):
        #print(array[i])
        print("%d" %array[i],end=" ")
 
def llenar_lista(n):
    lista=[]
    for i in range (n):
        lista.append(randint(1,n))
    return lista

#Crear lista de numeros
NUM = 1000
lista = llenar_lista(NUM)

inicio = default_timer()
SelectionSort(lista)
fin = default_timer()

resultadoTiempoS = fin - inicio
resultadoTiempoMS = resultadoTiempoS*1000000
print(" ")
print("PRUEBA 1: LISTA DE TAMAÑO:", NUM)
print("TIEMPO EN MICROSEGUNDOS => ",resultadoTiempoMS)#Tiempo en microsegundos





