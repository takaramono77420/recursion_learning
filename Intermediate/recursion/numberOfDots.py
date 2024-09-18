def numberOfDots(x):
    # 関数を完成させてください

    if x == 0:
        return 0
    
    return x + numberOfDots(x-1)


