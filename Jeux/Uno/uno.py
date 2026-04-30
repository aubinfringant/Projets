from Library.Class.DeckUno import *
from Library.Jeux.Uno.Back.engine import *

launch = main_menu()

while launch:

    counter, players_turn = 0, 0
    direction = 1

    deck = DeckUno()
    players = distribute(4,7, deck)

    top, deck = choose_first_card(deck)

    launch = playing(deck, players, top, direction, counter, players_turn)

pygame.quit()