def longestSubstringLength(password):
    # 関数を完成させてください

    hashMap = {}
    maxLength = 0
    cache = []
    index = 0

    for char in password:

        if char in hashMap.keys():
            cache = cache[hashMap.get(char)+1:]
            hashMap = {c: i for i, c in enumerate(cache)}
            index = len(cache)
        
        cache.append(char)

        if maxLength < len(cache):maxLength = len(cache)
        
        hashMap[char] = index

        index += 1
    
    return maxLength