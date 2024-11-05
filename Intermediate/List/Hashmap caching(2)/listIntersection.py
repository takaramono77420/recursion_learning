def listIntersection(targetList,searchList):
    # 関数を完成させてください
    hashMap = {}
    searchListIndex = []

    for index, value in enumerate(targetList):
        hashMap[value] = index

    searchList = set(searchList)

    for value in searchList:

        if hashMap.get(value) != None:
            searchListIndex.append(value)
    
    return sorted(searchListIndex)