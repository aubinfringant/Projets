from Library.Jeux.Uno.Front.assets import load_assets
import pygame

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("UNO")
    jouer, quitter = 0, 0
    choix_en_cours = True
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    msg = font.render("UNO", True, (255, 255, 255))
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    msg_titre = font.render("UNO", True, (200, 0, 0))
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
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == (1 or 3) and 338 > mouse_cord_x > 22 and 220 > mouse_cord_y > 180:
                    jouer += 1
                elif event.button == (1 or 3) and 161 > mouse_cord_x > 22 and 380 > mouse_cord_y > 340:
                    quitter += 1
        if jouer == 1:
            jouer = 0
            choix_en_cours = False
            return True
        elif quitter == 1:
            choix_en_cours = False
            pygame.quit()
            return False

def affichage_main_menu(msg,msg_titre,msg_nouvelle_partie,msg_quitter):
    screen.blit(msg, (37, 39))
    screen.blit(msg_titre, (40, 40))
    screen.blit(msg_nouvelle_partie, (20, 180))
    screen.blit(msg_quitter, (20, 340))

def display(players,deck,top,sens):
    clock.tick(60)
    screen.blit(tapis, (0, 0))
    if sens < 0:
        screen.blit(joker[2],(400,475))
    else:
        fleche_gauqhe = pygame.transform.rotate(joker[2], 180)
        screen.blit(fleche_gauqhe,(250,475))
    if len(players[0])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[0])
    grid = []
    for i in range(len(players[0])):
        if len(players[0]) < 5:
            dest = (350-50*len(players[0])+i*facteur,525)
        else:
            dest = (150 + i * facteur, 525)
        grid.append(dest)
        if players[0][i].value == "joker":
            screen.blit(joker[0],dest)
        elif players[0][i].value == "joker4":
            screen.blit(joker[1],dest)
        else:
            screen.blit(dico_de_cartes[players[0][i].card],dest)
    carte_dos_tourne_0 = pygame.transform.rotate(carte_dos,90)
    carte_dos_tourne_1 = pygame.transform.rotate(carte_dos,180)
    carte_dos_tourne_2 = pygame.transform.rotate(carte_dos, 270)
    if len(players[1])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[1])
    for i in range(len(players[1])):
        screen.blit(carte_dos_tourne_0, (-90, 150 + i * facteur))
    if len(players[2])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[2])
    for i in range(len(players[2])):
        screen.blit(carte_dos_tourne_1, (150 + i * facteur, 5))
    if len(players[3])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[3])
    for i in range(len(players[3])):
        screen.blit(carte_dos_tourne_2, (630, 150 + i * facteur))

    screen.blit(dico_de_cartes[top.card],(250, 275))
    screen.blit(carte_dos_tourne_1,(350, 275))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False,None
    return True,grid

def choix_cartes(players,deck,top,sens):
    running,grid = display(players,deck,top,sens)
    pygame.time.wait(40)
    while running:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            mouse_button = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                running = False
                return running,None
            if mouse_button[0]:
                for i in range(len(grid)-1):
                    if grid[i][0] <= x <= grid[i][0] + grid[i+1][0] - grid[i][0] and 525 <= y <= 675:
                        return True,i+1
                if grid[-1][0] <= x <= grid[-1][0] + 100 and 525 <= y <= 695:
                    return True,len(grid)
                elif 350<=x<=450 and 275<=y<=425:
                    return True, "Draw"
    return running, None

def choix_couleur(card):
    pygame.time.wait(40)
    running = True
    colors = ["Green", "Blue", "Red", "Yellow"]
    while running:
        for i in range(4):
            screen.blit(dico_de_cartes[(card.value,colors[i])],(112+i*125,325))
        pygame.display.flip()
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            mouse_button = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                running = False
                return running, None
            if mouse_button[0]:
                for i in range(4):
                    if 112+i*125 <= x <= 112+i*125 + 100 and 325 <= y <= 475:
                        return True, colors[i]

def game_over(players, deck, top, gagnant, sens):
    running, grid = display(players, deck, top,sens)
    pygame.time.wait(40)
    font = pygame.font.SysFont("comicsans", 60)
    msg_game_over = font.render("Joueur "+str(gagnant)+" a gagné !", True, (250, 50, 50))
    font = pygame.font.SysFont("comicsans", 61)
    shadow = font.render("Joueur " + str(gagnant) + " a gagné !", True, (0, 0, 0))
    while running:
        screen.blit(shadow, (99, 175))
        screen.blit(msg_game_over,(100, 175))

        pygame.display.flip()
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            mouse_button = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                running = False
                return running, None
            if mouse_button[0]:
                pygame.time.wait(1500)
                return running, True

    return running, None

carte_dos,dico_de_cartes,tapis, joker = load_assets()
print(dico_de_cartes)
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("UNO")
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()