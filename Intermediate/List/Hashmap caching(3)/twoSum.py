def twoSum(intArr,sumInt):
    # 関数を完成させてください

    hashMap = {intArr[i]: i for i in range(len(intArr)-1, -1, -1)}

    for i, value in enumerate(intArr):
        complement = sumInt - value
        complementIndex = hashMap.get(complement, -1)
        if complementIndex != -1 and i != complementIndex:
            return [i, complementIndex] if i < complementIndex else [complementIndex, i]

    return []