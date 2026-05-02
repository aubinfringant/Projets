import os
def load_assets():
    """
    Récupération des images pour afficher dans pygame.
    """
    PATH = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep
    CARD_SIZE = (100, 150)
    import pygame
    pygame.init()
    pygame.display.set_mode((700,700))
    def img(name, size=None):
        i = pygame.image.load(PATH + name).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    colors = {
        "co": "Hearts",
        "p": "Spades",
        "ca": "Diamonds",
        "t": "Clubs"
    }
    cards_sprite = {
        (str(i + 1), c): img(
            f"{val}_{c}.png",
            CARD_SIZE
        )
        for i, val in enumerate(values)
        for c, name in colors.items()
    }

    card_back = img("Cartes_dos.png", CARD_SIZE)

    carpet = img("Tapis_cartes.png", (700,700))
    return card_back, cards_sprite, carpet
