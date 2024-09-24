def howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, year):
    if capitalMoney >= goalMoney or year >= 80:
        return year
    
    if year % 2 == 0:
        return howLongToReachFundGoalHelper(capitalMoney * (1 + 0.01 * interest), goalMoney * 1.02, interest, year + 1)
    else:
        return howLongToReachFundGoalHelper(capitalMoney * (1 + 0.01 * interest), goalMoney * 1.03, interest, year + 1)

def howLongToReachFundGoal(capitalMoney,goalMoney,interest):
    # 関数を完成させてください

    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, 0)



