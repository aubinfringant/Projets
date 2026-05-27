import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from Jeux.Memory.Front.display import *
from Class.GridMemory import *
from Class.GameStart import *


Display = GameStart("Memory", (10, 80, 40),(700, 700))

while Display.main_menu():
    """
    Initialisation du programme
    """
    found_cards = []
    grid = Grid(4,4)
    grid.add_card()

    while not grid.full():
        """
        Boucle principale
        """
        choices = []

        while len(choices) != 2:
            choices.append(card_choice(grid,found_cards,choices))

        if choices[0][0] == choices[1][0]:
            found_cards.append(choices)
            grid.find_card(found_cards[-1])
        else:
            confirmation(grid, found_cards, choices)

    confirmation(grid, found_cards, choices)
