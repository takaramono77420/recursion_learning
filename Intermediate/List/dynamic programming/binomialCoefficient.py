def binomialCoefficient(n,k):
    # 関数を完成させてください
    cache = []

    for i in range(n + 1):
        if i == 0:
            cache.append([1])
        else:
            coefficient = [1]
            for j in range(1, i):
                coefficient.append(cache[i - 1][j - 1] + cache[i - 1][j])
            coefficient.append(1)
            cache.append(coefficient)
    
    return cache[n][k]