def decimalToHexadecimal(decNumber):
    # 関数を完成させてください

    if decNumber == 0:
        return "0"

    hexadecimal = []
    surplus = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    while decNumber > 0:
        hexadecimal.append(surplus[decNumber % 16])
        decNumber = decNumber // 16
    
    return ''.join(list(reversed(hexadecimal)))