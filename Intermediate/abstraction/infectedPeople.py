def infectedPeople(day):
    # 関数を完成させてください

    if day == 0:
        return 1
    
    return 2 * infectedPeople(day - 1)