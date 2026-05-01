from Jeux.Snake.Front.assets import load_assets
import pygame
import sys

def main_menu():
    fondu()
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    titre = font.render("SNAKE", True, (255, 255, 255))
    titre_ = font.render("SNAKE", True, (200, 0, 0))
    font = pygame.font.SysFont("calibri", 50, True)

    while True:
        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

        screen.fill((200, 200, 200))

        if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
            nouvelle_partie = font.render("Nouvelle partie", True, (50, 50, 50))
        else:
            nouvelle_partie = font.render("Nouvelle partie", True, (100, 100, 100))

        if 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
            quitter_ = font.render("Quitter", True, (50, 50, 50))
        else:
            quitter_ = font.render("Quitter", True, (100, 100, 100))

        affichage_main_menu(titre, titre_, nouvelle_partie, quitter_)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    if 338 > mouse_cord_x > 22 and 220 > mouse_cord_y > 180:
                        return True

                    elif 161 > mouse_cord_x > 22 and 380 > mouse_cord_y > 340:
                        pygame.quit()
                        sys.exit()

def intro(snake, apple):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type in (pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN):
                return

        affichage_snake(snake, apple)

def affichage_snake(snake, apple):

    screen.fill((200, 200, 200))
    screen.blit(grid, (30, 230))

    for cord in apple.position:
        screen.blit(apple_img, snake.get_grid_cord(cord[0],cord[1]))

    for i in range(len(snake.snake)):
        screen.blit(snake.snake[i][0], snake.get_cord(i))

    pygame.display.flip()

def game_over(apple_eaten):
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

def affichage_main_menu(titre,titre_,nouvelle_partie,quitter):
    screen.blit(titre, (17, 19))
    screen.blit(titre_, (20, 20))
    screen.blit(nouvelle_partie, (20, 180))
    screen.blit(quitter, (20, 340))

def fondu():
    for i in range(255):
        pygame.time.wait(1)
        screen.fill((i, i, i))
        pygame.display.flip()

apple_img, grid, head, body,tail,turn_horaire, turn_anti = load_assets()
pygame.init()
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 800))



