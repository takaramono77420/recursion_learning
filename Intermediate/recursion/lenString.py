def lenString(string):
    # 関数を完成させてください
    if string == "":
        return 0
    return 1 + lenString(string[:-1])