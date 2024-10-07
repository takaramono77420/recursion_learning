def isFirstStringLarger(s1,s2):
    # 関数を完成させてください
    s1Total = sum([ord(char) for char in s1.lower()])
    s2Total = sum([ord(char) for char in s2.lower()])

    return s1Total > s2Total