def reverseString(s):
    # 関数を完成させてください
    
    if len(s) <= 1:
        return s
    
    return reverseString(s[1:]) + s[0]
