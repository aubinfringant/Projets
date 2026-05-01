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

    # ---------- Cartes ----------
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    colors = {
        "co": "Hearts",
        "p": "Spades",
        "ca": "Diamonds",
        "t": "Clubs"
    }
    card_dict = {
        (str(i + 1), c): img(
            f"{val}_{c}.png",
            CARD_SIZE
        )
        for i, val in enumerate(values)
        for c, name in colors.items()
    }

    cartes_dos = img("Cartes_dos.png", CARD_SIZE)

    deck_png = [
        ((val, col), img)
        for (val, col), img in card_dict.items()
    ]
    tapis = img("Tapis_cartes.png", (700,700))
    return deck_png, cartes_dos, card_dict, tapis
