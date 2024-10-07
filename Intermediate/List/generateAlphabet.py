def generateAlphabet(firstAlphabet,secondAlphabet):
    # 関数を完成させてください
    arrivingAndDepartingStation = [ord(firstAlphabet.lower()), ord(secondAlphabet.lower())]
    startStation = min(arrivingAndDepartingStation)
    endStation = max(arrivingAndDepartingStation)
    
    stopStationList = []

    for i in range(startStation, endStation + 1):
        stopStationList.append(chr(i))
    
    return stopStationList