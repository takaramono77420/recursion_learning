def findPairs(numbers):
    # 関数を完成させてください

    numbersHashMap = {}
    cache = []

    for number in numbers:numbersHashMap[number] = numbersHashMap.get(number, 0) + 1

    for number in numbersHashMap:
        if numbersHashMap.get(number) == 2:
            cache.append(number)
    
    return sorted(cache)