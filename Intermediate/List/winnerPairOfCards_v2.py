# 変数、関数の名称はちゃんと変えないといけないとは思う。（時間があったらする。）
import random
class Card:
    def __init__(self, value, suit, power):
        self.value = value
        self.suit = suit
        self.power = power

class Deck:
    def __init__(self):
        self.deck = self.generateDeck()
    
    @staticmethod
    def generateDeck():
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♣", "♦", "♥", "♠"]
        deck = []
        
        for suit in suits:
            for i, value in enumerate(values):
                deck.append(Card(value, suit, i + 2))
        
        return deck

    def shuffleDeck(self):

        for i in range(len(self.deck)):
            j = random.randint(i, len(self.deck) - 1)

            tmp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = tmp
    
    def draw(self):
        return self.deck.pop()

class Dealer:
    @staticmethod
    def startGame():

        table = {
            "deck" : Deck(),
            "player" : []
        }

        table["deck"].shuffleDeck()

        for player in range(0, 2):
            table["player"].append([])
            for draw in range(0, 5):
                table["player"][player].append(table["deck"].draw())
        
        return table

    @staticmethod
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

    @staticmethod
    def winnerPairOfCardsHelper(playersHandCards):
        # 手札の有無を確認
        judge = Dealer.JudgeWinnerPlayer("handCards", playersHandCards)
        if judge != None:return judge

        # 一番枚数の多いランクのカードを取得する
        comparator = HelperFunctions.maxCardCounts(playersHandCards)

        # 枚数の比較
        judge = Dealer.JudgeWinnerPlayer("comparison", comparator1=comparator[0][1], comparator2=comparator[1][1])
        if judge != None:return judge

        # ランクの比較
        judge = Dealer.JudgeWinnerPlayer("comparison", comparator1=comparator[0][0], comparator2=comparator[1][0])
        if judge != None:return judge

        # 手札を捨てる
        for i in range(comparator[0][1]):
            playersHandCards[0].remove(comparator[0][0])
            playersHandCards[1].remove(comparator[1][0])
        
        return Dealer.winnerPairOfCardsHelper(playersHandCards)

    @staticmethod
    def winnerPairOfCards(table):
        playersHandCards = []
        
        for i, player in enumerate(table["player"]):
            playersHandCards.append([])
            for card in player:
                playersHandCards[i].append(card.power)
    
        return Dealer.winnerPairOfCardsHelper(playersHandCards)

class HelperFunctions:
    @staticmethod
    # 同じランクの枚数をカウントする関数
    def countCards(player):
        playerCardsCount = {}
        for card in player:playerCardsCount[card] = playerCardsCount.get(card, 0) + 1
        return playerCardsCount 

    @staticmethod
    # 各プレイヤーの一番枚数が多いランクと枚数を返す関数
    def maxCardCounts(playersHandCards):
        playersCardsCount = []
        cache = []

        for index, player in enumerate(playersHandCards):
            playersCardsCount.append(HelperFunctions.countCards(player))
            maxCount = 0
            maxCountRank = 0
            for rank in playersCardsCount[index]:
                count = playersCardsCount[index].get(rank)
                if maxCount < count:
                    maxCount = count
                    maxCountRank = rank
            cache.append([maxCountRank, maxCount])

        return cache
        

table = Dealer.startGame()
print(Dealer.winnerPairOfCards(table))