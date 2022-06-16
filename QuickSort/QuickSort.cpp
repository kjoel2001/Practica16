#include <iostream>
using namespace std;
#include <ctime>
unsigned t0, t1;
int partition(int arr[], int start, int end){
	int pivot = arr[end];
	int i = (start - 1);
	for (int j = start; j < end; j++) {
		if (arr[j] <= pivot) {
			i++;
			swap(arr[i], arr[j]);
		}
	}
	swap(arr[i + 1], arr[end]);
	return (i + 1);
}
void quickSort(int arr[], int start, int end){
	if (start >= end)
		return;
	int p = partition(arr, start, end);
	quickSort(arr, start, p - 1);
	quickSort(arr, p + 1, end);
}
int main(){
	int arr[] = { 9, 3, 4, 2, 1, 8 };
	int n = 6;
	t0=clock();
	quickSort(arr, 0, n - 1);
	t1 = clock();
	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
	double time = (double(t1-t0)/CLOCKS_PER_SEC);
	cout << "Execution Time: " << time << endl;
	return 0;
}
