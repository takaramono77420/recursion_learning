def winnerBlackjack(playerCards,houseCards):
    # 関数を完成させてください
    numberConverter = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    playerTotal = sum(numberConverter.index(card[1:]) + 1 for card in playerCards)

    if playerTotal > 21:
        return False

    houseTotal = sum(numberConverter.index(card[1:]) + 1 for card in houseCards)

    if houseTotal > 21:
        return True
    
    return playerTotal > houseTotal