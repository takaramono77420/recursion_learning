def maxOfPairSum(arr1,arr2,x):
    # 関数を完成させてください
    maxSum = -float('inf')

    flag = True

    for i in arr1:
        for j in arr2:
            if maxSum <= i + j and x > i +j:
                maxSum = i + j
                flag = False
    
    if flag:
        return "no pair"
        
    return maxSum