import math

class Animal:

    def __init__(self, name, weightKg, heightM, isPredator, speedKph):
        self.name = name
        self.weightKg = weightKg
        self.heightM = heightM
        self.isPredator = isPredator
        self.speedKph = speedKph
        self.activityMultiplier = 1.2
    
    def getBmi(self):
        return math.floor(self.weightKg / self.heightM**2 * 100) / 100
    
    def getDailyCalories(self):
        return math.floor((70 * self.weightKg**0.75) * self.activityMultiplier*100) / 100
    
    def isDangerous(self):
        if self.isPredator == True:
            return True
        elif self.heightM >= 1.7:
            return True
        elif self.speedKph >= 35:
            return True
        else:
            return False