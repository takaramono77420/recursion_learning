def firstRepeatingNumber(nums):
    # 関数を完成させてください

    hashMap = {}

    for num in nums:
        
        if num not in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1
    
    for num in nums:

        if hashMap[num] >= 2:
            return num
    
    return -1