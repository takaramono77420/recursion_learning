import math
def doubleArrayHelper(arr, start, end):
    if start == end:
        arr[start] = arr[start] * 2
        return arr

    mid = math.floor((start+end)/2)

    doubleArrayHelper(arr, start, mid)
    doubleArrayHelper(arr, mid+1, end)

    return arr


def doubledArray(arr):
    # 関数を完成させてください
    return doubleArrayHelper(arr, 0, len(arr)-1)