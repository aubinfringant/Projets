from Jeux.Memory.Front.assets import load_assets
import sys
import pygame

def display_cards(grid, grid_colid, found_cards, choices):
    """
    Place et affiche les cartes sur l'écran.
    """
    screen.blit(carpet, (0, 0))
    for i in range(len(grid.grid)):
        for j in range(len(grid.grid[i])):
            screen.blit(card_back, grid_colid[i][j])

    for pair in found_cards:
        for card in pair:
            screen.blit(cards_sprite[card[0]], card[1])

    for card in choices:
        screen.blit(cards_sprite[card[0]], card[1])

    pygame.display.flip()

def confirmation(grid, found_cards, choices):
    """
    Fais une pause pour bien mémoriser les deux cartes différentes.
    """
    grid_colid = [[[135 + i * 110, 30 + j * 160]
                   for i in range(len(grid.grid[0]))]
                  for j in range(len(grid.grid))]

    while True:
        clock.tick(60)
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
        clock.tick(60)
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

card_back, cards_sprite, carpet = load_assets()
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("MEMORY")
clock = pygame.time.Clock()
