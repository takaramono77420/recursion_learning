def isPangram(string):
    # 関数を完成させてください

    alphabetPresence = [False] * 26
    string = string.replace(" ", "").lower()
    string = set(string)

    for char in string:
        ascii = ord(char)

        if 97 <= ascii <= 122:
            alphabetPresence[ascii - 97] = True
    
    return all(alphabetPresence)