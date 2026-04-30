from Library.Jeux.Bataille.Front.display import *
from Library.Class.Deck_52 import *
from Library.Class.Player import *
from Library.Class.Trick import *
import random

def play_turn(): #-> Boolean

    if len(Player_1.hand) > 1:
        choice = display_choose(trick.cards, Player_1.hand, Player_2.hand)

    else:
        choice = 0
    if choice is None:
        return False
    Player_1.hand[0], Player_1.hand[choice] = Player_1.hand[choice], Player_1.hand[0]
    trick.cards.append(Player_1.drop())
    trick.cards.append(Player_2.drop())
    return display_game(trick.cards, Player_1.hand, Player_2.hand)



play = main_menu()

while play:

    run = True

    deck = Deck()
    deck.new_deck()
    random.shuffle(deck.deck)

    trick = Trick()

    Player_1 = Player("Joueur_1")
    Player_2 = Player("Joueur_2")

    deck.draw(Player_1.hand, 26)
    deck.draw(Player_2.hand, 26)

    while len(Player_1.hand) > 0 and len(Player_2.hand) > 0:

        run = play_turn()
        if not run:
            break

        while trick.result(Player_1, Player_2):
            run = play_turn()
            if not run:
                break

        if not run:
            break

    if run:
        result = display_game_over(Player_1.hand, Player_2.hand)

        if result:
            play = main_menu()
        else:
            play = False
    else:
        break