def summationOfSummation(n):
    # 関数を完成させてください
    answer = 0

    for i in range(0, n+1):
        total = 0
        for j in range(0, i+1):
            total += j
        
        answer += total
    
    return answer
