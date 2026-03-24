from Library.Jeux.Bataille.Front.assets import load_assets
import pygame
def main_menu():
    deck_png, carte_dos, dico_de_cartes, tapis = load_assets()
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("BATAILLE")
    font = pygame.font.SysFont("Arial", 30)
    clock = pygame.time.Clock()
    melange = font.render("Melange", True, (255, 255, 255))
    jouer, quitter = 0, 0
    choix_en_cours = True
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    msg = font.render("Bataille", True, (255, 255, 255))
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    msg_titre = font.render("Bataille", True, (200, 0, 0))
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

def jeu(pli,j1,j2):
    screen.blit(tapis, (0, 0))
    screen.blit(carte_dos, (100, 200))
    screen.blit(carte_dos, (500, 200))
    deck_ingage = []
    for i in range(len(pli)):
        deck_ingage.append(dico_de_cartes[pli[i].card])
    for i in range(0, len(deck_ingage), 2):
        screen.blit(deck_ingage[i], (210, 200 + 25 * i))
        screen.blit(deck_ingage[i + 1], (390, 200 + 25 * i))
    card_joueur = font.render(str(len(j1)), True, (255, 255, 255))
    card_ordi = font.render(str(len(j2)), True, (255, 255, 255))

    screen.blit(card_joueur, (128, 150))
    screen.blit(card_ordi, (528, 150))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.time.delay(30)


deck_png, carte_dos,dico_de_cartes,tapis = load_assets()
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("BATAILLE")
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()
melange = font.render("Melange", True, (255, 255, 255))