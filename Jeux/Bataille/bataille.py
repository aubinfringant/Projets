from Jeux.Bataille.Front.display import *
from Class.Deck52 import *
from Class.Player import *
from Class.Trick import *
import random

def player_turn():
    """
    Swap les 2 cartes en fonction de la carte choisie
    pour pouvoir donner la bonne avec .drop()
    ou donne la derniere carte si une carte restante.

    :return: func()
    """

    if len(Player_1.hand) > 1:
        choice = display_choose(trick.cards, Player_1.hand, Player_2.hand)

    else:
        choice = 0

    Player_1.hand[0], Player_1.hand[choice] = Player_1.hand[choice], Player_1.hand[0]

    trick.cards.append(Player_1.drop())
    trick.cards.append(Player_2.drop())

    return display_table(trick.cards, Player_1.hand, Player_2.hand)

while main_menu():
    """
    Initialisation du programme
    """
    deck = Deck()
    deck.new_deck()
    random.shuffle(deck.deck)

    trick = Trick()

    Player_1 = Player("Joueur_1")
    Player_2 = Player("Joueur_2")

    deck.draw(Player_1.hand, 26)
    deck.draw(Player_2.hand, 26)

    while len(Player_1.hand) > 0 and len(Player_2.hand) > 0:
        """
        Boucle principale
        """
        player_turn()
        pygame.display.flip()
        pygame.time.wait(250)


        while trick.result(Player_1, Player_2):
            player_turn()
            pygame.display.flip()
            pygame.time.wait(250)

    display_game_over(Player_1.hand, Player_2.hand)
