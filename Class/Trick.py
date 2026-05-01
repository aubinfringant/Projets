import random

class Trick:

    def __init__(self):
        self.cards = []

    def result(self, p1, p2):
        """
        Détermine le gagnant du pli et distribue les cartes.
        Gère trois cas :
        - p1 gagne : les cartes mélangées vont dans sa main
        - p2 gagne : les cartes mélangées vont dans sa main
        - Égalité : si assez de cartes (≥2 chacun), bataille (retourne True)
                   sinon, redistribution équitable et fin du pli
        :return: Boolean - True si bataille, False sinon
        """
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
                self.cards.append(p1.hand.pop(0))
                self.cards.append(p2.hand.pop(0))
                return True

            else:
                for i in range(0, len(self.cards), 2):
                    p1.hand.append(self.cards[i])
                    p2.hand.append(self.cards[i + 1])

                self.cards.clear()
                return False