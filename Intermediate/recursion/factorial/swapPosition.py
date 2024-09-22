def swapPosition(s):
    # 関数を完成させてください
    s_length = len(s)
    if s_length <= 1:
        return s
    return s[1] + s[0] + swapPosition(s[2:])