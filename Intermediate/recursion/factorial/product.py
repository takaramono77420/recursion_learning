def product(x,y):
    # 関数を完成させてください
    if y == 0 or x == 0:
        return 0
    elif y > 0:
        return x + product(x, y - 1)
    else:
        return -x + product(x, y + 1)