import os
import pygame

def load_assets():
    """
    Récupération des images pour afficher dans pygame.
    """
    CARD_SIZE = (100, 150)
    PATH = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep

    pygame.init()
    pygame.display.set_mode((700,700))

    def img(name, size=None):
        i = pygame.image.load(PATH + name).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Turn","Pass","Draw","joker","joker4"]
    colors = {
        "v": "Green",
        "b": "Blue",
        "r": "Red",
        "j": "Yellow"
    }

    joker = [
        img("joker.png",CARD_SIZE),
        img("joker4.png",CARD_SIZE),
        img("fleche.png")
    ]

    cards_dict = {
        (val, colors[name]): img(f"{val}_{name}.png",CARD_SIZE)
        for val in values
        for name in colors
    }

    card_back = img("dos.png", CARD_SIZE)

    carpet = img("Tapis_cartes.png", (700,700))

    return card_back, cards_dict, carpet, joker
