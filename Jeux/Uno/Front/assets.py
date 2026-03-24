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
    valeurs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Turn","Pass","Draw","joker","joker4"]
    couleurs = {"v": "Green",
                "b" : "Blue",
                "r":"Red",
                "j":"Yellow"}
    joker = [img("joker.png",TAILLE_CARTE),
             img("joker4.png",TAILLE_CARTE),
             img("fleche.png")]
    dico_de_cartes = {
        (val, couleurs[name]): img(
            f"{val}_{name}.png",
            TAILLE_CARTE
        )
        for val in valeurs
        for name in couleurs
    }

    cartes_dos = img("dos.png", TAILLE_CARTE)

    tapis = img("Tapis_cartes.png", (700,700))
    return cartes_dos, dico_de_cartes, tapis, joker
