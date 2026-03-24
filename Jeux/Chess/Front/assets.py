import os
def load_assets():
    BASE = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep
    import pygame
    pygame.init()
    pygame.display.set_mode((700,700))
    def img(nom, size=None):
        i = pygame.image.load(BASE + nom).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    rank = ["R", "D", "B", "C", "T", "P"]
    color = ["b", "n"]
    
    pieces = [img(
            f"{val}_{c}.png",(70,70))
        for val in rank
        for c in color
    ]

    echiquier= img("echiquier.png", (680,680))
    return echiquier, pieces