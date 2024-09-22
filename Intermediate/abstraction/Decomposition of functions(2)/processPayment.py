def processPayment(creditCardType ,cost):
    # 関数を完成させてください
    def checkCardType(creditCardType):
        return True if (creditCardType == "Visa" or creditCardType == "MasterCard") else False
    
    if not checkCardType(creditCardType):
        return -1.0
    
    def askForTips(cost):
        if cost % 3 == 0:
            return cost * 0.03
        elif cost % 5 == 0:
            return cost * 0.05
        elif cost % 7 == 0:
            return cost * 0.07
        else:
            return cost * 0.1
    
    totalPayment = cost * 1.1 + askForTips(cost)
    
    return totalPayment if totalPayment <= 300 else -1.0
