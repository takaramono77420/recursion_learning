def canMakeTargetVal(arr,target):
    # 関数を完成させてください

    for number in arr:
        for i in range(arr.index(number) + 1, len(arr)):
            if number + arr[i] == target:
                return True
    
    return False
