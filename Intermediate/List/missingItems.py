def missingItems(listA,listB):
    # 関数を完成させてください

    hashMap = {item: index for index, item in enumerate(listB)}
    cache = []

    for item in listA:

        if item not in hashMap:cache.append(item)
        
    return cache