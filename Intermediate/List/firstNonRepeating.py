def firstNonRepeating(s):
    # 関数を完成させてください

    countMap = {}

    for q in s:countMap[q] = countMap.get(q, 0) + 1

    for i in range(len(s)):
        if countMap.get(s[i]) == 1:
            return i
    
    return -1