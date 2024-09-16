import math
def calculateCorporationTax(state,year,profit):
    # 関数を完成させてください

    def getStateTax(state, profit):
        stateTaxRate = {
            "AZ":0.049,
            "CA":0.0884,
            "TX":0,
            "NC":0.025
        }
        return (stateTaxRate.get(state) if stateTaxRate.get(state) is not None else 0.05) * profit
    
    def isLeapYear(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    
    def getFederalTax(year, profit):
        if isLeapYear(year):
            return 0
        else:
            return profit * 0.21

    return math.ceil(getStateTax(state, profit) + getFederalTax(year, profit))

