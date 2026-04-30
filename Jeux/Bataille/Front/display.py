from Jeux.Bataille.Front.assets import load_assets
import pygame

def main_menu(): #-> Boolean

    font = pygame.font.SysFont("calibri", 50, True)
    new_game_msg = font.render("Nouvelle partie", True, (100, 100, 100))
    leave_msg = font.render("Quitter", True, (100, 100, 100))


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
        display_title()
        display_main_menu(new_game_msg, leave_msg)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3) and 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
                    return True
                elif event.button in (1, 3) and 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
                    pygame.quit()
                    return False

def display_main_menu(new_game_msg,leave_msg): #-> None

    screen.blit(new_game_msg, (20, 180))
    screen.blit(leave_msg, (20, 340))

def display_title(): #-> None

    screen.blit(msg, (37, 39))
    screen.blit(msg_titre, (40, 40))

def display_num_of_card(p1,p2): #-> None

    font = pygame.font.SysFont("calibri", 50, True)
    card_joueur = font.render(str(len(p1)), True, (255, 255, 255))
    card_ordi = font.render(str(len(p2)), True, (255, 255, 255))

    screen.blit(card_joueur, (128, 150))
    screen.blit(card_ordi, (528, 150))

def display_choose(trick,p1,p2): #-> None or Binairy

    card1 = cards_sprite[p1[0].card]
    card2 = cards_sprite[p1[1].card]

    while True:
        deck_ingage = []

        screen.blit(tapis, (0, 0))
        screen.blit(carte_dos, (100, 200))
        screen.blit(carte_dos, (500, 200))

        for i in range(len(trick)):
            deck_ingage.append(cards_sprite[trick[i].card])

        for i in range(0, len(deck_ingage), 2):
            screen.blit(deck_ingage[i], (210, 200 + 25 * i))
            screen.blit(deck_ingage[i + 1], (390, 200 + 25 * i))

        if len(deck_ingage) == 0:
            screen.blit(cards_sprite[p2[0].card], (390, 200 + 25 * (len(deck_ingage)//2)))
        else:
            screen.blit(cards_sprite[p2[0].card], (390, 200 + 25 * (len(deck_ingage)+1//2)))

        display_num_of_card(p1, p2)

        screen.blit(card1, (100, 500))
        screen.blit(card2, (220, 500))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    x, y = pygame.mouse.get_pos()
                    if 100 < x < 200 and 500 < y < 650:
                        return 0
                    if 220 < x < 320 and 500 < y < 650:
                        return 1

def display_game(trick,p1,p2): #-> Boolean

    screen.blit(tapis, (0, 0))
    screen.blit(carte_dos, (100, 200))
    screen.blit(carte_dos, (500, 200))
    deck_ingage = []

    for i in range(len(trick)):
        deck_ingage.append(cards_sprite[trick[i].card])

    for i in range(0, len(deck_ingage), 2):
        screen.blit(deck_ingage[i], (210, 200 + 25 * i))
        screen.blit(deck_ingage[i + 1], (390, 200 + 25 * i))

    display_num_of_card(p1,p2)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False

    pygame.time.delay(300)
    return True

def display_game_over(p1,p2): #-> Boolean

    font = pygame.font.SysFont("calibri", 70, True)

    while True:

        if len(p1) == 0:
            msg1 = font.render("GAME OVER", True, (200, 100, 100))
            msg2 = font.render("Player 2 GAGNE !", True, (200, 100, 100))

        else:
            msg1 = font.render("GAME OVER", True, (200, 100, 100))
            msg2 = font.render("Player 1 GAGNE !", True, (200, 100, 100))


        screen.blit(msg1, (165, 180))
        screen.blit(msg2, (110, 380))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1,3):
                    return True



pygame.init()
pygame.display.set_caption("BATAILLE")
screen = pygame.display.set_mode((700,700))

deck_png, carte_dos,cards_sprite,tapis = load_assets()

font = pygame.font.SysFont("timesnewroman", 70, True, True)
msg = font.render("Bataille", True, (255, 255, 255))
msg_titre = font.render("Bataille", True, (200, 0, 0))