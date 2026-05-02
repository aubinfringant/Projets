from Jeux.Snake.Front.assets import load_assets
import pygame
import sys

def intro(snake, apple):
    """
    Petite pause avant de commencer (pour se préparer mentalement).
    """
    while True:
        clock.tick(60)
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

    if apple_eaten == 140:
        msg = font.render("VOUS AVEZ GAGNEE !!!", True, (200, 0, 0))
    else:
        msg = font.render(f"VOUS AVEZ PERDU. SCORE : {apple_eaten} ", True, (200, 0, 0))

    restart = font.render("Appuyer sur Espace pour Restart", True, (200, 0, 0))

    screen.blit(msg, (107, 50))
    screen.blit(restart, (97, 100))
    pygame.display.flip()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

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
pygame.display.set_caption('SNAKE')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 800))



