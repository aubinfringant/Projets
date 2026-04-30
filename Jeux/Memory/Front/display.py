from Library.Jeux.Memory.Front.assets import load_assets
import pygame

def main_menu(): #-> Boolean

    font = pygame.font.SysFont("calibri", 50, True)
    msg_new_game = font.render("Nouvelle partie", True, (100, 100, 100))
    msg_leave = font.render("Quitter", True, (100, 100, 100))

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
        display_title()
        display_main_menu(msg_new_game, msg_leave)

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

def display_title(): #-> None

    screen.blit(msg, (37, 39))
    screen.blit(msg_title, (40, 40))

def display_main_menu(msg_new_game, msg_leave): #-> None

    screen.blit(msg_new_game, (20, 180))
    screen.blit(msg_leave, (20, 340))

def display_cards(grid, grid_colid, found_cards, choices): #-> None
    screen.blit(tapis, (0, 0))

    for i in range(len(grid.grid)):
        for j in range(len(grid.grid[i])):

            dest = (135 + j * 110, 30 + i * 160)
            card = grid.grid[i][j].card
            cord = grid_colid[i][j]

            if card in found_cards:
                screen.blit(card_sprites[card], dest)
            else:
                drawn = False
                for choice in choices:
                    if card == choice[0] and cord == choice[1]:
                        screen.blit(card_sprites[card], dest)
                        drawn = True
                        break

                if not drawn:
                    screen.blit(card_back, dest)

    pygame.display.flip()

def card_choice(grid, found_cards, choices, pause=False): #-> None or tuple, tuple

    grid_colid = [[[135 + i * 110, 30 + j * 160]
                     for i in range(len(grid.grid[0]))]
                     for j in range(len(grid.grid))]

    while True:
        pygame.event.clear()
        display_cards(grid, grid_colid, found_cards, choices)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):

                    if pause:
                        return True

                    x, y = pygame.mouse.get_pos()

                    for i in range(len(grid.grid)):
                        for j in range(len(grid.grid[0])):

                            cord = grid_colid[i][j]
                            card = grid.grid[i][j].card

                            if cord[0] <= x <= cord[0] + 100 and cord[1] <= y <= cord[1] + 150:

                                if card in found_cards:
                                    continue

                                if len(choices) == 0:
                                    return card, cord

                                if choices[0][1] != cord:
                                    return card, cord



card_back, card_sprites, tapis = load_assets()
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("MEMORY")

font = pygame.font.SysFont("timesnewroman", 70, True, True)
msg = font.render("Memory", True, (255, 255, 255))
msg_title = font.render("Memory", True, (200, 0, 0))
