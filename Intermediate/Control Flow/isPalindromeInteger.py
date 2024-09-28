def isPalindromeInteger(n):
    # 関数を完成させてください
    n = str(n)

    while len(n) >= 1:

        if n[0] != n[-1]:
            return False
        
        n = n[1:-1]
    
    return True

