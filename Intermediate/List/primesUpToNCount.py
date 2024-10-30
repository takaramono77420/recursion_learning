import math

def primesUpToNCount(n):
    # 関数を完成させてください

    cache = [True] * n

    for i in range(2, math.ceil(math.sqrt(n))):

        if not cache[i]:
            continue
        
        j = 2
        multiple = i * j

        while multiple < n:
            cache[multiple] = False
            j += 1
            multiple = i * j

    return cache[2::].count(True)