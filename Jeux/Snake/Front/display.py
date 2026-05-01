from Jeux.Snake.Front.assets import load_assets
import pygame
import sys

def main_menu():
    """
    Gére l'affichage du menu principale et du choix fait dedans
    :return: Boolean
    """
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    title = font.render("Bataille", True, (255, 255, 255))
    title_ = font.render("Bataille", True, (200, 0, 0))

    font = pygame.font.SysFont("calibri", 50, True)

    while True:

        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

        if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
            new_game_msg = font.render("Nouvelle partie", True, (50, 50, 50))
        else:
            new_game_msg = font.render("Nouvelle partie", True, (100, 100, 100))

        if 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
            leave_msg = font.render("Quitter", True, (50, 50, 50))
        else:
            leave_msg = font.render("Quitter", True, (100, 100, 100))


        screen.fill((200, 200, 200))
        display_main_menu(new_game_msg, leave_msg, title, title_)

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

def intro(snake, apple):
    """
    Petite pause avant de commencer (pour se préparer mentalement).
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type in (pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN):
                return

        display_all(snake, apple)

def display_all(snake, apple):
    """
    Gére l'affichage de la partie (serpent, pomme)
    """

    screen.fill((200, 200, 200))
    screen.blit(grid, (30, 230))

    for cord in apple.position:
        screen.blit(apple_img, snake.get_grid_cord(cord[0],cord[1]))

    for i in range(len(snake.snake)):
        screen.blit(snake.snake[i][0], snake.get_cord(i))

    pygame.display.flip()

def display_game_over(apple_eaten):
    """
    Gére l'affichage de la fin de la partie.
    :return: Boolean
    """
    font = pygame.font.SysFont("calibri", 30, True)

    if apple_eaten == 141:
        msg = font.render("VOUS AVEZ GAGNEE !!!", True, (200, 0, 0))
    else:
        msg = font.render(f"VOUS AVEZ PERDU. SCORE : {apple_eaten} ", True, (200, 0, 0))

    restart = font.render("Appuyer sur Espace pour Restart", True, (200, 0, 0))

    screen.blit(msg, (107, 50))
    screen.blit(restart, (97, 100))

    while True:

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

def display_main_menu(new_game_msg = str, leave_msg = str, title = str, title_ = str):
    """
    Place les eléments sur l'écran.
    """
    screen.blit(new_game_msg, (20, 180))
    screen.blit(leave_msg, (20, 340))
    screen.blit(title, (37, 39))
    screen.blit(title_, (40, 40))

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

apple_img, grid, head, body,tail,turn_horaire, turn_anti = load_assets()
pygame.init()
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 800))



