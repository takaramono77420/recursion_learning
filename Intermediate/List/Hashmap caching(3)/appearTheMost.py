def appearTheMost(levels):
    # 関数を完成させてください

    hashMap = {}
    maxCount = 0
    cache = set(levels)

    for level in levels:

        if level not in hashMap:
            hashMap[level] = 1
        else:
            hashMap[level] += 1
            if hashMap[level] > maxCount:
                maxCount = hashMap[level]
                cache = [level]
            elif hashMap[level] == maxCount:
                cache.append(level)
    
    return sorted(cache)