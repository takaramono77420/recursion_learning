def getEmotion(height,planet):
    # 関数を完成させてください

    def getPlanetGravityMpss(planet):
        planetGravityMpss = {
            "Earth" : 9.8,
            "Jupiter" : 24.79,
            "Mars" : 3.71,
            "Pluto" : 0.58,
            "Moon" : 1.62
        }
        gravityMpss = planetGravityMpss.get(planet) 
        return gravityMpss if gravityMpss is not None else 0
    
    gravityMpss = getPlanetGravityMpss(planet)

    if gravityMpss == 0:
        return "no data"
    
    def getVelocity(height, gravityMpss):
        return pow(2 * gravityMpss * height, 1/2)

    def emotionLevel(velocity):
        if velocity >= 80:
            return "terrified"
        elif velocity >= 60:
            return "frighten"
        elif velocity >= 40:
            return "scared"
        else:
            return "afraid"
    
    return emotionLevel(getVelocity(height, gravityMpss))



