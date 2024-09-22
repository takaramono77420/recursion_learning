def areaOfSquare(x, y):

    if x % y == 0:
        return y * y
    
    return areaOfSquare(y, x % y)

def countSquare(x,y):
    # 関数を完成させてください
    
    return int(x * y / areaOfSquare(x, y))

