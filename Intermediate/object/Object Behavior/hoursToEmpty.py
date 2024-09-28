import math
def hoursToEmpty(velocity,fuelEconomy,tankCapacity):
    # 関数を完成させてください
    newCar = car(velocity,fuelEconomy,tankCapacity)

    return math.floor(newCar.milesWithoutStop() / newCar.getDistance() * 10) / 10

class car:

    def __init__(self, velocity,fuelEconomy,tankCapacity):
        self.velocity = velocity
        self.fuelEconomy = fuelEconomy
        self.tankCapacity = tankCapacity
    
    def milesWithoutStop(self):
        return self.fuelEconomy * self.tankCapacity

    def getDistance(self):
        return self.velocity * 3600