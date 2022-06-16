package main

import (
	"fmt"
	"time"
)

func partition(arr []int, start, end int) int {
	var pivot int = arr[end]
	var i, j int = (start - 1), start
	for j < end {
		if arr[j] <= pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
		j++
	}
	arr[i+1], arr[end] = arr[end], arr[i+1]
	return i + 1
}
func quickSort(arr []int, start, end int) {
	if start >= end {
		return
	}
	var p int = partition(arr, start, end)
	quickSort(arr, start, p-1)
	quickSort(arr, p+1, end)
}
func main() {
	arr := []int{9, 3, 4, 2, 1, 8}
	var n int = 6
	start := time.Now()
	quickSort(arr, 0, n-1)
	timeElapsed := time.Since(start)
	for i := 0; i < n; i++ {
		p := arr[i]
		fmt.Println(p)
	}
	fmt.Printf("Execution Time: %s", timeElapsed)
}
