import random

class Trick:

    def __init__(self):

        self.cards = []

    def __str__(self):
        return " | ".join(f"{card.card[0]}({card.card[1]})" for card in self.cards)#IA

    def result(self, p1, p2):

        card_p1 = self.cards[-2].values[self.cards[-2].card[0]]
        card_p2 = self.cards[-1].values[self.cards[-1].card[0]]

        if card_p1 > card_p2:

            random.shuffle(self.cards)
            for card in self.cards:
                p1.hand.append(card)

            self.cards.clear()
            return False

        elif card_p1 < card_p2:

            random.shuffle(self.cards)
            for card in self.cards:
                p2.hand.append(card)

            self.cards.clear()
            return False

        else:
            if len(p1.hand) >= 2 and len(p2.hand) >= 2:
                self.cards.append(p1.drop())
                self.cards.append(p2.drop())
                return True

            else:
                for i in range(0, len(self.cards), 2):
                    p1.hand.append(self.cards[i])
                    p2.hand.append(self.cards[i + 1])

                self.cards.clear()
                return False