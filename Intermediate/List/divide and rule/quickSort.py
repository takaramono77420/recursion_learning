import random

def quickSort(arr):
    # 関数を完成させてください
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr

def quickSortHelper(arr, start, end):

    if start >= end:return

    pivotIndex = partition(arr, start, end)

    quickSortHelper(arr, start, pivotIndex - 1)
    quickSortHelper(arr, pivotIndex + 1, end)

def partition(arr, start, end):
    
    pivot = random.randint(start, end)

    arr[pivot], arr[end] = arr[end], arr[pivot]

    for i in range(start, end + 1):

        for j in range(i, end + 1):

            if arr[j] < arr[end]:
                arr[i], arr[j] = arr[j], arr[i]
                break
            
            if j == end:
                arr[i], arr[end] = arr[end], arr[i]
                return i
    
            
    

                





