from Library.Jeux.Snake.Front.assets import *
import pygame

def main_menu():
    fondu()
    jouer,quitter = False,False
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    titre = font.render("SNAKE", True, (255, 255, 255))
    titre_ = font.render("SNAKE", True, (200, 0, 0))
    font = pygame.font.SysFont("calibri", 50, True)

    choix = True
    while choix:
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
                choix = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    if 338 > mouse_cord_x > 22 and 220 > mouse_cord_y > 180:
                        jouer = True
                    elif 161 > mouse_cord_x > 22 and 380 > mouse_cord_y > 340:
                        quitter = True

        if jouer:
            choix = False
            return True
        elif quitter:
            choix = False
            return False

def intro(snake):
    running = True
    while running:
        screen.fill((200, 200, 200))
        screen.blit(grille, (30, 230))
        affichage_snake(snake)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            elif event.type in (pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN):
                if event.button in (1, 3):
                    running = False
                    return True

def start(snake):
    screen.fill((200, 200, 200))
    screen.blit(grille, (30, 230))
    #affichage_apple(apple)
    affichage_snake(snake)
    pygame.display.flip()

def affichage_snake(snake):
    screen.blit(snake.head[0], snake.head[1])
    for i in range(len(snake.body)):
        screen.blit(snake.body[i][0], snake.body[i][1])
    screen.blit(snake.tail[0], snake.tail[1])

def game_over(gagnant,tableau):
    running = True
    screen.fill((200, 200, 200))
    font = pygame.font.SysFont("calibri", 50, True)
    end = font.render("GAME OVER", True, (150,0,0))
    if gagnant == 1:
        result = font.render("Le joueur 1 (rouge) l'emporte !", True, (150, 0, 0))
        screen.blit(result,(160,85))
    elif gagnant == 2 :
        result = font.render("Le joueur 2 (jaune) l'emporte !", True, (150, 0, 0))
        screen.blit(result, (160, 85))
    else:
        result = font.render("C'est une égalité !", True, (150, 0, 0))
        screen.blit(result, (215, 85))

    while running:
        screen.blit(end, (310, 40))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = False
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

apple, grille, head, body,tail,turn_horaire, turn_anti = load_assets()
pygame.init()
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 800))



