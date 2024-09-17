def recursiveAddition(m,n):
    # 関数を完成させてください
    if n == 0:
        return m
    
    return 1 + recursiveAddition(m, n-1)