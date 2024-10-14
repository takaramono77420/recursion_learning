def getMinSteps(n):
    # 関数を完成させてください
    if n == 1:return 0

    dp = [n+1] * (n+1)
    dp[1] = 0
    dp[0] = 0

    for i in range(2, n+1):
        tmp = [dp[i-1]]
        if i%2 == 0:tmp.append(dp[i//2])
        if i%3 == 0:tmp.append(dp[i//3])

        dp[i] = min(tmp) + 1

    return dp[n]