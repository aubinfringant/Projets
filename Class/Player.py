class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def show_hand(self):
        hand = []
        for card in self.hand:
            card_face = (card.value, card.color)
            hand.append(card_face)

        for i in range(len(hand)):
            print(hand[i])

    def drop(self):
        return self.hand.pop(0)