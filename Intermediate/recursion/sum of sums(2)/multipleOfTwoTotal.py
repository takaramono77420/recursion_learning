def sumOfMultipleOfTwo(n):

    if n <= 1:
        return 2 * n
    
    return 2 * n + sumOfMultipleOfTwo(n - 1)


def multipleOfTwoTotal(n):
    # 関数を完成させてください
    if n <= 1:
        return sumOfMultipleOfTwo(n) 
    
    return sumOfMultipleOfTwo(n) + multipleOfTwoTotal(n - 1)
