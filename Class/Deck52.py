import random
from Class.Card import Card
class Deck:

    def __init__(self):
        self.values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        self.colors = ["co", "p", "t", "ca"]
        self.deck = []

    def new_deck(self):
        """
        Génère les 52 cartes du deck standard.
        Crée une carte pour chaque combinaison (valeur, couleur).
        """
        for color in self.colors:
            for value in self.values:
                self.deck.append(Card(value, color))

    def draw(self,player,number):
        """
        Distribue des cartes du deck vers la main d'un joueur.
        """
        for num in range(number):
            player.append(self.deck.pop())

    def shuffle(self):
        """
        Mélange aléatoirement les cartes du deck.
        """
        random.shuffle(self.deck)