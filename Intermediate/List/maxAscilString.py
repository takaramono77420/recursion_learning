def maxAscilString(stringList):
    # 関数を完成させてください

    asciiArray = [0] * len(stringList)

    for i, string in enumerate(stringList):

        for char in string:

            asciiArray[i] += ord(char)

    return asciiArray.index(max(asciiArray))