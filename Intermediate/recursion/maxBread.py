def calculateBreadFromStickers(hold_stickers, stickers):

    if hold_stickers < stickers:
        return 0
    else:
        return 1 + calculateBreadFromStickers(hold_stickers - stickers + 1, stickers)
    

def maxBread(money,price,sticker):
    # 関数を完成させてください
    count_bread = money // price

    count_bread = count_bread + calculateBreadFromStickers(count_bread, sticker)
    
    return count_bread


