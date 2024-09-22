def towerOfHanoi(discs):
    # 関数を完成させてください

    if discs == 1:
        return 1
    elif discs == 2:
        return 3

    return towerOfHanoi(1) + towerOfHanoi(discs - 1) * 2