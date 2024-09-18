def totalSquareArea(x):
    # 関数を完成させてください

    if x == 1:
        return pow(x, 2)
    
    return x * pow(x, 2) + totalSquareArea(x - 1)
