def squareSummation(n):
    # 関数を完成させてください
    if n == 1:
        return 1
    
    return pow(n, 2) + squareSummation(n - 1)