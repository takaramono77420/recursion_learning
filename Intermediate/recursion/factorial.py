def factorial(n):
    # 関数を完成させてください
    if n == 1:
        return 1
    
    return n * factorial(n - 1)