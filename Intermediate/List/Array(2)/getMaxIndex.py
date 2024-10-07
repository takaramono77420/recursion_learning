def getMaxIndex(arr):
    # 関数を完成させてください

    return len(arr) - arr[::-1].index(max(arr)) - 1