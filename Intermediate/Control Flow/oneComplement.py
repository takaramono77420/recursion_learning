def oneComplement(bits):
    # 関数を完成させてください
    reverse = "10"
    output = []

    for i in bits:
        output.append(reverse[int(i)])
    
    return ''.join(list(output))