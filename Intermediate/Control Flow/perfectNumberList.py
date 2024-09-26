def perfectNumberList(n):
    # 関数を完成させてください
    output = ""

    for i in range(2, n + 1):

        total = 0

        for j in range(1, i // 2 + 1):

            if i % j == 0:
                total += j
        
        if i == total:
            output += "-" + str(i)
    
    return output[1:] if output != "" else "none"