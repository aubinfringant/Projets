from Jeux.Puissance4.Front.assets import *
import pygame
import sys

def main_menu():
    """
        Gére l'affichage du menu principale et du choix fait dedans
        :return: Boolean
        """
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    title = font.render("PUISSANCE 4", True, (255, 255, 255))
    title_ = font.render("PUISSANCE 4", True, (200, 0, 0))

    font = pygame.font.SysFont("calibri", 50, True)

    while True:

        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

        if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
            new_game_msg = font.render("Nouvelle partie", True, (50, 50, 50))
        else:
            new_game_msg = font.render("Nouvelle partie", True, (100, 100, 100))

        if 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
            leave = font.render("Quitter", True, (50, 50, 50))
        else:
            leave = font.render("Quitter", True, (100, 100, 100))

        screen.fill((200, 200, 200))
        display_main_menu(title, title_, new_game_msg, leave)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
                        return True

                    elif 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
                        pygame.quit()
                        sys.exit()

def mode():
    """
    Gere la selection du mode (1 ou 2 joueurs).
    :return: Integer
    """
    while True:

        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

        if 150 < mouse_cord_x < 350 and 300 < mouse_cord_y < 340:
            player_1 = font.render("1 PLAYER", True, (50, 50, 50))
        else:
            player_1 = font.render("1 PLAYER", True, (100, 100, 100))
        if 550 < mouse_cord_x < 750 and 300 < mouse_cord_y < 340:
            player_2 = font.render("2 PLAYER", True, (50, 50, 50))
        else:
            player_2 = font.render("2 PLAYER", True, (100, 100, 100))

        screen.fill((200, 200, 200))
        affichage_menu(player_1, player_2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):

                    if 150 < mouse_cord_x < 340 and 300 < mouse_cord_y < 340:
                        return 1

                    elif 550 < mouse_cord_x < 740 and 300 < mouse_cord_y < 340:
                        return 2

def choice(grid,turn):
    """
    Gére la selection de la colonne du joueur.
    :return: Integer
    """
    while True:
        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

        screen.fill((200, 200, 200))

        if 60 < mouse_cord_y < 750:

            for i in range(len(columns)):
                if columns[i] - 4 < mouse_cord_x < columns[i] + 96:

                    if turn == 1:
                        screen.blit(chips[0], (columns[i], 54))
                    else:
                        screen.blit(chips[1], (columns[i], 54))

        display_chips(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):

                    for i in range(len(columns)):
                        if columns[i] - 4 < mouse_cord_x < columns[i] + 96:
                            return i

def game_over(winner,grid):
    """
    Gére la fin de parti (Quitter ou menu principale).
    :return:
    """
    end = font.render("GAME OVER", True, (150, 0, 0))

    screen.fill((200, 200, 200))
    screen.blit(end, (320, 40))
    display_chips(grid)

    if winner == 1:
        result = font.render("Le joueur 1 (rouge) l'emporte !", True, (150, 0, 0))
        screen.blit(result,(160,85))
    elif winner == 2 :
        result = font.render("Le joueur 2 (jaune) l'emporte !", True, (150, 0, 0))
        screen.blit(result, (160, 85))
    else:
        result = font.render("C'est une égalité !", True, (150, 0, 0))
        screen.blit(result, (270, 85))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                return True

def drop(color, col, grid, free_rows):
    """
    Petite animation de chute du jeton.
    """
    y = 57
    for i in range(free_rows):
        for j in range(34):

            y += 3

            screen.fill((200, 200, 200))
            screen.blit(chips[color-1], (columns[col], y))

            display_chips(grid)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.time.wait(4)

def display_chips(grid):
    """
    Affiche la grille avec les jetons dedans.
    """
    for i in range(0, 6):
        for j in range(0, 7):

            if grid[i][j] == 1:
                screen.blit(chips[0], (columns[j], rows[i]))
            elif grid[i][j] == 2:
                screen.blit(chips[1],(columns[j], rows[i]))

    screen.blit(grid, (100, 150))
    pygame.display.flip()

def display_main_menu(title,title_,new_game_msg,leave):
    """
    Place les eléments sur l'écran.
    """
    screen.blit(title, (17, 19))
    screen.blit(title_, (20, 20))
    screen.blit(new_game_msg, (20, 180))
    screen.blit(leave, (20, 340))

def affichage_menu(p1,p2):
    """
    Place les eléments sur l'écran.
    """
    screen.blit(p1, (150, 300))
    screen.blit(p2, (550, 300))

def fondu():
    """
    Petite animation de fondu.
    """
    for i in range(200):
        pygame.time.wait(1)
        screen.fill((i, i, i))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

columns = [105 + 100 * i for i in range(7)]
rows = [154 + 100 * i for i in range(6)]
chips,grid = load_assets()
pygame.init()
screen = pygame.display.set_mode((900,800))
pygame.display.set_caption('Puissance 4')
font = pygame.font.SysFont("calibri", 50, True)
