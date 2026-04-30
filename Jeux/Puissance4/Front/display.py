from Library.Jeux.Puissance4.Front.assets import *
import pygame

def main_menu():

    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    title = font.render("PUISSANCE 4", True, (255, 255, 255))
    title_ = font.render("PUISSANCE 4", True, (200, 0, 0))

    font = pygame.font.SysFont("calibri", 50, True)

    while True:
        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

        if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
            new_game = font.render("Nouvelle partie", True, (50, 50, 50))
        else:
            new_game = font.render("Nouvelle partie", True, (100, 100, 100))

        if 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
            leave = font.render("Quitter", True, (50, 50, 50))
        else:
            leave = font.render("Quitter", True, (100, 100, 100))

        screen.fill((200, 200, 200))
        display_main_menu(title, title_, new_game, leave)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    if 338 > mouse_cord_x > 22 and 220 > mouse_cord_y > 180:
                        return True
                    elif 161 > mouse_cord_x > 22 and 380 > mouse_cord_y > 340:
                        return False

def menu():
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
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button in (1, 3):

                    if 150 < mouse_cord_x < 340 and 300 < mouse_cord_y < 340:
                        return 1

                    elif 550 < mouse_cord_x < 740 and 300 < mouse_cord_y < 340:
                        return 2

def choice(grid,turn):
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
                return False,None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):

                    for i in range(len(columns)):
                        if columns[i] - 4 < mouse_cord_x < columns[i] + 96:
                            return True, i

def game_over(winner,grid):
    end = font.render("GAME OVER", True, (150, 0, 0))

    screen.fill((200, 200, 200))
    screen.blit(end, (310, 40))
    display_chips(grid)

    if winner == 1:
        result = font.render("Le joueur 1 (rouge) l'emporte !", True, (150, 0, 0))
        screen.blit(result,(160,85))
    elif winner == 2 :
        result = font.render("Le joueur 2 (jaune) l'emporte !", True, (150, 0, 0))
        screen.blit(result, (160, 85))
    else:
        result = font.render("C'est une égalité !", True, (150, 0, 0))
        screen.blit(result, (215, 85))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                return True

def drop(color, col, grid, free_rows):
    y = 57
    for i in range(free_rows):
        for j in range(33):

            y += 3

            screen.fill((200, 200, 200))
            screen.blit(chips[color-1], (columns[col], y))

            display_chips(grid)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            pygame.time.wait(4)
    return True

def display_chips(grid):
    for i in range(0, 6):
        for j in range(0, 7):

            if grid[i][j] == 1:
                screen.blit(chips[0], (columns[j], rows[i]))
            elif grid[i][j] == 2:
                screen.blit(chips[1],(columns[j], rows[i]))

    screen.blit(grille, (100, 150))
    pygame.display.flip()

def display_main_menu(title,title_,new_game,leave):

    screen.blit(title, (17, 19))
    screen.blit(title_, (20, 20))
    screen.blit(new_game, (20, 180))
    screen.blit(leave, (20, 340))

def affichage_menu(p1,p2):

    screen.blit(p1, (150, 300))
    screen.blit(p2, (550, 300))

def fondu():
    for i in range(255):
        pygame.time.wait(1)
        screen.fill((i, i, i))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True

columns = [105 + 100 * i for i in range(7)]
rows = [154 + 100 * i for i in range(6)]
chips,grille = load_assets()
pygame.init()
screen = pygame.display.set_mode((900,800))
pygame.display.set_caption('Puissance 4')
font = pygame.font.SysFont("calibri", 50, True)
