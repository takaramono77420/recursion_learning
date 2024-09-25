def hammingDistanceInString(string1,string2):
    # 関数を完成させてください
    length = len(string1)
    count = 0

    for i in range (0, length):
        if string1[i] != string2[i]:
            count += 1
    
    return count