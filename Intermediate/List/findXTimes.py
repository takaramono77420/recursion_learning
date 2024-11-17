def findXTimes(teams):
    # 関数を完成させてください
    teamsHashMap = {}

    for team in teams:teamsHashMap[team] = teamsHashMap.get(team, 0) + 1

    counts = teamsHashMap.values()
    return max(counts) == min(counts)