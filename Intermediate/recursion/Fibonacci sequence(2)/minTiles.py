import math

def minTiles(n,m):
    # 関数を完成させてください
    if n <= 0 or m <= 0:
        return 0

    multiplier = int(math.log2(m)) if n >= m else int(math.log2(n))
    side = pow(2, multiplier)

    return 1 + minTiles(n - side, side) + minTiles(side, m - side) + minTiles(n - side, m - side)
