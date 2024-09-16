import math

def fallingDistance(planet,time):
    # 関数を完成させてください

    def meterToMile(meter):
        return 0.000621371 * meter

    def planetGravityMpss(planet):
        if planet == "Earth":
            return 9.8
        elif planet == "Jupiter":
            return 24.79
        elif planet == "Mercury":
            return 3.7
        else:
            return 0
    
    return math.floor(meterToMile(planetGravityMpss(planet) * time ** 2 / 2))