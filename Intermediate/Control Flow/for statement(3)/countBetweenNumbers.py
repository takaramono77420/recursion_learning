def countBetweenNumbers(digit,idStart,idEnd):
    # 関数を完成させてください
    count = 0
    
    for i in range(idStart, idEnd+1):
        for j in str(i):
            if str(digit) == j:
                count += 1
    
    return count