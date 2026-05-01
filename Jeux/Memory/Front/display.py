from Jeux.Memory.Front.assets import load_assets
import sys
import pygame

def main_menu():
    """
    Gére l'affichage du menu principale et du choix fait dedans
    :return: Boolean
    """
    font = pygame.font.SysFont("timesnewroman", 70, True, True)
    title = font.render("Memory", True, (255, 255, 255))
    title_ = font.render("Memory", True, (200, 0, 0))

    font = pygame.font.SysFont("calibri", 50, True)

    while True:

        mouse_cord_x, mouse_cord_y = pygame.mouse.get_pos()

        if 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
            msg_new_game = font.render("Nouvelle partie", True, (50, 50, 50))
        else:
            msg_new_game = font.render("Nouvelle partie", True, (100, 100, 100))

        if 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
            msg_leave = font.render("Quitter", True, (50, 50, 50))
        else:
            msg_leave = font.render("Quitter", True, (100, 100, 100))

        screen.fill((50, 200, 50))
        display_title(title, title_)
        display_main_menu(msg_new_game, msg_leave)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3) and 22 < mouse_cord_x < 338 and 180 < mouse_cord_y < 220:
                    return True

                elif event.button in (1, 3) and 22 < mouse_cord_x < 161 and 340 < mouse_cord_y < 380:
                    pygame.quit()
                    sys.exit()

def display_main_menu(new_game_msg = str, leave_msg = str):
    """
    Place les eléments sur l'écran.
    """
    screen.blit(new_game_msg, (20, 180))
    screen.blit(leave_msg, (20, 340))

def display_title(title = str, title_ = str):
    """
    Place les eléments sur l'écran.
    """
    screen.blit(title, (37, 39))
    screen.blit(title_, (40, 40))

def display_cards(grid, grid_colid, found_cards, choices):
    """
    Place et affiche les cartes sur l'écran.
    """
    screen.blit(tapis, (0, 0))
    for i in range(len(grid.grid)):
        for j in range(len(grid.grid[i])):
            screen.blit(card_back, grid_colid[i][j])

    for pair in found_cards:
        for card in pair:
            screen.blit(card_sprites[card[0]], card[1])

    for card in choices:
        screen.blit(card_sprites[card[0]], card[1])

    pygame.display.flip()

def confirmation(grid, found_cards, choices):
    """
    Fais une pause pour bien mémoriser les deux cartes différentes.
    """
    grid_colid = [[[135 + i * 110, 30 + j * 160]
                   for i in range(len(grid.grid[0]))]
                  for j in range(len(grid.grid))]

    while True:
        display_cards(grid, grid_colid, found_cards, choices)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    return

def card_choice(grid, found_cards, choices):
    """
    Grosse fonction qui fait peur mais en vrai c'est juste des vérifs
    pour savoir si on a déjà selectionné la carte.
    :return: list[tuple,[int,int]]
    """
    grid_colid = [[[135 + i * 110, 30 + j * 160]
                     for i in range(len(grid.grid[0]))]
                     for j in range(len(grid.grid))]

    while True:
        pygame.event.clear()
        display_cards(grid, grid_colid, found_cards, choices)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    x, y = pygame.mouse.get_pos()

                    for i in range(len(grid.grid)):
                        for j in range(len(grid.grid[0])):

                            cord = grid_colid[i][j]
                            card = grid.grid[i][j].card

                            if cord[0] <= x <= cord[0] + 100 and cord[1] <= y <= cord[1] + 150:
                                same = False
                                if len(found_cards) != 0:

                                    for pair in found_cards:
                                        for cards in pair:
                                            if card == cards[0]:
                                                same = True

                                    if not same:

                                        if len(choices) == 0:
                                            return [card, cord]

                                        if choices[0][1] != cord:
                                            return [card, cord]
                                else:
                                    if len(choices) == 0:
                                        return [card, cord]

                                    if choices[0][1] != cord:
                                        return [card, cord]

card_back, card_sprites, tapis = load_assets()
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("MEMORY")
