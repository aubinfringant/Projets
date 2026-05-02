import os
import pygame

def load_assets():
    """
    Récupération des images pour afficher dans pygame.
    """
    PATH = os.path.join(os.path.dirname(__file__), 'Assets') + os.sep

    pygame.init()
    pygame.display.set_mode((900,800))

    def img(name, size=None):
        i = pygame.image.load(PATH + name).convert_alpha()
        return pygame.transform.scale(i, size) if size else i

    red = img('rouge.png',(90, 90))
    yellow = img('jaune.png',(90, 90))
    grid_img = img('grille.png',(700, 600))

    chips =  [red,yellow]

    return chips, grid_img
