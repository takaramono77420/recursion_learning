def calculateLocation(latitude,longitude):
    # �֐������������Ă�������
    latitude_location = "equator"
    longitude_location = "prime meridian"
    
    #�ܓx
    if latitude > 0:
        latitude_location = "north"
    elif latitude < 0:
        latitude_location = "south"
    
    #�o�x
    if longitude > 0:
        longitude_location = "east"
    elif longitude < 0:
        longitude_location = "west"
    
    return latitude_location + "/" + longitude_location