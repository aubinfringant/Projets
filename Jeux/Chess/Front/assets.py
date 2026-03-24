import os
def load_assets():
    BASE = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep
    print(BASE)
    TAILLE_CARTE = (100, 150)
    import pygame
    pygame.init()
    pygame.display.set_mode((700,700), pygame.SCALED)
    def img(nom, size=None):
        i = pygame.image.load(BASE + nom).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    
    rank = ["R", "D", "F", "C", "T", "P"]
    color = ["n", "b"]
    couleurs = {
        "co": "Hearts",
        "p": "Spades",
        "ca": "Diamonds",
        "t": "Clubs"
    }
    dico_de_cartes = {
        (str(i + 1), c): img(
            f"{val}_{c}.png",
            TAILLE_CARTE
        )
        for i, val in enumerate(valeurs)
        for c, name in couleurs.items()
    }

    cartes_dos = img("Cartes_dos.png", TAILLE_CARTE)

    tapis = img("Tapis_cartes.png", (700,700))
    return cartes_dos, dico_de_cartes, tapis