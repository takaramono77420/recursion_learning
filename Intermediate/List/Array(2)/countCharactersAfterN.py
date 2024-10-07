def countCharactersAfterN(arr):
    # 関数を完成させてください
    nUnicode = ord('n')
    zUnicode = ord('z')
    total = 0

    for string in arr:
        string = string.lower()
        for char in string:
            if nUnicode <= ord(char) <= zUnicode:
                total += 1
    
    return total