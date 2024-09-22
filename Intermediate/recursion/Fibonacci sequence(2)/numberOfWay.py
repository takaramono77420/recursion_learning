def numberOfWay(x):
    # 関数を完成させてください

    if x == 1:
        return 1
    elif x == 2:
        return 2

    return numberOfWay(x -1) + numberOfWay(x - 2)
    
    