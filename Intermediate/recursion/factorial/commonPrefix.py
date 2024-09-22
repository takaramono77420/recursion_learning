def commonPrefix(s1,s2):
    # 関数を完成させてください

    if s1[0] != s2[0]:
        return ""
    elif len(s1) <= 1 or len(s2) <= 1:
        return s1[0]
    
    return s1[0] + commonPrefix(s1[1:], s2[1:])