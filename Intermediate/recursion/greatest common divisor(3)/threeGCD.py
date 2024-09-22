def gcd(x, y):

    if x % y == 0:
        return y
    
    return gcd(y, x % y)

def threeGCD(x,y,z):
    # 関数を完成させてください

    return gcd(gcd(x, y), z)

