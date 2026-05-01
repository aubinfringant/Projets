from Class.DeckUno import *
from Jeux.Uno.Back.engine import *


while main_menu():
    """
    Initialisation du jeu.
    """
    counter, players_turn = 0, 0
    direction = 1

    deck = DeckUno()
    players = distribute(4,7, deck)

    choose_first_card(deck)

    playing(deck, players, direction, counter, players_turn)
