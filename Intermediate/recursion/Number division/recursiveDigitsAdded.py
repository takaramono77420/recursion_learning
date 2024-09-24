def splitAndAdd(digits, total):

    if digits == 0:
        return total
    
    return splitAndAdd(digits // 10, total + digits % 10)

def recursiveDigitsAddedHelper(digits, total):
    
    sum = splitAndAdd(digits, 0)
    total = total + sum

    if sum >= 10:
        return recursiveDigitsAddedHelper(sum, total)
    else:
        return total

def recursiveDigitsAdded(digits):
    # 関数を完成させてください

    return recursiveDigitsAddedHelper(digits, 0)