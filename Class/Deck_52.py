import random

class Card:

    def __init__(self, value, color):
        self.values = {"1" : 14, "2" : 2, "3" : 3, "4" : 4,
                       "5" : 5, "6" : 6, "7" : 7, "8" : 8,
                       "9" : 9, "10" : 10, "11" : 11,
                       "12" : 12, "13" : 13}
        self.card = (value, color)
        self.value = value
        self.color = color

    def __str__(self):
        return self.card

class Deck:

    def __init__(self):
        self.values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        self.colors = ["co", "p", "t", "ca"]
        self.deck = []

    def new_deck(self):
        for color in self.colors:
            for value in self.values:
                self.deck.append(Card(value, color))

    def draw(self,player,number):
        for num in range(number):
            player.append(self.deck.pop())