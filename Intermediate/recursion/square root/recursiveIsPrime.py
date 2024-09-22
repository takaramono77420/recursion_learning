def recursiveIsPrimeHelper(n, denominator):

    if n / 2 < denominator:
        return True
    elif n % denominator == 0:
        return False
    
    return recursiveIsPrimeHelper(n, denominator + 1)

def recursiveIsPrime(n):
    # 関数を完成させてください
    if n <= 1:
        return False
    
    return recursiveIsPrimeHelper(n, 2)