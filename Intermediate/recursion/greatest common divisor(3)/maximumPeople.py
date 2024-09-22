def maximumPeople(x,y):
    # 関数を完成させてください

    if x % y == 0:
        return y
    
    return maximumPeople(y, x % y)
