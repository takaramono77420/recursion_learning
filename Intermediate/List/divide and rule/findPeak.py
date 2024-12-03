import math
def findPeakHelper(arr, start, end):
    
    mid = math.floor((start+end)/2)

    if end - start <= 1:
        if arr[start] > arr[end]:
            return arr[start]
        else:
            return arr[end]

    if arr[mid] < arr[mid - 1]:
        return findPeakHelper(arr, start, mid - 1)
    elif arr[mid] < arr[mid + 1]:
        return findPeakHelper(arr, mid + 1, end)
    else:
        return arr[mid]

def findPeak(arr):
    # 関数を完成させてください
    if len(arr) == 1:return arr[0]
    return findPeakHelper(arr, 0, len(arr) - 1)