from Jeux.Uno.Front.assets import load_assets
import pygame
import sys

def main_menu():
    """
    Affiche le menu principal avec les options "Nouvelle partie" et "Quitter".
    Gère les événements souris pour détecter le choix de l'utilisateur.
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


        screen.fill((50, 200, 50))
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

def display_main_menu(new_game_msg = str, leave_msg = str, title = str, title_ = str):
    """
    Place les boutons du menu principal et le titre sur l'écran.
    """
    screen.blit(new_game_msg, (20, 180))
    screen.blit(leave_msg, (20, 340))
    screen.blit(title, (37, 39))
    screen.blit(title_, (40, 40))

def display_game(players,deck,direction):
    """
    Affiche le plateau de jeu avec la main du joueur, les cartes des bots, la carte en jeu et la pioche.
    Retourne les coordonnées des cartes du joueur pour la détection de clic.
    :return: List[Tuple]
    """
    grid = []
    top = deck.deck[0]
    print(type(top))
    right_arrow = joker[2]
    left_arrow = pygame.transform.rotate(right_arrow, 180)
    factor = get_factor(len(players[0]))

    screen.blit(carpet, (0, 0))

    if direction < 0:
        screen.blit(right_arrow,(400,475))
    else:
        screen.blit(left_arrow,(250,475))

    for i in range(len(players[0])):
        if len(players[0]) < 5:
            dest = (350-50*len(players[0])+i*factor,525)
        else:
            dest = (150 + i * factor, 525)
        grid.append(dest)

        if players[0][i].value == "joker":
            screen.blit(joker[0] ,dest)
        elif players[0][i].value == "joker4":
            screen.blit(joker[1] ,dest)
        else:
            screen.blit(dict_cards[players[0][i].card],dest)

    display_bot(players)
    screen.blit(dict_cards[top.card], (250, 275))
    screen.blit(card_back, (350, 275))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    return grid

def get_factor(hand):
    """
    Calcule l'espacement entre les cartes en fonction du nombre de cartes en main.
    :return: Integer
    """
    if hand<5:
        factor = 100
    else:
        factor = 350 // hand

    return factor

def display_bot(players):
    """
    Place les cartes des bots face caché dans le bon sens.
    """
    card_back_turned_0 = pygame.transform.rotate(card_back, 90)
    card_back_turned_1 = pygame.transform.rotate(card_back, 180)
    card_back_turned_2 = pygame.transform.rotate(card_back, 270)

    factor = get_factor(len(players[1]))

    for i in range(len(players[1])):
        screen.blit(card_back_turned_0, (-90, 150 + i * factor))

    factor = get_factor(len(players[2]))

    for i in range(len(players[2])):
        screen.blit(card_back_turned_1, (150 + i * factor, 5))

    factor = get_factor(len(players[3]))

    for i in range(len(players[3])):
        screen.blit(card_back_turned_2, (630, 150 + i * factor))

def card_choice(players,deck,top,direction):
    """
    Gère la sélection d'une carte par le joueur à la souris.
    Affiche le plateau et attend un clic sur une carte ou le bouton "Piocher".
    :return: Integer or String
    """
    grid = display_game(players,deck,direction)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    for i in range(len(grid) - 1):
                        card_x = grid[i][0]

                        if card_x <= mouse_cord_x <= card_x + grid[i+1][0] - card_x and 525 <= mouse_cord_y <= 675:
                            return i

                    if grid[-1][0] <= mouse_cord_x <= grid[-1][0] + 100 and 525 <= mouse_cord_y <= 695:
                        return len(grid) - 1

                    elif 350 <= mouse_cord_x <= 450 and 275 <= mouse_cord_y <= 425:
                        return "Draw"

def color_choice(card):
    """
    Affiche les 4 couleurs disponibles pour que le joueur choisisse la couleur du joker.
    :return: String
    """
    colors = ["Green", "Blue", "Red", "Yellow"]

    for i in range(4):
        screen.blit(dict_cards[(card.value, colors[i])], (112 + i * 125, 325))

    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    for i in range(4):
                        if 112+i*125 <= mouse_cord_x <= 112+i*125 + 100 and 325 <= mouse_cord_y <= 475:
                            return colors[i]
                    else:
                        return

def game_over(winner):
    """
    Affiche l'écran de fin de partie avec le vainqueur.
    Attend un clic pour retourner au menu.
    :return: Boolean
    """
    font = pygame.font.SysFont("comicsans", 60)
    msg_game_over = font.render("Joueur "+str(winner)+" a gagné !", True, (250, 50, 50))
    font = pygame.font.SysFont("comicsans", 61)
    shadow = font.render("Joueur " + str(winner) + " a gagné !", True, (0, 0, 0))

    while True:
        screen.blit(shadow, (99, 175))
        screen.blit(msg_game_over,(100, 175))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    return True

card_back,dict_cards,carpet, joker = load_assets()
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("UNO")