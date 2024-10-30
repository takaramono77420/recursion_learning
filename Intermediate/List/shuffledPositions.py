def shuffledPositions(arr,shuffledArr):
    # 関数を完成させてください
    
    cache = {value : index for index, value in enumerate(shuffledArr)}
    
    return [cache[value] for value in arr]