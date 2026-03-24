from Library.Jeux.Memory.Front.assets import load_assets
from Library.Jeux.Memory.Class.Grid import *
from copy import deepcopy
import pygame

def main_menu():
    carte_dos, dico_de_cartes, tapis = load_assets()
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("MEMORY")
    jouer, quitter = 0, 0
    choix_en_cours = True
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    msg = font.render("Memory", True, (255, 255, 255))
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    msg_titre = font.render("Memory", True, (200, 0, 0))
    font = pygame.font.SysFont("calibri", 50, True)
    msg_nouvelle_partie = font.render("Nouvelle partie", True, (100, 100, 100))
    msg_quitter = font.render("Quitter", True, (100, 100, 100))
    while choix_en_cours:
        screen.fill((50, 200, 50))
        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()
        if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
            msg_nouvelle_partie = font.render("Nouvelle partie", True, (50, 50, 50))
            affichage_main_menu(msg,msg_titre,msg_nouvelle_partie,msg_quitter)
        else:
            msg_nouvelle_partie = font.render("Nouvelle partie", True, (100, 100, 100))
            affichage_main_menu(msg,msg_titre,msg_nouvelle_partie,msg_quitter)

        if 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
            msg_quitter = font.render("Quitter", True, (50, 50, 50))
            affichage_main_menu(msg,msg_titre,msg_nouvelle_partie,msg_quitter)
        else:
            msg_quitter = font.render("Quitter", True, (100, 100, 100))
            affichage_main_menu(msg,msg_titre,msg_nouvelle_partie,msg_quitter)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choix_en_cours = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == (1 or 3) and 338 > mouse_cord_x > 22 and 220 > mouse_cord_y > 180:
                    jouer += 1
                elif event.button == (1 or 3) and 161 > mouse_cord_x > 22 and 380 > mouse_cord_y > 340:
                    quitter += 1
        if jouer == 1:
            jouer = 0
            choix_en_cours = False
            return
        elif quitter == 1:
            choix_en_cours = False
            pygame.quit()
            return

def affichage_main_menu(msg,msg_titre,msg_nouvelle_partie,msg_quitter):
    screen.blit(msg, (37, 39))
    screen.blit(msg_titre, (40, 40))
    screen.blit(msg_nouvelle_partie, (20, 180))
    screen.blit(msg_quitter, (20, 340))

def jeu(grille,cartes_trouve):
    running = True
    screen.blit(tapis, (0, 0))
    for i in range(len(grille.grid)):
        for j in range(len(grille.grid[i])):
            dest = (j * 110, i*160)
            if grille.grid[i][j].card in cartes_trouve:
                screen.blit(dico_de_cartes[grille.grid[i][j].card],dest)
            else:
                screen.blit(carte_dos, dest)
    pygame.display.flip()
    pygame.time.wait(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

def choix_cartes(grille,cartes_trouve,choix):
    grille_colid = [[[0 + i * 110, 0 + j * 160]
                     for i in range(len(grille.grid[0]))]
                     for j in range(len(grille.grid))]
    running = True
    while running:
        choix_copy = deepcopy(choix)
        screen.blit(tapis, (0, 0))
        for i in range(len(grille.grid)):
            for j in range(len(grille.grid[i])):

                dest = (j * 110, i * 160)
                if grille.grid[i][j].card in cartes_trouve:
                    screen.blit(dico_de_cartes[grille.grid[i][j].card], dest)

                elif len(choix_copy) == 2:
                    if grille.grid[i][j].card == choix_copy[1][0] and grille_colid[i][j] == choix_copy[1][1]:
                        screen.blit(dico_de_cartes[choix_copy[1][0]], dest)
                        choix_copy.pop(1)
                    elif grille.grid[i][j].card == choix_copy[0][0] and grille_colid[i][j] == choix_copy[0][1]:
                        screen.blit(dico_de_cartes[choix_copy[0][0]], dest)
                        choix_copy.pop(0)
                    else:
                        screen.blit(carte_dos, dest)

                elif len(choix_copy) == 1:
                    if grille.grid[i][j].card == choix_copy[0][0] and grille_colid[i][j] == choix_copy[0][1]:
                        screen.blit(dico_de_cartes[choix_copy[0][0]], dest)
                        choix_copy.pop(0)
                    else:
                        screen.blit(carte_dos, dest)

                else:
                    screen.blit(carte_dos, dest)
        pygame.display.flip()

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            mouse_button = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if mouse_button[0]:
                for i in range(len(grille.grid)):
                    for j in range(len(grille.grid[0])):
                        if grille_colid[i][j][0] <= x <= grille_colid[i][j][0] + 100 and grille_colid[i][j][1] <= y <= \
                                grille_colid[i][j][1] + 150:
                            if len(choix)>0:
                                if choix[0][1] != grille_colid[i][j]:
                                    return grille.grid[i][j].card,grille_colid[i][j]
                            else:
                                return grille.grid[i][j].card, grille_colid[i][j]

carte_dos,dico_de_cartes,tapis = load_assets()
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("BATAILLE")
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()