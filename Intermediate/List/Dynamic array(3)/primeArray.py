def primeArray(n):
    # 関数を完成させてください
    array = []

    for i in range(2, n + 1):

        isPrime = True

        for j in range(2, i // 2 + 1):

            if i % j == 0:
                isPrime = False
                break
        
        if isPrime:
            array.append(i)
    
    return array
