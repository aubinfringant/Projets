import pygame
import sys


class GameStart:
    """
    Classe générique pour initialiser et gérer le menu principal d'un jeu pygame.
    Permet de créer facilement une fenêtre avec un menu standard réutilisable.
    """


    def __init__(self, title: str, color: tuple, size: tuple):
        """
        Initialise la fenêtre et les propriétés du jeu.
        """
        pygame.init()
        self.title = title
        self.color = color
        self.width = size[0]
        self.height = size[1]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title.upper())

    def main_menu(self):
        """
        Affiche le menu principal avec les options "Nouvelle partie" et "Quitter".
        Gère les événements souris pour détecter le choix de l'utilisateur.
        :return: Boolean - True si nouvelle partie, sys.exit() sinon
        """
        font_title = pygame.font.SysFont("timesnewroman", 70, True, True)
        title = font_title.render(self.title, True, (255, 255, 255))
        title_ = font_title.render(self.title, True, (200, 0, 0))

        font_button = pygame.font.SysFont("calibri", 50, True)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

            new_game_msg = font_button.render("Nouvelle partie", True, (100, 100, 100))
            leave_msg = font_button.render("Quitter", True, (100, 100, 100))

            if 20 <= mouse_cord_x <= 338 and 180 <= mouse_cord_y <= 220:
                new_game_msg = font_button.render("Nouvelle partie", True, (50, 50, 50))

            if 20 <= mouse_cord_x <= 161 and 340 <= mouse_cord_y <= 380:
                leave_msg = font_button.render("Quitter", True, (50, 50, 50))

            self.screen.fill(self.color)
            self.display_main_menu(new_game_msg, leave_msg, title, title_)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in (1, 3):
                        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()
                        if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
                            return True

                        elif 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
                            pygame.quit()
                            sys.exit()

    def display_main_menu(self, new_game_msg, leave_msg, title, title_):
        """
        Place les boutons du menu principal et le titre sur l'écran.
        """
        self.screen.blit(new_game_msg, (20, 180))
        self.screen.blit(leave_msg, (20, 340))
        self.screen.blit(title, (37, 39))
        self.screen.blit(title_, (40, 40))