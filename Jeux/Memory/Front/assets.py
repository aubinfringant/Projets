import os
def load_assets():
    BASE = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep
    print(BASE)
    TAILLE_CARTE = (100, 150)
    import pygame
    pygame.init()
    pygame.display.set_mode((700,700))
    def img(nom, size=None):
        i = pygame.image.load(BASE + nom).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    # ---------- Cartes ----------
    valeurs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    valeur = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
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
