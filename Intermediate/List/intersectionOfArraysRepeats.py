def intersectionOfArraysRepeats(intList1,intList2):
    # 関数を完成させてください

    intMap2 = {}
    cache = []

    for num in intList2:intMap2[num] = intMap2.get(num, 0) + 1

    for num in intList1:

        if intMap2.get(num, 0) != 0:
            cache.append(num)
            intMap2[num] = intMap2.get(num) - 1
    
    return sorted(cache)