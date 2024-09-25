def squareSummation(n):
    # 関数を完成させてください
    answer = 1

    for i in range(2, n):
        answer = answer + pow(i, 2)
    
    return answer
