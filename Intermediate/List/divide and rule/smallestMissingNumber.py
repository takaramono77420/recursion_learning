import math
def smallestMissingNumberHelper(arr, start, end):

    if start == end:
        if arr[start] != start:
            return start
        else:
            return None

    mid = math.floor((start + end) / 2)

    left = smallestMissingNumberHelper(arr, 0, mid)
    right = smallestMissingNumberHelper(arr, mid + 1, end)

    return left if left != None else right


def smallestMissingNumber(arr):
    # 関数を完成させてください

    missingNum = smallestMissingNumberHelper(arr, 0, len(arr)-1)

    return missingNum if missingNum != None else len(arr)