def insertionSort(arr):
    n = len(arr)
    
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]         
        j = i - 1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1]=key    


arr = [9,67,1,7,78,90]
insertionSort(arr)
print(arr)