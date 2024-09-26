def isPrime(number):
    # 関数を完成させてください
    if number <= 1:
        return False

    i = 1

    while i < number //2:
        i += 1
        if number % i == 0:
            return False
        
    
    return True