def decimalToBinary(decNumber):
    # 関数を完成させてください
    if decNumber == 0:
        return "0"

    output = []

    while decNumber > 0:
        output.append(str(decNumber % 2))
        decNumber = decNumber // 2
    
    return ''.join(list(reversed(output)))