def fibonacciTotal(n):
    # 関数を完成させてください
    return fibonacciTotalHelper(0, 1, n, 0)
    

def fibonacciTotalHelper(Fn1, Fn2, n, total):
    total += Fn1
    if n < 1:
        return total

    return fibonacciTotalHelper(Fn2, Fn2+Fn1, n-1, total)
