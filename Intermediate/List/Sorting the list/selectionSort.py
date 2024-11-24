def selectionSort(arr):
    # 関数を完成させてください
    n = len(arr)

    for i in range(n):
        minIndex = i

        for j in range(i + 1, n):
            if arr[minIndex] >= arr[j]:
                minIndex = j
        
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp
    
    return arr