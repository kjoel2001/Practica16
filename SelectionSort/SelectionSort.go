package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Generates a slice of size, size filled with random numbers
func llenar_lista(size int) []int {

	slice := make([]int, size, size)
	for i := 0; i < size; i++ {
		slice[i] = rand.Intn(size)
	}
	return slice
}

func selectionsort(items []int) {
	var n = len(items)
	for i := 0; i < n; i++ {
		var minIdx = i
		for j := i; j < n; j++ {
			if items[j] < items[minIdx] {
				minIdx = j
			}
		}
		items[i], items[minIdx] = items[minIdx], items[i]
	}
}
func main() {
	slice := llenar_lista(1000)
	//fmt.Println(slice)
	inicio := time.Now()
	//fmt.Println("\n--- Desordenada --- \n\n", slice)
	selectionsort(slice)
	//fmt.Println("\n--- Ordenada --- \n\n", slice)
	duracion := time.Since(inicio)
	fmt.Println("Tiempo en Microsegundos: ", duracion.Microseconds())
}
