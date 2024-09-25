def fibonacci(n):
    # 関数を完成させてください
    fn1 = 0
    fn2 = 1

    for i in range(n):
        tmp = fn2
        fn2 = fn1 + fn2
        fn1 = tmp
    
    return fn1