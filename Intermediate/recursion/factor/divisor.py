def divisor(number):
    # 関数を完成させてください
    return divisorHelper(number, 1)

def divisorHelper(number, i):
    if number == i:
        return str(i)
    elif number % i == 0:
        return str(i) + "-" + divisorHelper(number, i+1)
    else:
        return divisorHelper(number, i+1)