def calculateLocation(latitude,longitude):
    # 関数を完成させてください
    latitude_location = "equator"
    longitude_location = "prime meridian"
    
    #緯度
    if latitude > 0:
        latitude_location = "north"
    elif latitude < 0:
        latitude_location = "south"
    
    #経度
    if longitude > 0:
        longitude_location = "east"
    elif longitude < 0:
        longitude_location = "west"
    
    return latitude_location + "/" + longitude_location