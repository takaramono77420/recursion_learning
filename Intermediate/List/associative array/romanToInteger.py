def romanToInteger(romanNumber):
    # 関数を完成させてください

    romanToIntegerList = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    integerNumber = 0

    for i in range(len(romanNumber) - 1):

        if romanToIntegerList[romanNumber[i]] < romanToIntegerList[romanNumber[i + 1]]:
            integerNumber -= romanToIntegerList[romanNumber[i]]
        else:
            integerNumber += romanToIntegerList[romanNumber[i]]
    
    integerNumber += romanToIntegerList[romanNumber[-1]]

    return integerNumber