import math

def sumOfAllPrimes(n):
    # 関数を完成させてください
    
    return sum(primeList(n))
            

def primeList(n):
    cache = [True]*(n+1)
    for index in range(2, math.ceil(math.sqrt(n+1))):
        if not cache[index]:
            continue
        
        j = 2
        jp = j * index

        while jp <= n:
            cache[jp] = False
            j = j + 1
            jp = j * index
    
    list = []
    for i, value in enumerate(cache):
        if value:
            list.append(i)

    return list[2:]