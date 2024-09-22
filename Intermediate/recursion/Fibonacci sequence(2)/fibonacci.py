def fibonacci(n):
    # 関数を完成させてください
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)