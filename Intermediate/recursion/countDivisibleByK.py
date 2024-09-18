def countDivisibleByK(n,k):
    # 関数を完成させてください
    
    if n % k != 0:
        return 0
    
    return 1 + countDivisibleByK(n / k, k)


