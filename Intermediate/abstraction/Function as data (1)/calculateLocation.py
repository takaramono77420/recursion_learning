def calculateLocation(latitude,longitude):
    # ŠÖ”‚ðŠ®¬‚³‚¹‚Ä‚­‚¾‚³‚¢
    latitude_location = "equator"
    longitude_location = "prime meridian"
    
    #ˆÜ“x
    if latitude > 0:
        latitude_location = "north"
    elif latitude < 0:
        latitude_location = "south"
    
    #Œo“x
    if longitude > 0:
        longitude_location = "east"
    elif longitude < 0:
        longitude_location = "west"
    
    return latitude_location + "/" + longitude_location