def insertionSort(arr):
    # 関数を完成させてください
    n = len(arr)

    for i in range(n):
        currentValue = arr[i]

        for j in range(i - 1, -1, -1):

            if currentValue < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = currentValue
            else:
                break
    
    return arr