// C++ program for implementation of
// selection sort
#include <bits/stdc++.h>
#include <time.h>
using namespace std;
 
 
void llenar_lista(int lista[], int n){
	int mayor;
	srand(time(NULL));
	int listado = n+1;//Para que toma el 100, 1000, etc.
	//Llenar arreglo
	for(int i=0; i<n; i++){
		lista[i]=rand()%listado;
	}
}

//Swap function
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void selectionSort(int arr[], int n)
{
    int i, j, min_idx;
    
    for (i = 0; i < n-1; i++)
    {
        min_idx = i;
        for (j = i+1; j < n; j++)
        if (arr[j] < arr[min_idx])
            min_idx = j;
 
        swap(&arr[min_idx], &arr[i]);
    }
}
 
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}
 
int main()
{
	int cantidad = 10000;
	int lista[cantidad];
	llenar_lista(lista, cantidad);
	//printArray(lista,cantidad);
	clock_t inicio = clock();
    selectionSort(lista, cantidad);
    clock_t fin = clock() - inicio;
    cout << "Lista Ordenada: \n";
    //printArray(lista, cantidad);
    float FinMS = ((double)fin);
    cout<< "Tiempo de ejecucion:"<<FinMS<<endl;
    return 0;
}
//
