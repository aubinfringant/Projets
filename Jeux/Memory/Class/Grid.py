from Library.Class.Deck_52 import *
import random

class Grid:
    def __init__(self, width, height):
        if width * height % 2 == 0:
            self.paires = width * height // 2
            self.grid = [[0 for i in range(width)] for j in range(height)]
            self.binary_grid = [[0 for i in range(width)] for j in range(height)]
        else:
            print("mauvaise taille")

    def full(self):
        for line in self.binary_grid:
            for i in range(len(line)):
                if line[i] == 0:
                    return False
        return True

    def draw(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j].card)

    def find_card(self, card):
        for line in range(len(self.grid)):
            for i in range(len(self.grid[line])):
                if self.grid[line][i].card == card:
                    self.binary_grid[line][i] = 1


    def add_card(self):
        bag = []
        deck = Deck()
        deck.new_deck()
        for i in range(self.paires):
            card = deck.deck.pop(random.randrange(len(deck.deck)))
            bag.append(card)
            bag.append(card)
        random.shuffle(bag)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = bag[i*(len(self.grid[0]))+j]

