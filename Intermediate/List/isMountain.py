def isMountain(height):
    # 関数を完成させてください
    heightLen = len(height)

    if heightLen < 3 or height[0] >= height[1]:return False

    upFlag = True

    for i in range(1,heightLen-1):
        if upFlag:
            if height[i] > height[i+1]:
                upFlag=False
            elif height[i] == height[i+1]:
                return False
        else:
            if height[i] < height[i+1]:
                return False
            elif height[i] == height[i+1]:
                return False
    
    if upFlag == True:return False
    
    return True
