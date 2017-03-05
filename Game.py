# #################################################
# #BLACKJACK (1p so far)
# # Authors:
# #     Rebecca Fleak
# #     Cody Krutil
# #################################################S
import random
deck = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10,'A':[1,11]}
used = []
def getCard():
    decklst = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    suit = ['Hearts','Diamonds','Clubs','Spades']
    cardPick = decklst[random.randint(0,len(decklst)-1)]
    suitPick = suit[random.randint(0,len(suit)-1)]
    card = [cardPick,suitPick]
    if len(used) == 52:
        return None
    elif card in used:
        card = getCard()
        return card
    elif card not in used:
        used.append(card)
        return card

class Hand:
    def __init__(self, card = None):
        # self.hand = self.startHand()
        self.hand = [card]
    def hit(self):
        self.hand.append(getCard())
        return self.hand
    def startHand(self):
        self.hand = []
        self.hit()
        self.hit()
        return self.hand
    def getHand(self):
        return self.hand
    def __str__(self):
        cards = ''
        for i in range(len(self.hand)):
            cards += ("\n" + str(self.hand[i][0]) + " of " + str(self.hand[i][1]))
        return cards
    def handValue(self):
        cardList = self.getHand()
        value = 0
        for i in range(len(cardList)):
            if value + i <= 10:
                deck['A'] = 11
            else:
                deck['A'] = 1
            value += deck[cardList[i][0]]
        return value

    def split(self, fromHand):
        splitted = Hand(fromHand)
        splitted.hit()
        return splitted

def play(playerHand,name):
    print(name + "'s turn!")
    hold = True
    once = True
    single = True
    split = False
    hand1 = None
    hand2 = None
    p1Hand1 = False
    p1Hand2 = False
    while hold:
        value = playerHand.handValue()
        if hand1 == None and hand2 == None:
            if value > 21:
                print("Your hand value is " + str(value))
                print("You lose.")
                hold = False
            elif value == 21:
                print("BLACKJACK!!!!  YOU WIN!")
                hold = False

            else:
                if once:
                    if playerHand.getHand()[0][0] == playerHand.getHand()[1][0]:
                        user = input("Would you like to split?[Y/N]")
                        if user.upper() == 'Y':
                            once = False
                            p1Hand1 = True
                            p1Hand2 = True
                            hand1 = playerHand.split(playerHand.getHand()[0])
                            hand2 = playerHand.split(playerHand.getHand()[1])
                        elif user.upper() == 'N':
                            once = False
                    else:
                        once = False
                else:
                    print(playerHand)
                    user = input("Your handvalue is: " + str(playerHand.handValue()) +"\nDo you want to hit? [HIT/HOLD]")
                    if user.upper() == 'HOLD':
                        hold = False
                        single = False
                    elif user.upper() == 'HIT':
                        playerHand.hit()
                        print(playerHand.handValue())

        elif len(hand1.getHand()) > 0 and len(hand2.getHand()) > 0:
            value1 = hand1.handValue()
            print('hand 1: ' + str(hand1))
            value2 = hand2.handValue()
            print('hand 2: ' + str(hand2))
            while p1Hand1:
                value1 = hand1.handValue()
                print(hand1)
                if value1 > 21:
                    print("Your hand value is " + str(value1))
                    print("You lose.")
                    p1Hand1 = False
                elif value1 == 21:
                    print("BLACKJACK!!!!  YOU WIN!")
                    p1Hand1 = False
                else:
                    user = input("Your handvalue is: " + str(value1) +"\nDo you want to hit? [HIT/HOLD]")
                    if user.upper() == 'HOLD':
                        p1Hand1 = False
                    elif user.upper() == 'HIT':
                        hand1.hit()
                        print(value1)
            while p1Hand2:
                value2 = hand2.handValue()
                print(hand2)
                if value2 > 21:
                    print("Your hand value is " + str(value2))
                    print("You lose.")
                    p1Hand2 = False
                    hold = False
                elif value2 == 21:
                    print("BLACKJACK!!!!  YOU WIN!")
                    p1Hand2 = False
                    hold = False
                else:
                    user = input("Your handvalue is: " + str(value2) +"\nDo you want to hit? [HIT/HOLD]")
                    if user.upper() == 'HOLD':
                        p1Hand2 = False
                        hold = False
                    elif user.upper() == 'HIT':
                        hand2.hit()
                        print(value2)
    if hand1 == None and hand2 == None:
        return playerHand.handValue()
    else:
        if hand1.handValue() > hand2.handValue() and hand1.handValue() < 22:
            return hand1.handValue()
        else:
            return hand2.handValue()
state = True
p1 = Hand()
p2 = Hand()
p3 = Hand()
p4 = Hand()
players = [[p1,'Player 1'],[p2,'Player 2'],[p3,'Player 3'],[p4,'Player 4']]
playerScores = []
player_amount = None
last = 0
nearest = None
while state:
    player_amount = input("How many players are playing?[1-4]")
    if player_amount.isdigit() and int(player_amount) < 5 and int(player_amount) > 0:
        player_amount = int(player_amount)
        state = False
    else:
        print("That isn't a number")
for i in range(player_amount):
    player = players[i]
    player[0].startHand()
    playerScores.append(play(player[0],player[1]))
for i in range(0,len(playerScores)):
    if playerScores[i] <= 22:
        if playerScores[i] > last:
            last = playerScores[i]
            nearest = i
print(playerScores)
print('\n' + players[nearest][1] + ' wins!')
#END
