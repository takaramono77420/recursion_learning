def mergeString(s1,s2):
    # 関数を完成させてください
    if s1 == "" and s2 == "":
        return ""
    return s1[0] + s2[0] + mergeString(s1[1:], s2[1:])


