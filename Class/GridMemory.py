from Class.Deck52 import *
import random

class Grid:
    def __init__(self, width, height):
        if width * height % 2 == 0:
            self.paires = width * height // 2
            self.grid = [[0 for i in range(width)] for j in range(height)]
            self.binary_grid = [[0 for i in range(width)] for j in range(height)]
        else:
            print("Mauvaise taille (Nombre paire seulement).")

    def full(self):
        """
        Vérifie si toutes les paires ont été trouvées.
        :return: Boolean - True si binary_grid est complètement rempli de 1, False sinon
        """
        for row in self.binary_grid:
            if 1 not in row:
                return False
        return True

    def find_card(self, card_try):
        """
        Marque toutes les occurrences d'une carte comme trouvées.
        Recherche dans grid et met à jour binary_grid à 1 pour chaque correspondance.
        """
        for i,row in enumerate(self.grid):
            for j,card in enumerate(row):
                if card.card == card_try:
                    self.binary_grid[i][j] = 1

    def add_card(self):
        """
        Remplit la grille avec des paires de cartes mélangées.
        Pioche des cartes uniques d'un deck standard,
        les duplique pour créer des paires,
        mélange et remplit la grille.
        """
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

