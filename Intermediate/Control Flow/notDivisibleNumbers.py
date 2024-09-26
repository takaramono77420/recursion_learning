def notDivisibleNumbers(x,y):
    # 関数を完成させてください
    string = ""
    for i in range(1, x + 1):
        if i % y != 0:
            string += str(i) + "-"
    
    return string[:-1]