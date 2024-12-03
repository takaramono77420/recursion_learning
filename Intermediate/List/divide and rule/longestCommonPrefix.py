def longestCommonPrefixHelper(strArr, start, end):

    if start == end:return strArr[start]

    mid = (start + end) // 2

    leftStr = longestCommonPrefixHelper(strArr, start, mid)
    rightStr = longestCommonPrefixHelper(strArr, mid + 1, end)

    strMinLength = len(leftStr) if len(leftStr) < len(rightStr) else len(rightStr)
    commonPrefix = []

    for i in range(0, strMinLength):
        if leftStr[i] == rightStr[i]:
            commonPrefix.append(leftStr[i])
        else:
            break

    return commonPrefix

def longestCommonPrefix(strArr):
    # 関数を完成させてください

    return ''.join(longestCommonPrefixHelper(strArr, 0, len(strArr) - 1))