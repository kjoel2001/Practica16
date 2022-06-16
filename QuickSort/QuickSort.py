import time
def partition(arr,start,end):
  pivot = arr[end]
  i = start - 1
  for j in range(start, end):
    if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
  return i + 1

def quickSort(arr,start,end):
    if (start >= end):
        return
    p=partition(arr,start,end)
    quickSort(arr,start,p-1)
    quickSort(arr,p+1,end)
    

arr = [ 9, 3, 4, 2, 1, 8 ]
n = len(arr)
inicio = time.time()
quickSort(arr, 0, n - 1)
fin = time.time()
print(arr)
print("Execution Time:",fin-inicio) 


