import math
def shuffleSuccessRate(arr,shuffledArr):
    # 関数を完成させてください

    indexMap = {value : index for index, value in enumerate(shuffledArr)}

    shuffleCount = 0

    for index, value in enumerate(arr):

        if indexMap[value] != index:
            shuffleCount = shuffleCount + 1
    
    return math.floor(100 * shuffleCount / len(arr))