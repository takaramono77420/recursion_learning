def gcd(x, y):

    if x % y == 0:
        return y
    
    return gcd(y, x % y)

def irreducibleFraction(x,y):
    # 関数を完成させてください

    x_y_gcd = gcd(x, y)

    if y == x_y_gcd:
        return str(x // x_y_gcd)

    return str(x // x_y_gcd) + "/" + str(y // x_y_gcd)