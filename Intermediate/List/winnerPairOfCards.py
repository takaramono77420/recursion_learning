# 同じランクの枚数をカウントする関数
def countCards(player):
    playerCardsCount = {}
    for card in player:playerCardsCount[card] = playerCardsCount.get(card, 0) + 1
    return playerCardsCount 

# 各プレイヤーの一番枚数が多いランクと枚数を返す関数
def maxCardCounts(playersHandCards):
    playersCardsCount = []
    cache = []

    for index, player in enumerate(playersHandCards):
        playersCardsCount.append(countCards(player))
        maxCount = 0
        maxCountRank = 0
        for rank in playersCardsCount[index]:
            count = playersCardsCount[index].get(rank)
            if maxCount < count:
                maxCount = count
                maxCountRank = rank
        cache.append([maxCountRank, maxCount])

    return cache

# カードのランクをintegerのリストに変換する関数
def convertCardToRank(table):
    convertValueToCardPower = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, \
                            "10":10, "J":11, "Q":12, "K":13, "A":14}
    playersRankList = []
    cache = []
    for player in table:
        
        for card in player:
            cache.append(convertValueToCardPower.get(card[1:]))
        playersRankList.append(sorted(cache.copy(), reverse=True))
        cache.clear()
    
    return playersRankList

# 勝敗のジャッジ
def JudgeWinnerPlayer(mode, playersHandCards=None, comparator1=0, comparator2=0):
    if mode == "comparison":
        if comparator1 > comparator2:
            return "player1"
        elif comparator1 < comparator2:
            return "player2"
        else:
            return None
    elif mode == "handCards":
        if len(playersHandCards[0]) == 0:
            return "draw"
        else:
            return None 

def winnerPairOfCardsHelper(playersHandCards):
    # 手札の有無を確認（なければドロー）
    judge = JudgeWinnerPlayer("handCards", playersHandCards)
    if judge != None:return judge

    # 一番枚数の多いランクのカードを取得する
    comparator = maxCardCounts(playersHandCards)

    # 枚数の比較
    judge = JudgeWinnerPlayer("comparison", comparator1=comparator[0][1], comparator2=comparator[1][1])
    if judge != None:return judge

    # ランクの比較
    judge = JudgeWinnerPlayer("comparison", comparator1=comparator[0][0], comparator2=comparator[1][0])
    if judge != None:return judge

    # 手札を捨てる
    for i in range(comparator[0][1]):
        playersHandCards[0].remove(comparator[0][0])
        playersHandCards[1].remove(comparator[1][0])
    
    return winnerPairOfCardsHelper(playersHandCards)


def winnerPairOfCards(player1,player2):
    # 関数を完成させてください
    table = [player1, player2]

    # カードをランクのリストに変換する
    playersHandCards = convertCardToRank(table)

    return winnerPairOfCardsHelper(playersHandCards)