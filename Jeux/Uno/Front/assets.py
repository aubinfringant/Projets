import os
import pygame

def load_assets():
    """
    Récupération des images pour afficher dans pygame.
    """
    card_format = (100, 150)
    path = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep

    pygame.init()
    pygame.display.set_mode((700,700))

    def img(name, size=None):
        i = pygame.image.load(path + name).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Turn","Pass","Draw","joker","joker4"]
    colors = {
        "v": "Green",
        "b": "Blue",
        "r": "Red",
        "j": "Yellow"
    }

    joker = [
        img("joker.png",card_format),
        img("joker4.png",card_format),
        img("fleche.png")
    ]

    card_dict = {
        (val, colors[name]): img(f"{val}_{name}.png",card_format)
        for val in values
        for name in colors
    }

    card_back = img("dos.png", card_format)

    carpet = img("Tapis_cartes.png", (700,700))

    return card_back, card_dict, carpet, joker
