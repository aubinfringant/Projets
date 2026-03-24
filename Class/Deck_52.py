import random

class Card:

    def __init__(self, value, color):
        self.card = (value, color)
        self.value = value
        self.color = color

class Deck:

    def __init__(self):
        self.values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        self.colors = ["co", "p", "t", "ca"]
        self.deck = []

    def new_deck(self):
        for color in self.colors:
            for value in self.values:
                self.deck.append(Card(value, color))

    def tirer(self,j,nb):
        for _ in range(nb):
            j.append(self.deck.pop())