def splitAndAdd(digits):
    # 関数を完成させてください

    if digits == 0:
        return digits
    
    return digits % 10 + splitAndAdd(digits // 10)
        
