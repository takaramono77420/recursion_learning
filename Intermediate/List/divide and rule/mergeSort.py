import math

def mergeSortHelper(arr, start, end):

    if start == end:return [arr[start]]

    mid = math.floor((start + end)/2)

    leftArr = mergeSortHelper(arr, start, mid)
    rightArr = mergeSortHelper(arr, mid + 1, end)

    leftArr.append(math.inf)
    rightArr.append(math.inf)
    mergedArr = []

    li = 0
    ri = 0

    while li + ri < len(leftArr) + len(rightArr) -2:
        if leftArr[li] <= rightArr[ri]:
            mergedArr.append(leftArr[li])
            li += 1
        else:
            mergedArr.append(rightArr[ri])
            ri += 1
    
    return mergedArr

def mergeSort(arr):
    # 関数を完成させてください
    return mergeSortHelper(arr, 0, len(arr) - 1)