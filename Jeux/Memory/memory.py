from Jeux.Memory.Front.display import *
from Class.GridMemory import *



while main_menu():
    """
    Initialisation du programme
    """
    grid = Grid(4,4)
    grid.add_card()

    found_cards = []
    choices = []

    while len(found_cards) != 8:
        """
        Boucle principale
        """
        choices = []

        while len(choices) != 2:
            choices.append(card_choice(grid,found_cards,choices))

        if choices[0][0] == choices[1][0]:
            found_cards.append(choices)
        else:
            confirmation(grid, found_cards, choices)

    confirmation(grid, found_cards, choices)
