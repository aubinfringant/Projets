from Library.Jeux.Uno.Front.assets import load_assets
import pygame

def main_menu():
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    title_ = font.render("UNO", True, (255, 255, 255))
    title = font.render("UNO", True, (200, 0, 0))

    font = pygame.font.SysFont("calibri", 50, True)
    new_game = font.render("Nouvelle partie", True, (100, 100, 100))
    leave = font.render("Quitter", True, (100, 100, 100))

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

        screen.fill((50, 200, 50))
        affichage_main_menu(title_,title,new_game,leave)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1,3) and 338 > mouse_cord_x > 22 and 220 > mouse_cord_y > 180:
                    return True
                elif event.button in (1,3) and 161 > mouse_cord_x > 22 and 380 > mouse_cord_y > 340:
                    return False

def affichage_main_menu(title_,title,new_game,leave):
    screen.blit(title_, (37, 39))
    screen.blit(title, (40, 40))
    screen.blit(new_game, (20, 180))
    screen.blit(leave, (20, 340))

def display_game(players,deck,top,direction):
    grid = []
    right_arrow = joker[2]
    left_arrow = pygame.transform.rotate(joker[2], 180)

    card_back_turned_0 = pygame.transform.rotate(card_back, 90)
    card_back_turned_1 = pygame.transform.rotate(card_back, 180)
    card_back_turned_2 = pygame.transform.rotate(card_back, 270)

    if len(players[0])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[0])

    screen.blit(carpet, (0, 0))

    if direction < 0:
        screen.blit(right_arrow,(400,475))
    else:
        screen.blit(left_arrow,(250,475))

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
            screen.blit(dict_cards[players[0][i].card],dest)

    if len(players[1])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[1])

    for i in range(len(players[1])):
        screen.blit(card_back_turned_0, (-90, 150 + i * facteur))

    if len(players[2])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[2])

    for i in range(len(players[2])):
        screen.blit(card_back_turned_1, (150 + i * facteur, 5))

    if len(players[3])<5:
        facteur = 100
    else:
        facteur = 350 // len(players[3])

    for i in range(len(players[3])):
        screen.blit(card_back_turned_2, (630, 150 + i * facteur))

    screen.blit(dict_cards[top.card],(250, 275))
    screen.blit(card_back,(350, 275))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True, grid

def card_choice(players,deck,top,direction):
    running,grid = display_game(players,deck,top,direction)
    while running:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            mouse_button = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                return False,None

            if mouse_button[0]:
                for i in range(len(grid)-1):
                    if grid[i][0] <= x <= grid[i][0] + grid[i+1][0] - grid[i][0] and 525 <= y <= 675:
                        return True, i

                if grid[-1][0] <= x <= grid[-1][0] + 100 and 525 <= y <= 695:
                    return True, len(grid)-1

                elif 350<=x<=450 and 275<=y<=425:
                    return True, "Draw"

    return False, None


def color_choice(card):
    running = True
    colors = ["Green", "Blue", "Red", "Yellow"]

    while running:
        for i in range(4):
            screen.blit(dict_cards[(card.value,colors[i])],(112+i*125,325))

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

def game_over(winner):
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
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1,3):
                    pygame.time.wait(300)
                    return  True

#initialisation globale
card_back,dict_cards,carpet, joker = load_assets()
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("UNO")