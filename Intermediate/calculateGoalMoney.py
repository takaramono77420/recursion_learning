def calculateGoalMoney(capital,year):
    # 関数を完成させてください
    if capital % 2 == 0:
        annual_interest_rate = 0.02
    else:
        annual_interest_rate = 0.03
    
    return int(capital * (1 + annual_interest_rate) ** year)
