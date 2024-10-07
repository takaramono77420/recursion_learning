def charInBagOfWordsCount(bagOfWords,keyCharacter):
    # 関数を完成させてください
    count = 0

    for string in bagOfWords:
        count += string.count(keyCharacter)
    
    return count