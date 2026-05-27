import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from Jeux.Bataille.Front.display import *
from Class.GameStart import *
from Class.Deck52 import *
from Class.Player import *
from Class.Trick import *

Display = GameStart("Bataille", (10, 80, 40),(700, 700))

while Display.main_menu():
    """
    Initialisation du programme
    """
    deck = Deck()
    deck.new_deck()
    deck.shuffle()

    trick = Trick()

    p1 = Player("Joueur_1")
    p2 = Player("Joueur_2")

    deck.draw(p1.hand, 26)
    deck.draw(p2.hand, 26)

    while len(p1.hand) > 0 and len(p2.hand) > 0:
        """
        Boucle principale
        """
        player_turn(trick, p1, p2)
        pygame.display.flip()
        pygame.time.wait(250)
        pygame.event.clear()


        while trick.result(p1, p2):
            player_turn(trick, p1, p2)
            pygame.display.flip()
            pygame.time.wait(250)
            pygame.event.clear()

    display_game_over(p1.hand, p2.hand)
