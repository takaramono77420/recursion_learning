def twosComplement(bits):
    # 関数を完成させてください
    output = ['1' if i == '0' else '0' for i in bits]
    
    length = len(output)
    carry = 1
    
    for i in range(length - 1, -1, -1):

        if output[i] == "0":
            output[i] = "1"
            carry = 0
            break
        else:
            output[i] = "0"
        
    if carry == 1:
        return "1" + "".join(output)

    
    return "".join(output)