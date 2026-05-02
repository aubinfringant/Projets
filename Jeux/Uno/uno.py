from Class.DeckUno import *
from Jeux.Uno.Back.engine import *
from Class.GameStart import *


Display = GameStart("Uno", (10, 80, 40),(700, 700))

while Display.main_menu():
    """
    Initialisation du jeu.
    """
    counter, players_turn = 0, 0
    direction = 1

    deck = DeckUno()
    players = distribute(4,7, deck)

    choose_first_card(deck)

    playing(deck, players, direction, counter, players_turn)
