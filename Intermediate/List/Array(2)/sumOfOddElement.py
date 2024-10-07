def sumOfOddElement(arr):
    # 関数を完成させてください
    total = 0

    for i in arr:
        if i % 2 != 0:
            total += i
    
    return total


