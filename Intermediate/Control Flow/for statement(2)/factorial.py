def factorial(n):
    # 関数を完成させてください
    product = 1

    for i in range(2,n + 1):

        product = product * i
    
    return product
