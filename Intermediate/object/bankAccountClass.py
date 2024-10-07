class BankAccount:
    def __init__(self, bankName, ownerName, savings):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings
    
    def depositMoney(self, depositAmount):

        if self.savings <= 20000:
            self.savings -= 100
        
        self.savings += depositAmount

        return self.savings
    
    def withdrawMoney(self, withdrawAmount):

        if self.savings * 0.2 < withdrawAmount:
            withdrawAmount = int(self.savings * 0.2)
        
        self.savings -= withdrawAmount

        return self.savings
    
    def pastime(self, days):
        return self.savings + 0.25 * days

user1 = BankAccount("Chase", "Claire Simmmons", 30000)

print(user1.withdrawMoney(2000))
print(user1.depositMoney(10000))
print(user1.pastime(93))

user2 = BankAccount("Bank Of America", "Remy Clay", 10000)

print(user2.withdrawMoney(8000))
print(user2.depositMoney(12000))
print(user2.pastime(505))