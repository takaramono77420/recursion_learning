def longestPalindromeLength(string):
    # 関数を完成させてください
    elementsString = set(string)
    hashMap = {char: string.count(char) for char in elementsString}
    count = 0

    for char in elementsString:
        count += hashMap.get(char) // 2 * 2
    
    if count < len(string):count += 1

    return count

        



