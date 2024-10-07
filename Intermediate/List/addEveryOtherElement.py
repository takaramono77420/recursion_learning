def addEveryOtherElement(intArr):
    # 関数を完成させてください
    total = 0

    for i in range(0, len(intArr), 2):
        total += intArr[i]
    
    return total