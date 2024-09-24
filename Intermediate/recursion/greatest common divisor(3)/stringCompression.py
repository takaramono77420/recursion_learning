def consecutiveCharCount(s):
    
    if len(s) == 1 or s[0] != s[1]:
        return 1
    
    return 1 + consecutiveCharCount(s[1:])

def stringCompression(s):
    # 関数を完成させてください
    if len(s) <= 1:
        return s
    
    count = consecutiveCharCount(s)

    if count == 1:
        return s[0] + stringCompression(s[count:])
    else:
        return s[0] + str(count) + stringCompression(s[count:])