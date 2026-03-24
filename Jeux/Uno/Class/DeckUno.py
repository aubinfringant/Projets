import random
class Card:

    def __init__(self, value, color=None):
        self.card = (value, color)
        self.value = value
        self.color = color

    def __str__(self):
        return str(self.card)

class DeckUno:
    def __str__(self):
        return str(self.deck)
    def __init__(self):
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Turn", "Pass", "Draw"]
        self.colors = ["Green", "Blue", "Red", "Yellow"]
        self.deck = []

        for color in self.colors:
            for value in self.values:
                self.deck.append(Card(value, color))
                if value != 0:
                    self.deck.append(Card(value, color))
            self.deck.append(Card("joker"))
            self.deck.append(Card("joker4"))

        random.shuffle(self.deck)

    def draw(self, n):
        drawer = []
        if n <= 0:
            return drawer
        for i in range(n):
            drawer.append(self.deck.pop())
        return drawer

    def sort(self,hand):
        for l in range(len(hand)):
            for i in range(len(hand) - 1):
                card = hand[i].card
                card_ = hand[i+1].card
                if card[1] in ("Green", "Blue", "Yellow") and card_[1] == "Red":
                    hand[i + 1], hand[i] = hand[i], hand[i + 1]
                elif card[1] in ("Green", "Yellow") and card_[1] == "Blue":
                    hand[i + 1], hand[i] = hand[i], hand[i + 1]
                elif card[1] == "Yellow" and card_[1] == "Green":
                    hand[i + 1], hand[i] = hand[i], hand[i + 1]
                elif card[1] is None and card_[1] is not None:
                    hand[i + 1], hand[i] = hand[i], hand[i + 1]

        for j in range(len(hand)):
            for i in range(len(hand) - 1):
                card = hand[i].card
                card_ = hand[i + 1].card
                if card[1] == card_[1]:
                    if type(card[0]) is int and type(card_[0]) is int:
                        if card[0] > card_[0]:
                            hand[i + 1], hand[i] = hand[i], hand[i + 1]
                    else:
                        if type(card_[0]) is int:
                            hand[i + 1], hand[i] = hand[i], hand[i + 1]
                        elif card[0] == "joker4" and card_[0] == "joker":
                            hand[i + 1], hand[i] = hand[i], hand[i + 1]


        return hand


