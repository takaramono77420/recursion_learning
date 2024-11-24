import math
def sumOfArrayHelper(arr, start, end):
    if start == end:return arr[start]

    mid = math.floor((start + end) / 2)

    left = sumOfArrayHelper(arr, start, mid)
    right = sumOfArrayHelper(arr, mid + 1, end)
    
    return left + right


def sumOfArray(arr):
    # 関数を完成させてください
    return sumOfArrayHelper(arr, 0, len(arr)-1)