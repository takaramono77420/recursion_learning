def hasSameStructure(inputChar,wordList):
    # 関数を完成させてください
    wordList = wordList.split(' ')

    if len(wordList) != len(inputChar):return False

    hashMap = {}

    for i in range(len(inputChar)):
        char = inputChar[i]
        word = wordList[i]

        if (char in hashMap and hashMap.get(char) != word) \
            or (word in hashMap.values() and char not in hashMap):
            return False
            
        hashMap[char] = word

    return True