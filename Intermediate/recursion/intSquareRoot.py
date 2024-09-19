def intSquareRootHelper(x, count):

    if pow(count, 2) > x:
        return count - 1

    return intSquareRootHelper(x, count + 1)

def intSquareRoot(n):
    # 関数を完成させてください

    return intSquareRootHelper(n, 1)