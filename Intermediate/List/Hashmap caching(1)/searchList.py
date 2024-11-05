def searchList(numList,value):
    # 関数を完成させてください
    hashMap = {}

    for index, num in enumerate(numList):
        hashMap[num] = index
    
    return hashMap.get(value, -1)